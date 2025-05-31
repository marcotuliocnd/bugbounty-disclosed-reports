# Use-After-Free In IPV6_2292PKTOPTIONS leading To Arbitrary Kernel R/W Primitives

## Report Details
- **Report ID**: 826026
- **URL**: https://hackerone.com/reports/826026
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-03-21T16:40:38.626Z
- **Disclosed**: 2020-07-06T19:12:54.099Z

## Reporter
- **Username**: theflow0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: playstation

## Vulnerability Information
## Summary

Due to missing locks in option `IPV6_2292PKTOPTIONS` of `setsockopt` , it is possible to race and free the `struct ip6_pktopts ` buffer, while it is being handled by `ip6_setpktopt`. This structure contains pointers (`ip6po_pktinfo`) that can be hijacked to obtain arbitrary kernel R/W primitives. As a consequence, it is easy to have kernel code execution. This vulnerability is reachable from WebKit sandbox and is available in the latest FW, that is 7.02.

## Attachment

Attached is a Proof-Of-Concept that achieves a Local Privilege Escalation on FreeBSD 9 and FreeBSD 12.

## Impact

- In conjunction with a WebKit exploit, a fully chained remote attack can be achieved.
- It is possible to steal/manipulate user data.
- Dump and run pirated games.

## Attachments
- exploit.c
