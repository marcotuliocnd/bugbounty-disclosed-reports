# Admin.MyTVA.com Customer lookup and internal notes bypass

## Report Details
- **Report ID**: 2043552
- **URL**: https://hackerone.com/reports/2043552
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-06-29T20:14:54.705Z
- **Disclosed**: 2023-10-13T12:32:36.833Z

## Reporter
- **Username**: itssixtynein
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: tennessee-valley-authority

## Vulnerability Information
## Summary:
The admin.mytva.com site does not properly secure the admin only endpoints, which can allow an attacker to bypass the login and take actions like looking up customers. The endpoints can be enumerated through the forgot password function.

## Steps To Reproduce:


  1. Navigate to https://admin.mytva.com/Account/ForgotPassword.aspx and enter 'admin' as the ID
  2. Wait on the admin email to appear (this should also be restricted)
  3. Attempt to send the reset password and capture the request with BURP
4. Review the response to the request for new endpoints. Some of them that will stand out are:
/Evaluation/EditNotes.aspx?ProjectId=
/Evaluation/HOEvalDetailWONav.aspx?ProjectID=
/Tools/Customer/AddressLookup.aspx
5. The endpoints do not protect themselves for bruteforcing either, so the attacker can now attempt to retrieve further information or add internal/customer notes

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

Unprotected endpoints may lead to a data breach. It would be recommended to check the logs for previous attacks

## Attachments
- customer.JPG
- notes.JPG
- request.JPG
