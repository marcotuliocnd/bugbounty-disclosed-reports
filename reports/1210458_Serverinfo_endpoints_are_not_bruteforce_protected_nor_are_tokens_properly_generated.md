# Serverinfo endpoints are not bruteforce protected nor are tokens properly generated

## Report Details
- **Report ID**: 1210458
- **URL**: https://hackerone.com/reports/1210458
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-05-27T10:48:41.077Z
- **Disclosed**: 2021-06-16T08:39:22.233Z

## Reporter
- **Username**: rtod
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
The serverinfo app allows accessing the endpoints also via a custom token.

https://github.com/nextcloud/serverinfo/blob/9ae9dde028a684e53a1b37c9ba8e964ffe42a97f/lib/Controller/ApiController.php#L121

The token is set/generated via
https://github.com/nextcloud/serverinfo/blob/9ae9dde028a684e53a1b37c9ba8e964ffe42a97f/templates/settings-admin.php#L341

## Impact

There is no bruteforce protection on this endpoint in general. So a attacker can just fire off request. Combine this with that they have to generate a token on their own (which is usually a lot weaker) and in a lot of cases obtaining acccess should not be horribly hard.

I'd recommend

1. Add bruteforce protection to the endpoint
2. Have a button in the UI to generate a proper long random string

## Attachments
No attachments
