# Application Error disclosure, Verification token seen error and user able to change password

## Report Details
- **Report ID**: 642494
- **URL**: https://hackerone.com/reports/642494
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-07-13T15:31:51.599Z
- **Disclosed**: 2019-08-28T15:31:21.094Z

## Reporter
- **Username**: amol01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kartpay

## Vulnerability Information
## Summary:
Application Error disclosure, Verification token seen error and user able to change password

## Browsers Verified In:

Broswer version:
Google Chrome is up to date
Version 75.0.3770.100 (Official Build) (64-bit)

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  Steps to reproduce issue:
1.	https://merchant.kartpay.com/register
Enter Firstname, Enter LastName, Enter “Email address”, Enter Phone and Click on SIGN UP

Press SIGN UP button
2.	We are getting below error and 

Failed to authenticate on SMTP server with username "xtravalue" using 2 possible authenticators.
Authenticator LOGIN returned Expected response code 250 but got an empty response. Authenticator PLAIN returned Expected response code 250 but got an empty response.

Also token exposed in error message

'https://merchant.kartpay.com/verification/2AK9vH0sQVwpAIMy7THNYrvBQkqgEGptPCWHqw87ZnT6ko

3. Copied Verification token and Paste in browser, here you can changed password page
  https://merchant.kartpay.com/verification/2AK9vH0sQVwpAIMy7THNYrvBQkqgEGptPCWHqw87ZnT6kog8z3



## Supporting Material/References:
Please find attachment SMTP Error.doc

  * [attachment / reference]

## Impact

Impact : 
#1 Attacker can enter find email id and phone number of customer easily in India, and change his/her password
#2  SMTP error, give all file name on sever related to Authentication

## Attachments
- SMTP_Error.docx
