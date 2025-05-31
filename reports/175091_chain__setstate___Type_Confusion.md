# chain.__setstate__ Type Confusion

## Report Details
- **Report ID**: 175091
- **URL**: https://hackerone.com/reports/175091
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-10-11T08:14:36.540Z
- **Disclosed**: 2016-12-05T00:30:56.041Z

## Reporter
- **Username**: johnleitch
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Python 3.5.2 suffers from a type confusion vulnerability in the chain.__setstate__ method of the itertools module. The issue exists due to lack of argument validation in the chain_setstate() function:

    static PyObject *
    chain_setstate(chainobject *lz, PyObject *state)
    {
        PyObject *source, *active=NULL;

        if (! PyArg_ParseTuple(state, "O|O", &source, &active))
            return NULL;

        Py_INCREF(source);
        Py_XSETREF(lz->source, source);
        Py_XINCREF(active);
        Py_XSETREF(lz->active, active);
        Py_RETURN_NONE;
    }

After parsing the argument tuple, source and active are set without validating that they are iterator objects. This causes issues elsewhere, where the values are passed PyIter_Next:

    static PyObject *
    chain_next(chainobject *lz)
    {
        PyObject *item;

        if (lz->source == NULL)
            return NULL;                                    /* already stopped */

        if (lz->active == NULL) {
            PyObject *iterable = PyIter_Next(lz->source);
            if (iterable == NULL) {
                Py_CLEAR(lz->source);
                return NULL;                                /* no more input sources */
            }
            lz->active = PyObject_GetIter(iterable);
            Py_DECREF(iterable);
            if (lz->active == NULL) {
                Py_CLEAR(lz->source);
                return NULL;                                /* input not iterable */
            }
        }
        item = PyIter_Next(lz->active);
        if (item != NULL)
            return item;
        if (PyErr_Occurred()) {
            if (PyErr_ExceptionMatches(PyExc_StopIteration))
                PyErr_Clear();
            else
                return NULL;                                /* input raised an exception */
        }
        Py_CLEAR(lz->active);
        return chain_next(lz);                      /* recurse and use next active */
    }

In some cases, this can lead to a DEP access violation. It might be possible to exploit this to achieve code execution.

    (4074.198c): Access violation - code c0000005 (first chance)
    First chance exceptions are reported before any exception handling.
    This exception may be expected and handled.
    eax=00000000 ebx=0132fa10 ecx=5b547028 edx=00000002 esi=0132fa10 edi=5b37b3e0
    eip=00000000 esp=009ef940 ebp=009ef94c iopl=0         nv up ei pl zr na pe nc
    cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010246
    00000000 ??              ???
    0:000> k6
    ChildEBP RetAddr  
    WARNING: Frame IP not in any known module. Following frames may be wrong.
    009ef93c 5b329ac0 0x0
    009ef94c 5b2cb321 python35!PyIter_Next+0x10 [c:\build\cpython\objects\abstract.c @ 2778]
    009ef960 5b37b42e python35!chain_next+0x21 [c:\build\cpython\modules\itertoolsmodule.c @ 1846]
    009ef970 5b33fedd python35!wrap_next+0x4e [c:\build\cpython\objects\typeobject.c @ 5470]
    009ef990 5b328b9d python35!wrapper_call+0x7d [c:\build\cpython\objects\descrobject.c @ 1195]
    009ef9ac 5b3c463c python35!PyObject_Call+0x6d [c:\build\cpython\objects\abstract.c @ 2167]

To fix this issue, it is recommended that chain_setstate() be updated to validate its arguments. A proposed patch has been attached.

    static PyObject *
    chain_setstate(chainobject *lz, PyObject *state)
    {
        PyObject *source, *active=NULL;

        if (! PyArg_ParseTuple(state, "O|O", &source, &active))
            return NULL;

        if (!PyIter_Check(source) || (active != NULL && !PyIter_Check(active))) {
            PyErr_SetString(PyExc_ValueError, "Arguments must be iterators.");
            return NULL;
        }

        Py_INCREF(source);
        Py_XSETREF(lz->source, source);
        Py_XINCREF(active);
        Py_XSETREF(lz->active, active);
        Py_RETURN_NONE;
    }

## Attachments
No attachments
