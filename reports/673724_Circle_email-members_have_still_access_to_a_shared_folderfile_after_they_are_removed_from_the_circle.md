# Circle email-members have still access to a shared folder/file after they are removed from the circle

## Report Details
- **Report ID**: 673724
- **URL**: https://hackerone.com/reports/673724
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-08-14T15:46:23.970Z
- **Disclosed**: 2020-03-01T11:24:48.159Z

## Reporter
- **Username**: michag86
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
If a email-address is added to a circle, the email user has still access after the email-address is removed from the circle.
Requirements
-------
circles app and share by mail app enabled

Steps to reproduce
-------------
1. add an email address to a circle
2. share a folder/file with the circle
3. remove the email address from the circle
4. try to access the link that is sent to the email address

email user has still access!

Additional information
----------
For every circle share is a non user specific link token created. this token is sent to the email-members.
An other problem is, that if you have forced password usage for link shares and share by mail shares, this link is still accessible without a password. 

Tested with:
Nextcloud 15.0.10
Circles 0.16.9
share by mail 1.5.0

## Impact

A email-member that is removed from a circle

## Attachments
No attachments
