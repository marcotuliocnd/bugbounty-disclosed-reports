# 2FA Bypass via Leaked Cookies

## Report Details
- **Report ID**: 2479622
- **URL**: https://hackerone.com/reports/2479622
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-04-26T04:32:34.283Z
- **Disclosed**: 2024-07-11T15:14:40.892Z

## Reporter
- **Username**: deepmarketer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
The discovered vulnerability allows for the bypass of Two-Factor Authentication (2FA) mechanisms through the exploitation of leaked cookies. By intercepting and utilizing these cookies, an attacker can gain unauthorized access to user accounts without the need for the second authentication factor, compromising the security of the system.

**Description:**
The discovered vulnerability allows attackers to bypass Two-Factor Authentication (2FA) mechanisms by exploiting leaked cookies, compromising the security of user accounts within the hackerone. Two-Factor Authentication is a widely adopted security measure that adds an additional layer of protection beyond passwords, typically requiring users to provide a secondary authentication factor such as a code generated by an authenticator app . The vulnerability described herein enables attackers to bypass this additional security layer through the interception and utilization of session cookies, thus gaining unauthorized access to user accounts without the need for the secondary authentication factor.

## Steps To Reproduce

1. Navigate to the account settings and enable 2FA.

2. Log out and log back in using valid credentials.

3. Enter the required 2FA code to proceed.

4.Export session cookies using a cookie editor tool.

5.Paste the copied cookies into another browser

6 Access the account  without providing the 2FA code,2FA Authentication bypassed.

### Mitigation:
 Introduce device-based Two-Factor Authentication (2FA) mechanisms that require additional verification steps when signing in from new or unrecognized devices, browsers, or locations. This adds an extra layer of security by verifying the identity of the user and the device being used for authentication.

### Supporting Material/References 
POC Attached

## Impact

The vulnerability allows attackers to bypass Two-Factor Authentication (2FA) mechanisms by stealing and utilizing session cookies obtained through various means, such as man-in-the-middle (MitM) attacks using tools like Evilginx2. By exploiting this vulnerability, attackers can gain unauthorized access to user accounts without the need for the second authentication factor, compromising the security of the system and potentially leading to unauthorized data access, fraudulent transactions, or other malicious activities.

## Attachments
No attachments
