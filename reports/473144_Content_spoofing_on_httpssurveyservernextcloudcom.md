# Content spoofing on https://surveyserver.nextcloud.com

## Report Details
- **Report ID**: 473144
- **URL**: https://hackerone.com/reports/473144
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-12-29T14:54:19.769Z
- **Disclosed**: 2021-02-14T15:57:12.701Z

## Reporter
- **Username**: mik317
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi NextCloud team,
the `https://surveyserver.nextcloud.com` domain is vulnerable against `content spoofing` in the `forbidden page` due to the fact that the `request URI` is reflected without validation inside the aforementioned page.

1. Go on https://surveyserver.nextcloud.com/.htaccess%20because%20the%20webserver%20has%20been%20moved%20on%20http://evil.com%20and%20only%20an%20old%20version%20is%20present
2. Text injected successfully {F398692}

## Impact

Insert arbitrary text inside the `forbidden page` via `request URI`

## Attachments
- content.png
