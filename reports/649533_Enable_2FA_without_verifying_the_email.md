# Enable 2FA without verifying the email

## Report Details
- **Report ID**: 649533
- **URL**: https://hackerone.com/reports/649533
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-07-18T16:21:16.837Z
- **Disclosed**: 2019-10-25T08:13:30.342Z

## Reporter
- **Username**: rioncool22
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: moneybird

## Vulnerability Information
# Description : 
I able to add 2FA to my account without verifying my email

# Attack scenario : 
1. Attacker sign up with victim email (Email verification will be sent to victim email).
2. Attacker able to login without verifying email.
3. Attacker add 2FA.

## Impact

the victim can't register an account with victim email. If the victim reset the password, the password will change, but the victim can't login because 2FA.

## Attachments
- Screenshot_from_2019-07-18_12-20-05.png
- Screenshot_from_2019-07-18_12-19-52.png
