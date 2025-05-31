# Bypassing Recaptcha Protection in  `https://connect.acronis.com`

## Report Details
- **Report ID**: 1655629
- **URL**: https://hackerone.com/reports/1655629
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-08-01T06:59:05.710Z
- **Disclosed**: 2024-10-30T20:35:57.472Z

## Reporter
- **Username**: regexr
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
The Recaptcha Token is not validated in `https://connect.acronis.com/auth/register`
The Invader can reuse the same Token to create infinite other user accounts, and flood the system.

{F1847755}

{F1847756}

##Suggested Mitigation/Remediation Actions:
1. Limiting the request to once every X minutes.
2. Make sure that every request is checked for correct recaptchaand is then processed.

## Impact

The whole purpose of having the security feature of captcha has gone in vain.

##Possible Scenarios:
1. Attacker could use this vulnerability to bomb out the system.
2. Attacker might cause denial of service to servers.

## Attachments
- 200_OK.png
- Request.png
