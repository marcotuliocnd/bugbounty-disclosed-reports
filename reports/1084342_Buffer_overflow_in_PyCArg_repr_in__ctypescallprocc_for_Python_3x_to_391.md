# Buffer overflow in PyCArg_repr in _ctypes/callproc.c for Python 3.x to 3.9.1

## Report Details
- **Report ID**: 1084342
- **URL**: https://hackerone.com/reports/1084342
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-01-22T09:48:45.890Z
- **Disclosed**: 2021-08-25T20:32:53.759Z

## Reporter
- **Username**: jordyzomer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
**TL;DR Description**

Python 3.x through 3.9.1 has a buffer overflow in PyCArg_repr in _ctypes/callproc.c, which may lead to remote code execution in certain Python applications that accept floating-point numbers as untrusted input, as demonstrated by a 1e300 argument to c_double.from_param. This occurs because sprintf is used unsafely. The CVE number used for this vulnerability is CVE-2021-3177.

**Details**

There's a buffer overflow in the PyCArg_repr() function in _ctypes/callproc.c.

The buffer overflow happens due to not checking the length of th sprintf() function on line: 

    case 'd':
        sprintf(buffer, "<cparam '%c' (%f)>",
            self->tag, self->value.d);
        break;

Because we control self->value.d we could make it copy _extreme_ values. For example we could make it copy 1e300 which would be a 1 with 300 zero's  to overflow the buffer.

This could potentially cause RCE when a user allows untrusted input in these functions.

**Proof of Concept**

>>> from ctypes import *
>>> c_double.from_param(1e300)
*** buffer overflow detected ***: terminated
Aborted


**References**

    MISC:https://bugs.python.org/issue42938
    MISC:https://github.com/python/cpython/pull/24239
    MISC:https://python-security.readthedocs.io/vuln/ctypes-buffer-overflow-pycarg_repr.html

## Impact

**Availability**

Buffer overflows generally lead to crashes. Other attacks leading to lack of availability are possible, including putting the program into an infinite loop.


**Access Control**

Buffer overflows often can be used to execute arbitrary code, which is usually outside the scope of a program’s implicit security policy.

**Other**

 When the consequence is arbitrary code execution, this can often be used to subvert any other security service.

## Attachments
No attachments
