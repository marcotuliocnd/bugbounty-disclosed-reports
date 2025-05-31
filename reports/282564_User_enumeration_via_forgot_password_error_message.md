# User enumeration via forgot password error message

## Report Details
- **Report ID**: 282564
- **URL**: https://hackerone.com/reports/282564
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-10-24T17:36:07.917Z
- **Disclosed**: 2017-10-27T08:05:08.652Z

## Reporter
- **Username**: kiddie
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: infogram

## Vulnerability Information
Hi Team,

Vulnerable URL :
https://infogram.com/forgot

Description:
During testing forgot password field whether it's rate limiting is working or not, I noticed forgot password field is vulnerable to user enumeration. When user enter email id which is not available into database it shows an error " E-mail not recognized".

Mitigation: handle the above situation correctly, e.g.: "Reset link is send to email : xxxx@xxx.xxx". This doesn't inform the attacker  E-mail not recognized and make enumeration more difficult

Thanks and regards,
Kiddie

Refer Ticket : #77067
#123496

## Attachments
No attachments
