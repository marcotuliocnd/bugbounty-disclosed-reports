# TOTP Authenticator implementation Accepts Expired Codes

## Report Details
- **Report ID**: 2588810
- **URL**: https://hackerone.com/reports/2588810
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-07-07T19:01:24.901Z
- **Disclosed**: 2024-07-11T14:27:56.641Z

## Reporter
- **Username**: noob_but_cut3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Hi,

During testing hackerone.com, I discovered that the TOTP authenticator implementation accepts expired codes, allowing attackers to bypass authentication. This is a security vulnerability that reduces the effectiveness of the TOTP authentication mechanism.


**Description:**

TOTP (Time-Based One-Time Password) is a widely used authentication mechanism that generates a new password every 30 seconds. The password is valid for a short period, typically 30 seconds, before a new password is generated. This mechanism is designed to prevent attackers from using previously generated passwords.

During testing, I discovered that the TOTP authenticator implementation accepts expired codes, allowing attackers to bypass authentication. Specifically, I found that the authenticator accepts codes that are more than 1 minute old, which is considered a large window of acceptance.
This vulnerability reduces the security benefits of TOTP, allowing attackers to reuse expired codes. This can lead to unauthorized access to the system, which can result in data breaches, financial losses, and reputational damage.

### Steps To Reproduce

1. Enable TOTP authentication for the account at hackerone.com with google authenticator.
1. Log in to the tfa enabled account with correct password.
1. When it comes to tfa state, save the current totp code from authenticator app.
1. Wait for the code to expire (e.g., 1 minute).
1. Submit the expired code to the authentication endpoint.
1. Observe that the authentication is successful despite using an expired code.

### Suggest Fix 

1. Reduce the window of acceptance to a more secure value (e.g., 30 seconds).
1. Implement a more robust TOTP algorithm that rejects expired codes.

### Optional: Supporting Material/References (Screenshots)

 I have attached a POC video via google drive link cause it is over 250 mb.

https://drive.google.com/file/d/1onGsQvF-mmPXisjmxhkBbQUB4sbvoXz5/view?usp=sharing

## Impact

The attacker can bypass the two factor authentication by using expired otp code.

## Attachments
No attachments
