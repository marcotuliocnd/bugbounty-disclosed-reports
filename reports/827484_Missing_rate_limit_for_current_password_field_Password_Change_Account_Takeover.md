# Missing rate limit for current password field (Password Change) Account Takeover

## Report Details
- **Report ID**: 827484
- **URL**: https://hackerone.com/reports/827484
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-03-23T18:14:29.766Z
- **Disclosed**: 2020-10-06T09:46:08.759Z

## Reporter
- **Username**: full109tun
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Vulnerability:
Missing Rate Limit for Current Password field (Password Change) Account Takeover

Steps to reproduce the bug:
1)Go to Profile > Password. Enter any (wrong password) In current password filed.
2)Now enter the new password and Turn the Intercept ON.
3)Capture the request & Send the request to Intruder and add a Payload Marker on the current password value.
4)Add the payload for the password field having a list of more than 100 password or more for test and start attack.
BOOM!

Screen shot is attached as a proof of concept.

## Impact

There is no rate limit enabled for "Current Password" field on changing password on your website. A malicious minded user can continually tries to brute force an account password. If user forget to logout account in some public computer then attacker is able to know the correct password, and also able to change the password to new one by inputting large number of payloads.

## Attachments
- acronic_1.PNG
- acronic_2.PNG
