# Storage of old passwords in plain text format

## Report Details
- **Report ID**: 1549217
- **URL**: https://hackerone.com/reports/1549217
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-04-24T06:40:14.362Z
- **Disclosed**: 2022-05-12T13:06:30.085Z

## Reporter
- **Username**: subuganz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: recorded-future

## Vulnerability Information
## Summary:

Server response from app.recordedfuture.com has old passwords for a logged in account in plain text format. Storage of password(s) in any readable format or using weak hashes put the account or system at great risk. What's interesting is how RecordedFuture store multiple passwords (not just 1 but 2 latest passwords) in a readable format. Anybody within Recorded Future has now access to those passwords and also, users who share their account access internally within their teammates during emergency investigations can get access to those passwords too.  Regardless of old or current password storing them in a plain text is a big no. 

## Steps To Reproduce:

- Login to Recorded Future
- Send a POST request to  https://app.recordedfuture.com/rf/kobradata/user/get/user
- Intercept the request through a web proxy and take a look at the server response
- Look under 'params'
-'_password1' and '_password2' shows the old passwords in plain text

  

## Supporting Material/References:
 Attached is the obfuscated screenshot showing the password params

## Impact

-Storing passwords in plaintext is bad because it puts both the system and users at risk.
-RF internal devs get access to accidentally look at those passwords
- Account sharing (which happens within companies) put the seat holder at risk because the password pattern can be used elsewhere to compromise other accounts (Insider threat/malicious intention). Also, people tend to reuse the passwords

## Attachments
- Screen_Shot_2022-04-24_at_1.34.50_AM.png
