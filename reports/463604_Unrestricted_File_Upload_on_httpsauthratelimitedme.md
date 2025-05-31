# Unrestricted File Upload on https://auth.ratelimited.me

## Report Details
- **Report ID**: 463604
- **URL**: https://hackerone.com/reports/463604
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-12-17T01:13:14.056Z
- **Disclosed**: 2019-05-18T15:27:21.078Z

## Reporter
- **Username**: daniel_v
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ratelimited

## Vulnerability Information
Hello security team,

Have found a way to upload files that aren't images on https://auth.ratelimited.me/

Steps to reproduce:

1. Login at https://auth.ratelimited.me/
2. Click "change photo" and intercept with a tool (used burpsuite)
3. Choose "gravatar" option and change the 'url' parameter to anything you would like
4. Done
Ps: The same occurs when you intercept "no photo" option

Ps2: I could not execute code through this, but i thought it was a valid report because i tried to upload .txt files in "upload photo" options and it was not allowed.

If you need further information, please contact me
Best Regards,
Daniel

## Impact

possibility of uploading anything rather than images

## Attachments
- uploading_url.PNG
