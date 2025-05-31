# Session not expired on logout

## Report Details
- **Report ID**: 245124
- **URL**: https://hackerone.com/reports/245124
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-07-01T14:11:52.133Z
- **Disclosed**: 2017-07-03T17:36:26.480Z

## Reporter
- **Username**: ronygigi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
Description:
Session management issue in https://wakatime.com

Cookies are used to maintain session of the particular user and they should expire once the user logs out of his account.In secure web application,Cookies immediately expire once the user logs out of his account.
But this is not happening in the case of WakaTime, same cookies can be used again and again to open the session of the victim.
Browser Version:
Google Chrome Version 59.0.3071.115 
Extension Required:
Edit this cookie extension
Steps to reproduce the issue:
1) Create a WakaTime account and log in into the newly created account or you can use your existing account as well.
2) Copy the cookies  using "Export" option of the Edit this cookie extension
3) Now log out from your WakaTime account.
4) Now delete the existing cookies and paste the cookies after clicking "Import" option.Try to visit  https://wakatime.com/dashboard .
You can see that you gets logged in.The cookies are not getting expired once the user logs out of his account.
Impact:
If a malicious user gets the cookies by exploiting any vulnerability,he can log in to the victim's account.

Looking forward to hear from you.
Best Regards,
Rony Gigi



## Attachments
No attachments
