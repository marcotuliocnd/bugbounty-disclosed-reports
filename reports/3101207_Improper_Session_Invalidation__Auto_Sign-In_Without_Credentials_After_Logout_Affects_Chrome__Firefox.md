# Improper Session Invalidation – Auto Sign-In Without Credentials After Logout (Affects Chrome & Firefox)

## Report Details
- **Report ID**: 3101207
- **URL**: https://hackerone.com/reports/3101207
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2025-04-19T23:18:32.094Z
- **Disclosed**: 2025-04-29T14:09:13.683Z

## Reporter
- **Username**: pent0ss
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: dust

## Vulnerability Information
## Summary:
When a user logs out, the session is not invalidated properly. Revisiting the login page allows automatic re-authentication without any user input. This means the session remains active or is being improperly restored.

Tested on:
- Google Chrome 
- Mozilla Firefox

Behavior is consistent across multiple browsers

## Steps To Reproduce:

1. Log in to the web application with a valid account.
2. Click on the "Logout" button.
3. Stay in the same browser, or open a new tab with the site.
4. Click on “Sign In” or visit the login page.

### Observe: User is automatically signed back in without entering email/password

## Expected Behavior:

- On logout, all session tokens should be invalidated both client and server-side.

- Revisiting the login page must not restore access without re-authentication

## Recommendation:

- Properly invalidate the session on the server.
- Remove all tokens/cookies from the browser.
- Set cache-control headers to prevent session restoration via back/forward navigation.
- Consider revoking refresh tokens where applicable

## Impact

- Logout becomes meaningless, giving a false sense of security.
- If someone else gains temporary or physical access to the browser, they can easily regain access to the account without credentials.
- Risk is amplified in environments like internet cafés, libraries, or if a device is lost/stolen.

## Attachments
- Insufficient_Session_Expiration.mkv
