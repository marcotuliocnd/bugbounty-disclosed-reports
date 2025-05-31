# Some limited confidential information can still be accessed after a user exits a private program

## Report Details
- **Report ID**: 2278865
- **URL**: https://hackerone.com/reports/2278865
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-12-08T20:57:05.997Z
- **Disclosed**: 2024-01-19T13:11:44.014Z

## Reporter
- **Username**: oauth2
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Good morning team!!!
I identified a bug where it is possible to access some limited confidential information from a private program even after you have already exited that program. 
information like:
:number of domains
:Bounties paid
:Number of hackers paid
:Response efficiency
:Minimum reward and maximum reward
:Sobre

steps:
1:do you accept a private invitation
2:you add this program to your favorites
3:the expiry date for sending reports arrives
4:Now you can no longer send reports to this program or have access to its policy page
5:now go to opportunities -> My programs
6:And there is your program and you have access to the information mentioned above

## Impact

Disclosure of private program information

## Attachments
No attachments
