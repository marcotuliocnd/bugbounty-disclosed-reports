# Information Disclosure Due To exposed .env file (Directory Listing) at ████████

## Report Details
- **Report ID**: 2784712
- **URL**: https://hackerone.com/reports/2784712
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-10-16T14:44:33.783Z
- **Disclosed**: 2024-10-22T13:35:45.070Z

## Reporter
- **Username**: necr0mancer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: aws_vdp

## Vulnerability Information
A .env file was discovered on the server at ████, exposing sensitive application configurations, including database credentials, email settings, and more. This information could allow an attacker to gain unauthorized access to critical systems and services.

**Steps to Reproduce:**

1. Open a web browser.
2. Navigate to ████████.
3. The .env file content is displayed, revealing sensitive information.

**PoC Video Link:** ██████

## Impact

The exposed .env file could lead to multiple security threats, including but not limited to:

Unauthorized database access using DB_HOST, DB_USERNAME, and DB_PASSWORD.
Compromise of email services via MAIL_USERNAME and MAIL_PASSWORD.
Ability to access or manipulate other connected services.

## Attachments
No attachments
