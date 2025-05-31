# No Rate Limitation on Regenerate Api Key

## Report Details
- **Report ID**: 243619
- **URL**: https://hackerone.com/reports/243619
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-06-27T13:00:15.458Z
- **Disclosed**: 2017-08-21T17:41:05.953Z

## Reporter
- **Username**: footstep
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi,

I discovered that there is no request throttling or limit on api key regeneration. Though theres a little change while making a total of 30 requests in a few seconds, server error occurred then it continued.

##Screenshot
{F197872}

In the screenshot `685` denotes a processed request and `6052` denotes an error: on the server.

Shuaib

## Attachments
- Screen_Shot_2017-06-27_at_1.57.55_PM.png
