# Session Replay Attack Allows Authentication Bypass via Captured Login Responses Allowing Bypass of 429 Too many attempts for Multiple Failed Logins

## Report Details
- **Report ID**: 3120790
- **URL**: https://hackerone.com/reports/3120790
- **State**: Closed
- **Severity**: high
- **Submitted**: 2025-05-01T00:05:53.247Z
- **Disclosed**: 2025-05-01T19:33:10.423Z

## Reporter
- **Username**: ctrl_cipher
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
#Summary
An attacker can bypass authentication by capturing a valid login response (including session cookies/tokens) and replaying it during a failed login attempt with incorrect credentials. The server fails to invalidate or validate session tokens properly, allowing unauthorized access even after logout.

#Steps to Reproduce
1. Legitimate Login:
Send a valid login request (correct email/password).
Capture the response using Burp Suite and copy it.

2. Invalid Login:
Log out the user.
Send a new login request with an incorrect password.
Replace the 400 Bad Request response with the previously captured legitimate login response (including the valid session cookie).

3. Result:
The server grants access to the account despite the wrong password.
The attacker can now interact with the account as the legitimate user.

#Recommendations
Server-Side Session Invalidation:
Maintain a database of active sessions and revoke old tokens on logout or failed login attempts.

Token Binding:
Bind session tokens to user context (e.g., IP address, user agent hash).

Short-Lived Tokens:
Use JWT with short expiration times (e.g., 15 minutes) and refresh tokens.

Replay Attack Mitigation:
Add a unique nonce or timestamp to each login request.

Secure Cookie Attributes:
Ensure cookies include Secure, HttpOnly, SameSite=Strict, and Max-Age

## Impact

Unauthorized Account Access: Attackers can compromise any account by replaying captured session tokens.
Persistence: Old tokens remain valid indefinitely.
Data Theft/Abuse: Sensitive user data (coding activity, API keys, etc.) can be stolen or modified.

## Attachments
- 1.jpg
- 2.jpg
- 4.jpg
- 5.jpg
