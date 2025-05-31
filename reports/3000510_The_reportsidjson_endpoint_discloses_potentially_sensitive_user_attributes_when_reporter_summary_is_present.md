# The /reports/:id.json endpoint discloses potentially sensitive user attributes when reporter summary is present

## Report Details
- **Report ID**: 3000510
- **URL**: https://hackerone.com/reports/3000510
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2025-02-19T10:52:13.074Z
- **Disclosed**: 2025-04-01T18:23:00.654Z

## Reporter
- **Username**: avinash_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi

The.json endpoint of any disclosed report is leaking reporter's email, OTP backup codes, reporter's phone number, "graphql_secret_token", tshirt size all the reporter account's internal details etc. 

```
 GET /reports/█████.json HTTP/2
Host: hackerone.com
````

* I was checking Hackerone's disclosed report ██████████ and suddenly during check found .json point is leaking too much data of reporter ```████``` . I immediately reported it to you.

█████



* PoC:- Leakage of data of reporter

█████
█████





## Impact

Reporter H1 account private data disclosed

## Attachments
No attachments
