# Stored Cross-site Scripting on devicelock.com/forum/

## Report Details
- **Report ID**: 1122513
- **URL**: https://hackerone.com/reports/1122513
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-03-10T18:04:32.523Z
- **Disclosed**: 2022-02-08T10:49:21.823Z

## Reporter
- **Username**: h4x0r_dz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary

Hello, @acronis Team I hope you all doing well.

I just found A Stored Cross-site Scripting on devicelock.com/forum/ by changing the ***City*** value on https://www.devicelock.com/bitrix/admin/user_edit.php? to HTML/javascript code and lead to Stored Cross-site Scripting.


  1. go to https://www.devicelock.com/forum/view_profile.php?register=yes  and create a new account 
  1. go to https://www.devicelock.com/bitrix/admin/user_edit.php? and click on **Personal information** and in `City` input put and xss payload like: `<img src=x onerror=alert(document.cookie)>` and click on apply.
  1. Go to https://www.devicelock.com/forum/view_profile.php?UID=<your_user_id> and change `<your_user_id>` to your id 

## POC
https://www.devicelock.com/forum/view_profile.php?UID=28349

{F1225664}

## Impact

Stored XSS.

## Attachments
- 2021-03-10_18-58-16.mp4
