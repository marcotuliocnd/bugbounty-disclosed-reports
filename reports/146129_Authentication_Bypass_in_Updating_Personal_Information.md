# Authentication Bypass in Updating Personal Information

## Report Details
- **Report ID**: 146129
- **URL**: https://hackerone.com/reports/146129
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-20T22:20:44.337Z
- **Disclosed**: 2017-01-17T17:57:05.310Z

## Reporter
- **Username**: footstep
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: instacart

## Vulnerability Information

Hello Instacart,

Firstly, I would like to remind you that I made this report by mail 2 days ago, Sat, 16-08-2016 before I got the invite here. 

Although a user is expected to input password before updating their personal information. This is not so anyway as I have found that one could actually update "Personal Information​"​ without filling the "Current Password" field.

Steps to Reproduce:
1. Login your instacart account.
2. Go to account or https://www.instacart.com/store/account
3. In the personal information, Click Change
4. Fill new information leaving "Current Password" blank
5. Click "Save Account Information"
6. The ​​"Personal Information" will be updated.

This is a flaw as I could update my Personal Information without password although there is a field to input the password,hence, Authentication Bypass.

I hope I get a response from you soon.

​Looking Forward,
Shuaib Oladigbolu


## Attachments
No attachments
