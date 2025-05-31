# No Password Length Restriction leads to Denial of Service

## Report Details
- **Report ID**: 1243009
- **URL**: https://hackerone.com/reports/1243009
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-06-24T12:42:31.911Z
- **Disclosed**: 2021-10-21T19:51:35.598Z

## Reporter
- **Username**: c_j_27
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
Hey when I try to set the password while creating account I noticed that you haven't kept any password limit.
You need to decrease password length :There are two reasons for limiting the password size. For one, hashing a large amount of data can cause significant resource consumption on behalf of the server and would be an easy target for Denial Of Service attack.
Normally all sites have a password minimum to maximum length like 72 characters limit or 48 limit to prevent Denial Of Service attack. But in your  registration page there are no limitation. Let me know if you need any more details.

This is typically not DoS, but a vulnerability which may lead to DoS attack.

The password I tried is:

Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40

## Impact

As the response is seen, the server might not be able to handle such lengthy passwords coming from different machines simultaneously. The attacker can perform a DDOS attack by using this vulnerability.

## Attachments
No attachments
