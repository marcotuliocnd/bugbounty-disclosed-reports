# Cross-site scripting on dashboard2.omise.co

## Report Details
- **Report ID**: 1532858
- **URL**: https://hackerone.com/reports/1532858
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-04-06T21:18:50.626Z
- **Disclosed**: 2022-05-24T11:54:30.797Z

## Reporter
- **Username**: oblivionlight
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: omise

## Vulnerability Information
## Summary:
Cross-site scripting (XSS) is an attack vector that injects malicious code into a vulnerable web application.
Stored XSS, also known as persistent XSS, is the more damaging of the two. It occurs when a malicious script is injected directly into a vulnerable web application.

Steps To Reproduce:
1. Log in to your account.
2. Visit https://dashboard.omise.co/test/settings 
3. Under Export - Specify the metadata that you want to include in your export option. Enter <script>alert(2)</script> in all four parameters including Charge, Transfer, Refund, Dispute.
4. Click on Update settings.
5. Click on Try our new dashboard, XSS will Trigger or log out and log in again, and XSS will Trigger.

POC:
Attached Video.

## Impact

Code injected into a vulnerable application can exfiltrate data or install malware on the user's machine. Attackers can masquerade as authorized users via session cookies, allowing them to perform any action allowed by the user account.

## Attachments
No attachments
