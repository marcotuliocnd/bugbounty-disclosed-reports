# Insecure loading of ICU data through ICU_DATA environment variable

## Report Details
- **Report ID**: 1625036
- **URL**: https://hackerone.com/reports/1625036
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-07-04T22:28:55.668Z
- **Disclosed**: 2023-03-19T17:10:01.903Z

## Reporter
- **Username**: bnoordhuis
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
Node.js correctly ignores the NODE_ICU_DATA environment variable when it is running with elevated privileges (e.g. setuid root).

ICU on the other hand still honors the ICU_DATA environment variable, without regard for privilege level.

## Impact

ICU is not very resilient to crafted data files but since users can select custom data files anyway with the `--icu-data-dir` flag, the real-world impact is probably not much worse than what is already possible through documented means...

...which doesn't mean it shouldn't be fixed because scenarios where it is in fact exploitable are imaginable, just not very likely.

Suggestions:

- build ICU with ICU_NO_USER_DATA_OVERRIDE defined
- sanitize the environment before initializing ICU

## Attachments
No attachments
