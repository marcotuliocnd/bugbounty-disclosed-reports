# Type confusion in FutureIter_throw() which may potentially lead to an arbitrary code execution

## Report Details
- **Report ID**: 182169
- **URL**: https://hackerone.com/reports/182169
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-11-14T21:37:24.096Z
- **Disclosed**: 2016-12-03T20:13:05.980Z

## Reporter
- **Username**: artem
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Hello,

I reported this directly to security@python.org. The issue has been fixed. Python Team confirmed that it's fixed and disclosed:

It's disclosed. Feel free to file a bug if that would be helpful to you. 



On Mon, Nov 14, 2016, at 09:54, Artem Smotrakov wrote:
> Hello Benjamin,
>
> I am planning to submit it to https://hackerone.com/ibb-python to see if
> it's eligible. Since the fix is in public repo, may it be considered as
> disclosed? Or, should I wait for next release?
>
> Is there a bug id for it?
>
> Thanks for fixing this quickly!
>
> Artem
>
> 2016-11-14 0:17 GMT-08:00 Benjamin Peterson <benjamin@python.org>:
>
> > Thank you for the report. Fixed in
> > https://hg.python.org/cpython/rev/3ea121235ede


Here is the original report:




Hello Python Security Team,

A type confusion may occur in FutureIter_throw() method of _asynciomodule:

https://hg.python.org/cpython/file/tip/Modules/_asynciomodule.c#l1022

```
static PyObject *
FutureIter_throw(futureiterobject *self, PyObject *args)
{
    PyObject *type=NULL, *val=NULL, *tb=NULL;
    if (!PyArg_ParseTuple(args, "O|OO", &type, &val, &tb))
        return NULL;

    if (val == Py_None) {
        val = NULL;
    }
    if (tb == Py_None) {
        tb = NULL;
    }

    Py_CLEAR(self->future);

    if (tb != NULL) {
        PyErr_Restore(type, val, tb);
    }
```

The method doesn't check types of "type" and "val", and passes them to PyErr_Restore().

PyErr_Restore() method doesn't perform any type check on "type" and "val" either,
and stores them "as is" to "tstate->curexc_type" and "tstate->curexc_value".

https://hg.python.org/cpython/file/tip/Python/errors.c#l27

Then, "tstate->curexc_value" can be retrieved by PyErr_Fetch() funciton,
and callers will assume that it returns an object of exception type.
This results to a type confusion.

There are a lot of invocation of PyErr_Fetch() which may lead to different consequences.
I am attaching two POCs which demonstrates the problem.

1. FutureIter_type_confusion_1.py results to a crash with the following output:

```
in A.__init__
in A.__str__
in except, e = this is not an exception
in except, type(e) = <class 'Exception'>
Traceback (most recent call last):
  File "./FutureIter_type_confusion_report/FutureIter_type_confusion_1.py", line 13, in <module>
Segmentation fault (core dumped)
```

2. FutureIter_type_confusion_2.py shows that the issue may lead to overwritting function pointers
which may potentially result to an arbitrary code execution:

```
(gdb) run
Starting program: /home/artem/projects/python/build/cpython-normal/bin/python3 ./FutureIter_type_confusion_report/FutureIter_type_confusion_2.py
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Program received signal SIGSEGV, Segmentation fault.
0x00000000004b751a in PyObject_Repr (v=0xae1890) at Objects/object.c:474
474	    if (Py_TYPE(v)->tp_repr == NULL)
(gdb) p v->ob_type->tp_repr
Cannot access memory at address 0x50607020304050c8
(gdb) list
469	        return NULL;
470	    }
471	#endif
472	    if (v == NULL)
473	        return PyUnicode_FromString("<NULL>");
474	    if (Py_TYPE(v)->tp_repr == NULL)
475	        return PyUnicode_FromFormat("<%s object at %p>",
476	                                    v->ob_type->tp_name, v);
477
478	#ifdef Py_DEBUG
479	    /* PyObject_Repr() must not be called with an exception set,
480	       because it may clear it (directly or indirectly) and so the
481	       caller loses its exception */
482	    assert(!PyErr_Occurred());
483	#endif
484
485	    res = (*v->ob_type->tp_repr)(v);
486	    if (res == NULL)
487	        return NULL;
488	    if (!PyUnicode_Check(res)) {
(gdb)
```

"v->ob_type->tp_repr" contains an invalid address 0x50607020304050c8, so it results to a crash.
But this address is controlled by an attacker.
"v->ob_type->tp_repr" is called later in line 485, so if it had a valid pointer,
then it may potentially lead to full control of instruction pointer.


FutureIter_throw() accepts any types, and confused "tstate->curexc_value" may be used in lots of places,
so there may be much more many ways to use this problem.

I am also attaching an untested patch which updates FutureIter_throw() function to check types of its parameters.
The patch seems to solve the problem. I am wondering if such a check might be added to PyErr_Restore() to prevent similar issues.

## Attachments
- FutureIter_type_confusion.patch
- FutureIter_type_confusion_1.py
- FutureIter_type_confusion_2.py
