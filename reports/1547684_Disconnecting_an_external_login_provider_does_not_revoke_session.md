# Disconnecting an external login provider does not revoke session

## Report Details
- **Report ID**: 1547684
- **URL**: https://hackerone.com/reports/1547684
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-04-22T05:14:45.434Z
- **Disclosed**: 2022-12-01T19:50:54.122Z

## Reporter
- **Username**: attackerbhai2003
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi team,

Summary:
attacker could create a backdoor using google login function.if an attacker stole the  login password of victims throught any means. attacker could connect his/her google account and create a backdoor and attacker login with google  if the victim disconnect attacker session did  not expire and still get access beacuse of no session expire after disconnected with google account .attacker could still connect his google account again.

Steps To Reproduce:
  1. attacker stole the  login password of victims throught any means - https://accounts.shopify.com {{attacker prespective}}
  2.  attacker could connect his/her google account {{attacker prespective}}
 3. attacker login with google authentication {{attacker prespective}}
4. victim disconnect attacker session did  not expire and still get access beacuse of no session expire  in the attacker browser after disconnected with google account {{victims prespective}}
5. attacker could still connect his google account again. {{attacker prespective}}

POC video attached in this report

## Impact

no session expire after disconnected with google account an attacker can still logined to the victim account .thus an attacker could create a backdoor in victim account to login even if the victims changes the password attacker has a backdoor way to login to the account .

## Attachments
No attachments
