# Stored XSS in "Create Groups"

## Report Details
- **Report ID**: 647130
- **URL**: https://hackerone.com/reports/647130
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-07-17T06:17:40.240Z
- **Disclosed**: 2020-08-26T14:15:21.414Z

## Reporter
- **Username**: rioncool22
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the (parenthesized) sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

### Summary

Stored attacks are those where the injected script is permanently stored on the target servers, such as in a database, in a message forum, visitor log, comment field, etc. The victim then retrieves the malicious script from the server when it requests the stored information. Stored XSS is also sometimes referred to as Persistent or Type-I XSS. 

### Steps to reproduce

1. Login to [Gitlab](https://gitlab.com)
2. Create a new group with xss payload
payload i use = "><img src=x onerror=prompt(123)>
3. Open Group
4. To trigger XSS you can click "NEW PROJECT"
5. XSS Trigger

## Impact

Can steal Cookie, Can run javascript code, etc

## Attachments
- Screenshot_from_2019-07-17_02-06-52.png
