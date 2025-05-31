# Passcode bypass on Talk Android app

## Report Details
- **Report ID**: 1784645
- **URL**: https://hackerone.com/reports/1784645
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-11-26T12:04:28.024Z
- **Disclosed**: 2023-01-09T05:49:57.485Z

## Reporter
- **Username**: ctulhu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
It is possible to bypass the passcode protection in nextcloud android talk by clicking the notification of a message.

Talk App Android version: ```15.0.2 RC1```

## Steps To Reproduce:

1. Create two users
1. Using User A login it to the web interface while User B on Talk App Android
1. Using User B setup the passcode protection in settings
1. Using User A send a message to User B
1. Wait for the notification and click it

## Supporting Material/References:

█████

## Impact

To exploit this the attacker needs to have a physical access to the  target's device which makes it severity to medium. 
Due to the bypass of passcode an attacker is able to access the user's nextcloud files and view conversations.

████████

## Attachments
No attachments
