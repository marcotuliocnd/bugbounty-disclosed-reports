# Error Page Content Spoofing or Text Injection 

## Report Details
- **Report ID**: 1245051
- **URL**: https://hackerone.com/reports/1245051
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-06-26T11:38:32.332Z
- **Disclosed**: 2021-07-14T12:21:01.122Z

## Reporter
- **Username**: princej_76
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: basecamp

## Vulnerability Information
Target:  https://gopher.hey.com/

Description:  Content spoofing, also referred to as content injection, "arbitrary text injection" or virtual defacement, is an attack targeting a user made possible by an injection vulnerability in a web application. When an application does not properly handle user-supplied data, an attacker can supply content to a web application, typically via a parameter value, that is reflected back to the user. This presents the user with a modified page under the context of the trusted domain.


Steps to Reproduce:
1. Go to https://gopher.hey.com/
2.  Type any thing after slash, it will be reflected on the page.

Reference: https://hackerone.com/reports/498562
                           https://hackerone.com/reports/327671

## Impact

This attack is typically used as, or in conjunction with, social engineering because the attack is exploiting a code-based vulnerability and a user's trust. As a side note, this attack is widely misunderstood as a kind of bug that brings no impact.

## Attachments
- Screenshot_from_2021-06-26_16-56-41.png
- Screenshot_from_2021-06-26_16-56-07.png
