# Unauthorized Account Access via Leaked Credentials in URL Format (Account Takeover )

## Report Details
- **Report ID**: 3080597
- **URL**: https://hackerone.com/reports/3080597
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2025-04-07T12:55:43.790Z
- **Disclosed**: 2025-05-07T23:08:32.838Z

## Reporter
- **Username**: firec4t
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: khanacademy

## Vulnerability Information
I discovered a critical vulnerability that allows attackers to access user accounts on khanAcademy.com using credentials publicly available on VirusTotal., an attacker can directly authenticate into a user’s account without any secondary verification or alert to the user.
i have reported a similar issue , here's the report ( 2981324 ) 

this time the email and password of the victim is archived in clear text ( https://en.khanacademy.org/login,██████,,█████████,,,█████████,██████████,Personal )

by entering the mail ( ██████████ ) and password ( ███████ ) in the login , the attacker can easily perform account takeover

Please Enforce 2FA: Make two-factor authentication mandatory, especially for accounts with detected exposure.

## Impact

Full account takeover: Unauthorized access to user accounts with no user awareness.

Exposure of personal data: Private information such as learning progress, messages, and linked accounts may be compromised.

Potential financial or reputational damage: If linked to other services, this access may lead to wider exploitation.

## Attachments
No attachments
