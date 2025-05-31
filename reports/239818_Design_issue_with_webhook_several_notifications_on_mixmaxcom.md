# Design issue with webhook (several) notifications on mixmax.com

## Report Details
- **Report ID**: 239818
- **URL**: https://hackerone.com/reports/239818
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-06-14T12:51:58.622Z
- **Disclosed**: 2017-06-23T20:39:07.171Z

## Reporter
- **Username**: be6bfca755e616cb69c1a51
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mixmax

## Vulnerability Information

Hi team,

I noticed a design problem involving successive notifications about an incorrect webhook set at https://app.mixmax.com/dashboard/settings/rules

I set an incorrect webhook (for testing) on this page and in a few hours I received more than 10 notifications.

This can cause a certain inconvenience to users due to the amount of emails sent by support@mixmax.com

{F194169}

## Attachments
- mixmax.png
