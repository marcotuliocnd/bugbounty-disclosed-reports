# Improper email address verifiation while saving Account Details

## Report Details
- **Report ID**: 825646
- **URL**: https://hackerone.com/reports/825646
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-03-20T20:22:07.550Z
- **Disclosed**: 2020-03-23T08:31:07.262Z

## Reporter
- **Username**: harshitshah4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stagingdoteverydotorg

## Vulnerability Information
## Summary:
Attacker could be able change its email to any email address even already created another user's email address.(Even though UI doesnot allow it)
## Steps To Reproduce:

  0. Set up proxy.
  1. Singup with any email address
  2. Go to profile section 
  3. Click on update button
  4. Monitor call in reverse proxy and change email field to any user's email address
 5. Done! Attacker is able to change its email address to any email address even registered one's

## Supporting Material/References:
https://hackerone.com/reports/30975
[list any additional material (e.g. screenshots, logs, etc.)]

## Impact

Attacker might be able to impersonate as any other user

## Attachments
No attachments
