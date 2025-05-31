# Possible Sensitive Session Information Leak in Active Storage

## Report Details
- **Report ID**: 3082917
- **URL**: https://hackerone.com/reports/3082917
- **State**: Closed
- **Severity**: high
- **Submitted**: 2025-04-08T13:37:49.305Z
- **Disclosed**: 2025-04-27T22:55:36.012Z

## Reporter
- **Username**: tyage
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Original report: https://hackerone.com/reports/2140554
Advisory: https://github.com/rails/rails/security/advisories/GHSA-8h22-8cf7-hq6g

## Impact

Active Storage, when serving files (blobs), incorrectly sends the Set-Cookie header containing the user's session cookie along with a Cache-Control: public header.
Some certain caching proxies may cache this response, including the Set-Cookie header.
This allows unrelated users accessing the cached content to obtain the original user's session cookie.

## Attachments
No attachments
