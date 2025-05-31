# Rate limits too low for email 2FA

## Report Details
- **Report ID**: 979820
- **URL**: https://hackerone.com/reports/979820
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-09-11T14:34:10.459Z
- **Disclosed**: 2020-10-14T18:18:31.415Z

## Reporter
- **Username**: akashhamal0x01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bitwarden

## Vulnerability Information
NO RATE LIMIT ON 2FA CAN LEAD TO ACCOUNT COMPROMISE!

1. Create account on vault.bitwarden.com  if you don't have.
2.Setup 2FA via email 
3.Logout and log in again. This time along with password you have to fill the 2fa code which is sent to the email.
4.Type Any Random number, intercept request with burp  then send to intruder, mark the code position and start bruteforcing

Results:

>>Invalid Code Response = 400 
>>Valid Code Response = 200

## Impact

2FA acts as extra security. Even if the attacker has user credentials 2FA always protects them from accessing the user data and compromise their whole account.
If the 2FA can be bruteforced it can lead to account compromise assuming that attacker already knows email and password!

## Attachments
No attachments
