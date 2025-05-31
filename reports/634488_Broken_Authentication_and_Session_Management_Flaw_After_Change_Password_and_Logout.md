# Broken Authentication and Session Management Flaw After Change Password and Logout

## Report Details
- **Report ID**: 634488
- **URL**: https://hackerone.com/reports/634488
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-07-03T15:24:20.575Z
- **Disclosed**: 2020-11-08T07:36:53.457Z

## Reporter
- **Username**: root_geek280
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: omise

## Vulnerability Information
####Summary
Usually it's happened that when you change password or sign out from one place (or one browser), automatically someone who is open same account will sign out too from another browser. Basically your session destroyed at server side...
But in your site, it still alive..

####PoC
Detail About Vulnerability and PoC on Attachment File

Noted: You can try these vulnerability in another site. (e.g cryptfolio.com, facebook.com, etc). It's not alive when another has changed password and sign out

For More Information about This Vulnerability You can check OWASP Guide

[https://www.owasp.org/index.php?title=Broken_Authentication_and_Session_Management&setlang=en](https://www.owasp.org/index.php?title=Broken_Authentication_and_Session_Management&setlang=en)

####Attachment Video
[https://gofile.io/?c=Vt4m42](https://gofile.io/?c=Vt4m42)

## Impact

Account profile still can be edited even in another browser the account has signedout and changed password

## Attachments
No attachments
