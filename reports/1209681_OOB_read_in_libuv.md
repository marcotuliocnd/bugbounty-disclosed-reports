# OOB read in libuv

## Report Details
- **Report ID**: 1209681
- **URL**: https://hackerone.com/reports/1209681
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-05-26T06:22:37.526Z
- **Disclosed**: 2021-07-05T08:30:01.209Z

## Reporter
- **Username**: ericsesterhenn
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:** 

The pointer p is read and increased without checking whether it is beyond pe, with the latter holding a pointer to the end of the buffer. This can lead to information disclosures or crashes. This function can be triggered via uv_getaddrinfo().  nodejs seems to use libuv and is possibly affected by this as well.

**Description:**
An out-of-bound read can occur when uv__idna_toascii() is used to convert strings to ASCII. The pointer p is read and increased without checking whether it is beyond pe, with the latter holding a pointer to the end of the buffer. This can lead to information disclosures or crashes. This function can be triggered via uv_getaddrinfo().  nodejs seems to use libuv and is possibly affected by this as well.

## Steps To Reproduce:

i attached a testcase and the ad-hoc fuzzer I used to identify the issues. If you need further help reproducing, please let me know.

~~~
static unsigned uv__utf8_decode1_slow(const char** p,
                                      const char* pe,
                                      unsigned a) {
  unsigned b;
  unsigned c;
  unsigned d;
  unsigned min;

  if (a > 0xF7)
    return -1;

  switch (*p - pe) {
  default:
    if (a > 0xEF) {
      if (p + 3 > pe)
        return -1;
      min = 0x10000;
      a = a & 7;
      b = (unsigned char) *(*p)++;   // OOB READ
      c = (unsigned char) *(*p)++;   // OOB READ
      d = (unsigned char) *(*p)++;   // OOB READ
      break;
    }
    /* Fall through. */
~~~



## Impact: [add why this issue matters]

Possiblity to crash the process when untrusted hostnames are passed to uv__getaddrinfo()

## Supporting Material/References:

-

## Misc

This issue was found during an audit of Cure53 for ExpressVPN but ExpressVPN is not affected by the issue. I reported it to the libuv project, whose maintainers suggested that i report it to nodejs directly as well.

## Impact

An oob read that does not seem to be abused to leak data, but possibly read to a guarded page which segfaults the process.

## Attachments
- desc.txt
- fuzz.tar.bz2
- testcase_oob_read
