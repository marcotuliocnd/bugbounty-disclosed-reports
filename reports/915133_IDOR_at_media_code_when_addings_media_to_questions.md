# IDOR at 'media_code' when addings media to questions

## Report Details
- **Report ID**: 915133
- **URL**: https://hackerone.com/reports/915133
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-07-04T03:53:42.237Z
- **Disclosed**: 2020-11-18T14:22:27.150Z

## Reporter
- **Username**: bugra
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
Hi team,
When you add a question to your survey and click `Save`, it sends this request :
{F893416}

In this request, `media_code` is vulnerable for IDOR. If you change it to any media ID, you will see it on your question. 
And these IDs are sequential. So you can access to any user's media contents. 

## Steps To Reproduce:

  1. Create a survey
  1. Add any question like `Free Text` and open your proxy program
  1. Click to question and click `Save` 
  1. Your proxy program will catch the request
  1. Change the `media_code` parameter's value to a 7 digit number. Like `2013124` (my media content)
  1. Send the request, you will see the victim's media.

## Impact

Access to user's media contents

Thanks,
Bugra

## Attachments
- request.PNG
