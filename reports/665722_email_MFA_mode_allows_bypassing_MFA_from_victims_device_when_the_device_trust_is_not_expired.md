# “email” MFA mode allows bypassing MFA from victim’s device when the device trust is not expired

## Report Details
- **Report ID**: 665722
- **URL**: https://hackerone.com/reports/665722
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-08-02T02:55:13.236Z
- **Disclosed**: 2019-08-12T18:19:39.032Z

## Reporter
- **Username**: l1nkworld
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: grammarly

## Vulnerability Information
**Summary:**
It is possible bypass MFA without the need to have the phone code.

**Description:** 
When we turn on the MFA and we have the user and password of the user, it is possible bypass the MFA only changing some values the endpoint POST `auth.grammarly.com//v3/api/login`

## Steps To Reproduce:
Note: 
- Use burp suite or another tool to intercept the requests

  1. Turn on and configure your MFA
  2. Login with your email and password
  3. The page of MFA is going to appear
  4. Enter any random number
  5. when you press the button "sign in securely" intercept the request POST `auth.grammarly.com/v3/api/login` and in the POST message change the fields:
- `"mode":"sms"` by `"mode":"email"`
-  `"secureLogin":true` by `"secureLogin":false`
 6. send the modification and check, you are in your account! It was not necessary to enter the phone code.

## Impact

The attacker can bypass the experimental MFA, If the attacker has the email and password, the attacker can login in the account without the need of the phone code.

## Attachments
No attachments
