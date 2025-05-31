# The Linux binaries (nordvpn and nordvpnd) don't use PIE/ASLR

## Report Details
- **Report ID**: 817244
- **URL**: https://hackerone.com/reports/817244
- **State**: Closed
- **Severity**: none
- **Submitted**: 2020-03-12T00:38:19.028Z
- **Disclosed**: 2020-04-22T11:29:59.782Z

## Reporter
- **Username**: skyplabs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nordsecurity

## Vulnerability Information
## Summary:

The Linux binaries `nordvpn` and `nordvpnd` don't have PIE/ASLR enabled. A such feature is used to harden programs against the exploitation of memory corruption bugs and should be enabled.

The use of ASLR has long been debated among the Golang community. However, it seems that it's becoming the default choice now.

## Steps To Reproduce:

```
$ rabin2 -I /usr/bin/nordvpn | grep pic
pic      false
$ rabin2 -I /usr/sbin/nordvpnd | grep pic
pic      false
```

## Supporting Material/References:

  * https://insanitybit.github.io/2016/12/28/golang-and-rustlang-memory-safety
  * https://github.com/golang/go/issues/35192
  * https://fedoraproject.org/wiki/Changes/golang-buildmode-pie

## Impact

Any memory corruption bug (e.g. buffer overflow) can easily lead to a working exploit when ASLR is not enabled.

## Attachments
No attachments
