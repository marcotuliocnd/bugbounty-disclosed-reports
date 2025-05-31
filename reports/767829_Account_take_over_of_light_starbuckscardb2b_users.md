# Account take over of 'light' starbuckscardb2b users

## Report Details
- **Report ID**: 767829
- **URL**: https://hackerone.com/reports/767829
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-01-03T19:32:55.361Z
- **Disclosed**: 2020-01-29T17:38:31.113Z

## Reporter
- **Username**: zude
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
This issue was found on https://www.starbuckscardb2b.com, this website belongs to starbucks and its is a critical vulnerability so I am reporting this.

```Issue:``` An attacker can takeover the account of the victim by creating a new account by using victim's (who is already registered) email address. 

Steps to reproduce are as follows:
1. Open https://www.starbuckscardb2b.com and go to create account.
2. for example user successfully created the account with ```abc@xyz.com``` and password ```12345678```
3. Now attacker will create the account with the email used in step 2  ```abc@xyz.com``` with different password.
4. After completion of step 3 the password for the  ```abc@xyz.com``` user will be set to the password used by attacker.
5. This will result in the account take over by attacker.

## Impact

An attacker can take over the control of any/all registered users.

## Attachments
No attachments
