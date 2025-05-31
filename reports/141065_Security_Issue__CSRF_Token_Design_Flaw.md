# Security Issue : CSRF Token Design Flaw

## Report Details
- **Report ID**: 141065
- **URL**: https://hackerone.com/reports/141065
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-25T23:50:54.437Z
- **Disclosed**: 2016-07-30T23:44:29.036Z

## Reporter
- **Username**: ghumman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: drchrono

## Vulnerability Information
Introduction:

Hello I am Bruin, a security researcher and analyst. I have been able to identify a bypass in your CSRF protection mechanism, which upon a successful execution can result in a successful CSRF attack on a victim's account.

Description:

CSRF Token's are different from session ID'S in a way that they are not consistent in entire user session but drchrono.com do not practice the rotation of CSRF token's for every request in a session.

Reproduction Steps:

< Log in to drchrono.com
< go to settings
< go to profile
< click change password
< fill out the fields
< click save and intercept the request
< copy POST data
< repeat the process

--Observe that the CSRF token from both request's is same.

Impact:

It can be misused in multiple ways, some of the scenarios are listed below :

*An attacker capturing the CSRF token via cross site scripting can use it to plant a successful CSRF attack even if the session id is unusable.
*A network based attack can be used to capture and replay the token on to the victim's account.

Fix:

Rotate the token on each consecutive session.

Please let me know if any additional information is required . I shall be waiting for your reply.

Regards,
Bruin,
Security Researcher.

## Attachments
No attachments
