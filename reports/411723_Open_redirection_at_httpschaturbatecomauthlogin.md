# Open redirection at https://chaturbate.com/auth/login/

## Report Details
- **Report ID**: 411723
- **URL**: https://hackerone.com/reports/411723
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-09-20T10:33:20.219Z
- **Disclosed**: 2018-10-22T01:50:43.336Z

## Reporter
- **Username**: shailesh4594
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: chaturbate

## Vulnerability Information
Hi,

##Summary##
An attacker can redirect vicitm on an external website using https://chaturbate.com/auth/login/ endpoint because `next` parameter is not being validated properly. There is a protection existed but it's weak and can be bypassed.

`http` keyword is detected and protection works if payload contains `http` at beginning but that check can be bypassed using `Http` keyword. Though, only numeric is allowed after `Http:` so we can use decimal form of external domain/IP-address. In PoC, `3627732462` is decimal form of IP address of google.com.

## Steps To Reproduce:

  1. Open https://chaturbate.com/auth/login/?next=Http:3627732462
  1. Get logged in
  1. You will be redirected on https://google.com instead of a chaturbate website
  1. Done

###Suggested Fix:
Use more strong regular expression at this endpoint.

## Impact

- Simplifies phishing attacks
- Reflected File Download

## Attachments
No attachments
