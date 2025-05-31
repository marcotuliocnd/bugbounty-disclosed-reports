# Unsafe arithmetic in PyString_DecodeEscape

## Report Details
- **Report ID**: 241202
- **URL**: https://hackerone.com/reports/241202
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-06-18T17:17:37.672Z
- **Disclosed**: 2017-08-15T11:50:42.211Z

## Reporter
- **Username**: jaybosamiya
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
I have submitted a vulnerability that has now been fixed. The report includes a proof of concept that demonstrates reliable heap corruption through integer overflow. I also submitted a patch which was accepted and merged.

https://bugs.python.org/issue30657

---

In Python 2.7, there is a possible integer overflow in PyString_DecodeEscape function of the file stringobject.c, which can be abused to gain a heap overflow, possibly leading to arbitrary code execution.

The relevant parts of the code are highlighted below:

```
    PyObject *PyString_DecodeEscape(const char *s,
                                    Py_ssize_t len,
                                    const char *errors,
                                    Py_ssize_t unicode,
                                    const char *recode_encoding)
    {
        int c;
        char *p, *buf;
        const char *end;
        PyObject *v;
(1)     Py_ssize_t newlen = recode_encoding ? 4*len:len;
(2)     v = PyString_FromStringAndSize((char *)NULL, newlen);
        if (v == NULL)
            return NULL;
(3)     p = buf = PyString_AsString(v);
        end = s + len;
        while (s < end) {
            if (*s != '\\') {
              non_esc:
    #ifdef Py_USING_UNICODE
    [...]
    #else
(4)             *p++ = *s++;
    #endif
                continue;
    [...]
            }
        }
        if (p-buf < newlen)
            _PyString_Resize(&v, p - buf); /* v is cleared on error */
        return v;
      failed:
        Py_DECREF(v);
        return NULL;
    }
```

(1) If recode_encoding is true (i.e., non-null), we have an integer overflow here which can set newlen to be some very small value
(2) This allows a small string to be created into v
(3) Now p (and buf) use that small string
(4) The small string is copied into with a larger string, thereby giving a heap buffer overflow

In the highly unlikely but definitely possible situation that we pass it a very large string (in the order of ~1GB on a 32-bit Python install), one can reliably get heap corruption. It is possible to access this function (and condition in line(1)) through function parsestr from ast.c, when the file encoding of an input .py file is something apart from utf-8 and iso-8859-1. This can be trivially done using the following at the start of the file:
```
    # -*- coding: us-ascii -*-
```

The attached file (poc-gen.py) produces a poc.py file which satisfies these constraints and shows the vulnerability.

Note: To see the vulnerability in action, it is necessary to have an ASAN build of Python, compiled for 32 bit on a 64 bit machine. Additionally, the poc.py file generated can take an extremely long time to load (over a few hours), and finally crash. Instead, if one wishes to see the proof of vulnerability quicker, then it might be better to change the constant 4 in line (1) to 65536 (just for simplicity sake), and change the multiplication_constant in poc-gen.py file to be the same (i.e. 65536).

Proposed fix: Confirm that the multiplication will not overflow, before actually performing the multiplication and depending on the result.

---

https://github.com/python/cpython/pull/2174

```
diff --git a/Objects/stringobject.c b/Objects/stringobject.c
index c78e193..59d22e7 100644
--- a/Objects/stringobject.c
+++ b/Objects/stringobject.c
@@ -612,7 +612,13 @@ PyObject *PyString_DecodeEscape(const char *s,
     char *p, *buf;
     const char *end;
     PyObject *v;
-    Py_ssize_t newlen = recode_encoding ? 4*len:len;
+    Py_ssize_t newlen;
+    /* Check for integer overflow */
+    if (recode_encoding && (len > PY_SSIZE_T_MAX / 4)) {
+        PyErr_SetString(PyExc_OverflowError, "string is too large");
+        return NULL;
+    }
+    newlen = recode_encoding ? 4*len:len;
     v = PyString_FromStringAndSize((char *)NULL, newlen);
     if (v == NULL)
         return NULL;
```

## Attachments
- poc-gen.py
