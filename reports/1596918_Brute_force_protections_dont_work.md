# Brute force protections don't work

## Report Details
- **Report ID**: 1596918
- **URL**: https://hackerone.com/reports/1596918
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-06-10T11:34:48.305Z
- **Disclosed**: 2022-09-03T06:25:26.022Z

## Reporter
- **Username**: nickvergessen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
Most of the brute force protections don't actually throttle() the response and so they are not logging negative attempts

Search for functions with the `@BruteForceProtection` annotation and check that they call `throttle()` on the response at least conditionally.

## Impact

Brute force protection is not throttling any requests:
https://github.com/nextcloud/server/blob/b70c6a128fe5d0053b7971881696eafce4cb7c26/lib/private/AppFramework/Middleware/Security/BruteForceMiddleware.php#L78-L82

## Attachments
No attachments
