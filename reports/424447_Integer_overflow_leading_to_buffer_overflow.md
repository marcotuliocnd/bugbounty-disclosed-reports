# Integer overflow leading to buffer overflow

## Report Details
- **Report ID**: 424447
- **URL**: https://hackerone.com/reports/424447
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-10-15T23:30:09.941Z
- **Disclosed**: 2019-09-25T18:30:15.302Z

## Reporter
- **Username**: jkrshnmenon
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
There exists an integer overflow in Perl_my_setenv @ util.c : 2070

2070: void Perl_my_setenv(pTHX_ const char *nam, const char *val) {
...
2166:         const int nlen = strlen(nam);
...
2171:         vlen = strlen(val);
2172:         new_env = (char*)safesysmalloc((nlen + vlen + 2) * sizeof(char));

Here in a 64 bit version of Perl, since the arguments `nam` and `val` are user controlled, the 32 bit integers `nlen` and `vlen` are also under the control of the attacker. Therefore, if `nam` and `val` are two very long strings (for example, 2147483647 bytes long), the addition at line 2172 would result in an integer overflow.

The `new_env` would therefore be a chunk of a size which is smaller than the sum of the lengths of the two input strings.

This `new_env` is subsequently used in a call to `memcpy` to copy `nlen` bytes from `nam` followed by `vlen` bytes from `val`.

This results in a buffer overflow on the heap with attacker controlled input.

Please find attached a PoC which demonstrates the buffer overflow. Please note that the attached PoC consumes large amounts of memory and results in a segmentation fault on a 64 bit Ubuntu 16.04 system running a 64 bit version of perl.
This segmentation fault occurs due to the fact that the `memcpy` tries to write outside the initial heap boundary.

This vulnerability has been recognised as a serious security issue and has been assigned the identifier CVE-2018-18311 by the developers.

## Impact

Memory corruption with attacker controlled input which can lead to arbitrary code execution

## Attachments
- test.pl
