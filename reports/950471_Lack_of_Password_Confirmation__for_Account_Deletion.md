# Lack of Password Confirmation  for Account Deletion

## Report Details
- **Report ID**: 950471
- **URL**: https://hackerone.com/reports/950471
- **State**: Closed
- **Severity**: none
- **Submitted**: 2020-08-03T20:47:36.374Z
- **Disclosed**: 2020-08-11T12:22:35.537Z

## Reporter
- **Username**: cybrot
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
Description:  Issue in the zomato android application is that the user account can be deleted without confirming user password or re authentication.
 The removal of account is one of the sensitive part of any application that needs to protect, therefore removing an account should validate the authenticity of the legitimate user. 

Steps To Reproduce:
1. Login through google authentication in the Zomato android application. 

2. Do some modification like change user name, add user address etc.

3. Go to account settings and click on delete account. Give any reason for deletion and click next..

4. There will next page where click on delete my account now option. 

Remediation:
System must confirm authentic user before performing such task. A link can be send to user email id that can be used for delete operation. Otherwise user password should be provided to application to confirm the entity identity.



POC Video Link : https://drive.google.com/file/d/1645NnultPzEIvR1rPwBRFOOeV234U9mV/view?usp=sharing

## Impact

It seems to be of very low impact,but consider a situation when user forget to logout from his account or someone get access to his phone and delete the account. This situation is more severe than account takeover as there is no way to get account again. All the save information and data including previous record, card information etc will be deleted.

C: Low
I:   Medium
A: High

## Attachments
No attachments
