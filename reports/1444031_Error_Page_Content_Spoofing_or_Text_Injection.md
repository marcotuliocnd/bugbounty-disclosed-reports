# Error Page Content Spoofing or Text Injection

## Report Details
- **Report ID**: 1444031
- **URL**: https://hackerone.com/reports/1444031
- **State**: Closed
- **Severity**: none
- **Submitted**: 2022-01-08T14:59:59.320Z
- **Disclosed**: 2022-03-09T17:57:06.190Z

## Reporter
- **Username**: mrirfan___07
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: krisp

## Vulnerability Information
## Summary:

Error Page Content Spoofing or Text Injection in two urls

Target: https://download.prelive.krisp.ai/
Target:https://upld.prelive.krisp.ai/


Description: Content spoofing, also referred to as content injection, "arbitrary text injection" or virtual defacement, is an attack targeting a user made possible by an injection vulnerability in a web application. When an application does not properly handle user-supplied data, an attacker can supply content to a web application, typically via a paramete value, that is reflected back to the user. This presents the user with a modified page under the context of the trusted domain.

Steps to Reproduce:

1.Go to https://download.prelive.krisp.ai/  and this url :https://upld.prelive.krisp.ai/
2.Type any thing after slash, it will be reflected on the page.

Reference: 
https://hackerone.com/reports/498562
https://hackerone.com/reports/1245051
https://hackerone.com/reports/327671

## Impact

This attack is typically used as, or in conjunction with, social engineering because the attack is exploiting a code-based vulnerability and a user's trust. As a side note, this attack is widely misunderstood as a kind of bug that brings no impact.

poc:

## Attachments
- Screenshot_(289).png
- Screenshot_(290).png
