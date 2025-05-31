# Memcached used as RateLimiter backend is no-op

## Report Details
- **Report ID**: 2110945
- **URL**: https://hackerone.com/reports/2110945
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-08-15T16:38:48.103Z
- **Disclosed**: 2023-11-12T08:06:18.886Z

## Reporter
- **Username**: nickvergessen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
When Memcached is used as backend:
https://github.com/nextcloud/server/blob/c705b8fcb3de7910e67cd2ed2d2b38653f58962a/lib/private/Server.php#L787-L799

The following code block is problematic:
https://github.com/nextcloud/server/blob/90104bc1c448c6da2fd3e052fca75bb3fb261c87/lib/private/Memcache/Memcached.php#L135-L139

I guess we need to check the actual cache type and use the DB backend when Memcached is used?

## Impact

Any action that partly resets any cache entry will wipe rate limit attempts and future bruteforce protection (with https://github.com/nextcloud/server/pull/39870 )

## Attachments
No attachments
