# Bypass Password Authentication to Update the Password

## Report Details
- **Report ID**: 982293
- **URL**: https://hackerone.com/reports/982293
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-09-15T03:32:01.316Z
- **Disclosed**: 2021-02-12T06:41:21.627Z

## Reporter
- **Username**: a13h1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Summary:**  This additional security measure from twitter provides protection to the victim's account, considering that a victim's session may have been hijacked by a hacker, however, due to this additional layer of security Implemented by twitter the hacker would not be able to change the victim's Password, as they will be prompted to enter the victim's account password In order to make these changes, which will not be known to a hacker (In case of a session hijack)

This report is to bring to your attention a security vulnerability that will allow hackers that have hijacked a user's session to bypass the password screen (Without knowing the user's password)

**Description:**  For users that have had their twitter flightschool session hijacked, this security vulnerability would enable a hacker to completely take over a victim's account as they will be able to change the victim's password by bypassing the old password by the unrestricted rate limit or brute forcing in the password
the victim account could be hijacked by session hijacking or XSS cookies grabbing 

## Steps To Reproduce:

With the assumption that the victim's twitter session is 'hijacked' and in a 'logged in' state for the hacker. The below steps must be followed In order to reproduce the security vulnerability.

Security Vulnerability #1 - Update Victim's Password - Bypass old password by unrestricted rate limiting

1.Go to My Profile
2.Click on Edit Profile-> Change Password
3.Enter any random password and Click on 'Next' F988224
4.Intercept the request the above request and send it to intruder F988225 
5.Then select the position old password F988226
6.Then go in payload add password list F988227
7.Then start the attack bcoz of no rate limit the password bruteforcing is continue and find the correct password and update the old one
F988228  , F988229



##Resolution: Apply the Rate Limitation

## Impact

This a serious security vulnerability, as It could lead to a hacker completely taking over the user's account by overriding twitter's security protocol as they could use this technique to bypass the password and it use to fully takeover the victim password

## Attachments
- flightschool11.PNG
- flighschool12.PNG
- flightschool13.PNG
- flightschool14.PNG
- flightschool1.PNG
- flightschool2.PNG
