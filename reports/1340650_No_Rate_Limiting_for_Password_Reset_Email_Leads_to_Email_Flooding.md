# No Rate Limiting for Password Reset Email Leads to Email Flooding

## Report Details
- **Report ID**: 1340650
- **URL**: https://hackerone.com/reports/1340650
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-09-15T16:51:40.123Z
- **Disclosed**: 2022-03-26T17:58:04.540Z

## Reporter
- **Username**: bd10ceb041a5297f881137c
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: upchieve

## Vulnerability Information
There is "No Rate Limiting" implemented in sending the Password Reset Email. Thus, attacker can use this Vulnerability to bomb out the Email Inbox of the victim.
Affected URL : https://hackers.upchieve.org/resetpassword

Steps to Reproduce: 
1. Log In to : https://hackers.upchieve.org/
2. Go To : https://hackers.upchieve.org/resetpassword
3. Enter Email to reset password and click Enter and Capture the request on Burp Suite.
4. Send the captured request to Intruder and repeat the request in loop
5. Then just check the Email, your email will be flooded by UPchieve Reset Password Email.

Remediation :
Rate limiting should be implemented to Prevent Email Flooding.

## Impact

Email Flooding can create Trouble to the users on the website because huge email bombing can be done by the attackers within seconds.

## Attachments
- UPchieve.png
