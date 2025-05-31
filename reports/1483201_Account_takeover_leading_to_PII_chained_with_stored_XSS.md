# Account takeover leading to PII chained with stored XSS

## Report Details
- **Report ID**: 1483201
- **URL**: https://hackerone.com/reports/1483201
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-02-17T10:11:36.538Z
- **Disclosed**: 2022-04-16T08:20:52.040Z

## Reporter
- **Username**: imthatt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_vdp

## Vulnerability Information
## 
I have found a vulnerability on https://vehiclestdb.fas.gsa.gov/ for account takeovers
The website is not using proper authentication to claim the user signing in is actually the account owner due to only requiring an email address to sign in and no password. This leads to an attacker being able to place a stored XSS payload within the victims profile and reveals PII including phone numbers of the victim. 

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Visit https://vehiclestdb.fas.gsa.gov/
  2. Enter  email address in the signing form itsdavenn@gmail.com (or for official account use tesg@gsa.gov)
  3. You have now signed in as a users account you do not own and if you browse to the profile you can see PII in the form of phone numbers.
4. We can do this with any registered user
5. You can place an XSS stored payload on the users profile in the first name field using ant" autofocus onfocus=prompt(1) x=" 

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]
Please re create these steps to see the impact

## Impact

An attacker can takeover any users account from just knowing the email address, from here on in they can find PII in the form of phone numbers and place stored XSS on the users profile to execute JavaScript code on the users profile.

## Attachments
No attachments
