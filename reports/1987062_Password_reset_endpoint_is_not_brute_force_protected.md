# Password reset endpoint is not brute force protected

## Report Details
- **Report ID**: 1987062
- **URL**: https://hackerone.com/reports/1987062
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-05-13T19:17:02.646Z
- **Disclosed**: 2023-07-21T06:14:00.426Z

## Reporter
- **Username**: rullzer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Oversight of https://github.com/nextcloud/security-advisories/security/advisories/GHSA-v243-x6jc-42mp (https://hackerone.com/reports/1841665, but I can't judge the content there as it is not yet public).

In any case. The whole lostpassword flow is now annotated with bruteforce protection. Except the endpoint that actually matters. https://github.com/nextcloud/server/blob/master/core/Controller/LostController.php#L226-L229

An attacker can still happily try to brute force the token. Without getting throttled.

## Impact

The lostpassword flow is without actual bruteforce protection.

## Attachments
No attachments
