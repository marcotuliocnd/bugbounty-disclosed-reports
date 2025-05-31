# Potential invocation of qsort on uninitialized memory during cookie save

## Report Details
- **Report ID**: 696822
- **URL**: https://hackerone.com/reports/696822
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-09-18T01:52:21.989Z
- **Disclosed**: 2021-02-08T07:54:36.887Z

## Reporter
- **Username**: pauldreik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
If cookiejar is set, cookies are written to file at exit. That is done by the function cookie_output() in cookie.c. The cookies are sorted before being stored, using qsort on a temporary array. That temporary array is uninitialized (gotten from malloc at https://github.com/curl/curl/blob/7c596f5dea586c1ba99dfbe7f3ce1996d82f7de0/lib/cookie.c#L1534 ). This would not be a problem unless there also is a bug in the range given to qsort 
https://github.com/curl/curl/blob/7c596f5dea586c1ba99dfbe7f3ce1996d82f7de0/lib/cookie.c#L1550
which is numcookies. However, it should be j which is used for counting at https://github.com/curl/curl/blob/7c596f5dea586c1ba99dfbe7f3ce1996d82f7de0/lib/cookie.c#L1546.

The buffer passed to qsort is partially filled with cookie data, and the rest is uninitialized. When qsort sorts, it will dereference the supposed to be pointers to compare the elements and depending on the results jump around reading in memory.

## Steps To Reproduce:
I found this through fuzzing and I do not want to make that public until the problems I find are fixed - in case you want it now already, just hit me up. I attached the most important part of the fuzzer.


It is not obvious how to reproduce without the fuzzer: (c->numcookies must be nonzero and co->domain must not be set on at least one of them for this bug to be triggered. Perhaps by loading an evil cookie file from disk.

To detect it, address and undefined sanitizers are not sufficient. That is likely because qsort is a library function, so it's not instrumented. Valgrind does not always catch it either. I found it by adding an assert on pointer alignment inside the cookie_sort_ct(), and eventually found which of the 60000 test cases I had caused it.

## Suggested fix
```
diff --git a/lib/cookie.c b/lib/cookie.c
index 53ca40237..875569bb0 100644
--- a/lib/cookie.c
+++ b/lib/cookie.c
@@ -1547,7 +1547,7 @@ static int cookie_output(struct CookieInfo *c, const char *dumphere)
       }
     }
 
-    qsort(array, c->numcookies, sizeof(struct Cookie *), cookie_sort_ct);
+    qsort(array, j, sizeof(struct Cookie *), cookie_sort_ct);
 
     for(i = 0; i < j; i++) {
       char *format_ptr = get_netscape_format(array[i]);

```

Even better (defence in depth) would be to allocate array with calloc instead of malloc which would cause (near null) pointer dereference instead of "random" values.

## Supporting Material/References:
Attached is
  - the test case to feed as input to the fuzzer above.
  - crash report from valgrind and assert()

## Impact

This is read access, and if triggered it will perhaps cause a crash (segmentation fault), and the cookie jar is not written. So a fairly benign bug.

## Attachments
- aadaae36b4be454366dff6257c995dfa18f8d539
- README.txt
- fuzz_cookies.cc
