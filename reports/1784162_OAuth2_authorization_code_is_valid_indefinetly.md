# OAuth2 "authorization_code" is valid indefinetly

## Report Details
- **Report ID**: 1784162
- **URL**: https://hackerone.com/reports/1784162
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-11-25T11:50:10.544Z
- **Disclosed**: 2024-02-17T08:39:14.500Z

## Reporter
- **Username**: mikaelgundersen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Your OAuth2 endpoint is not at all following best practices. When the authorization_code is generated it is stored without a timeout. Now according to https://www.rfc-editor.org/rfc/rfc6749#section-4.1.2 10 minutes is recommended. As the goal is that is gets used almost directly or not at all.

Now there is a debate maybe to have on the 10 minutes. But there is kind of a big difference between 10 minutes and no timeout at all.

## Impact

An attacker that obtains this code could possibly easily redeem it in the future.
Or an attacker could just keep trying codes.

## Attachments
No attachments
