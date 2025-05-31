# XSS (stored) Wizard is saving executable code

## Report Details
- **Report ID**: 384517
- **URL**: https://hackerone.com/reports/384517
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-07-20T11:20:42.267Z
- **Disclosed**: 2018-09-27T12:46:09.463Z

## Reporter
- **Username**: nitin_24
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
issue: xss(stored)
Stored XSS occurs when a web application gathers input from a user which might be malicious, and then stores that input in a data store for later use. The stored input is not correctly filtered. As a consequence, the malicious data will appear to be part of the web site and run within the user’s browser under the privileges of the web application.

poc:
url: https://imgsrcxonerrorprompt2.rocket.chat

## Impact

Attackers can execute scripts in a victim’s browser to hijack user sessions, deface web sites, insert hostile content, redirect users, hijack the user’s browser using malware, etc.

## Attachments
- Screenshot_(143).png
- Screenshot_(144).png
- Screenshot_(145)_(1).png
