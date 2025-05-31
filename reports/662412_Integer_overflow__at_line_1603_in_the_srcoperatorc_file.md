# Integer overflow  at line 1603 in the src/operator.c file

## Report Details
- **Report ID**: 662412
- **URL**: https://hackerone.com/reports/662412
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-07-29T01:10:32.565Z
- **Disclosed**: 2021-02-08T07:55:42.258Z

## Reporter
- **Username**: cjun
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
[add summary of the vulnerability]
On systems with a 64 bit, if —retry-max-time > 18446744073709552, config->retry-max-time*1000L will be overflow  at line 1603 in the src/operator.c file. Similarly, the same is true for 32-bit operating systems.
## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. [add step]
run: curl --retry-max-time 18446744073709552 -v 127.0.0.1:8080/test.html
  1. [add step]
  1. [add step]

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

If the integer overflow is triggered, the parameter retry-max-time will be illegal.

## Attachments
No attachments
