# User files is disclosed when someone called while the screen is locked

## Report Details
- **Report ID**: 1338781
- **URL**: https://hackerone.com/reports/1338781
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-09-13T19:57:30.766Z
- **Disclosed**: 2022-03-14T15:41:56.047Z

## Reporter
- **Username**: ctulhu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
User files in the server is disclosed while the screen is locked when someone called. 

## Steps To Reproduce:
[add details for how we can reproduce the issue]

1.) Make 2 Accounts, Lets call them Account A and Account B
2.) Using Account A login to (https://nextcloud/apps/spreed/)
3.) Using Account B login to NextCloud Talk App in your Phone and Lock the Screen
4.) Using Account A call Account B
5.) Using Account B accept the call and click the Message or SMS icon in the bottom left
6.) Attach a file and Press share from your nextcloud server
7.) You can see the user files

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

████

## Impact

A malicious attacker can see the user files by calling the phone while the screen is locked.

## Attachments
No attachments
