# Android app does not clear end to end encryption keys

## Report Details
- **Report ID**: 1189168
- **URL**: https://hackerone.com/reports/1189168
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-05-08T19:36:02.535Z
- **Disclosed**: 2021-06-16T08:57:38.495Z

## Reporter
- **Username**: rtod
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
1. userA on serverA sets up end to end encryption on their android device
2. userA has some end to end encrypted data
3. userA removes their account on serverA from their android device (for whatever reason)
4. attacker (evil admin) obtains the device of userA
5. attacker (evil admin) logs in on the account of userA  (reset the pw and just log in)
6. attacker (evil admin) can see and access all encrypted files

## Impact

While I believe the impact is minimal since you need to obtain the device of the victim.
Once you remove your account all information regarding that account should be removed.

* the keys
* the mnemonic

And certainly when you re-add an account you should be asked to enter your mnemonic!

## Attachments
No attachments
