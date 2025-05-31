# failure to invalidate session on password change

## Report Details
- **Report ID**: 145488
- **URL**: https://hackerone.com/reports/145488
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-17T17:44:59.869Z
- **Disclosed**: 2017-04-20T15:09:39.387Z

## Reporter
- **Username**: pradeepch99
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Steps to reproduce
1. Login as user1 in firefox browser
2. Go to http://localhost/nextcloud/index.php/settings/personal
3. Go to other browser (chrome) and login as user1
4. Change the password in chrome 

Observe that the session in firefox still works

## Attachments
No attachments
