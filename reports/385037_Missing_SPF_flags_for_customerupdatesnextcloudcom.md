# Missing SPF flags for customerupdates.nextcloud.com

## Report Details
- **Report ID**: 385037
- **URL**: https://hackerone.com/reports/385037
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-07-21T20:20:57.651Z
- **Disclosed**: 2020-03-01T13:56:05.848Z

## Reporter
- **Username**: alpertecimer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hey,

I just checked for SPF records for the customerupdates.nextcloud.com domain, and there are none. The fake message reaches the inbox from this domain. Not spam.

 You can validate by testing yourself here: http://www.kitterman.com/spf/validate.html

This subdomain too: update.nextcloud.com

## Impact

Attacker could send fake email.

## Attachments
No attachments
