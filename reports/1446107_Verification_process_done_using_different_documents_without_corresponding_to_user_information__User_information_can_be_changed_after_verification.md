# Verification process done using different documents without corresponding to user information / User information can be changed after verification

## Report Details
- **Report ID**: 1446107
- **URL**: https://hackerone.com/reports/1446107
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-01-11T03:15:00.729Z
- **Disclosed**: 2023-01-27T16:30:14.150Z

## Reporter
- **Username**: feynmvn__
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: exness

## Vulnerability Information
## Summary:

1. A verified user can change their profile information  (Name, DoB and Address) after identity verification using the API endpoint /kyc_back/api/v2/surveys/personal_info 
2. A  user can verifiy their account with ofical documents that does not correspond to their Name and Address information provided in verification process

*** Note -*** *my.exness.com does not allow to change profile information (Name, DoB, Address) using website or mobile app. The only point where a user can set name, address and dob is when verifying the account but after that, there is no way for the user an option to change such that information in the GUI.*

## Affected enpoints:
  - wbesite and mobile apps

## Steps to Reproduce:

***NOTE -*** The following steps covers the two issues found, changing info after verification and with documents that does not correspond to the user

  1. Open BurpSuite CE, turn off the Proxy feature in order just to log each request made by the browser.
  2. Configure your browser with BurpSuite CE proxy settings
  3. Create an account for a real account (not a demo account), you can use a properly email provider or a dispoable one too
  4. Go to https://my.exness.com/pa/settings/profile
  5. At the top of the window, there is a button that helps to go to the process to verify the account
  6. Verify the current verification step with the code sent to the email used
  7.  Verify the current verification step with the code sent to the phone number used
  7. Add any name, address and dob, click next
  7. Continue with the verification process... 
  8. Select ID card, add your documents (it could be a oficial ID card that does not correspond to you)
  9. You will asked to upload a document to proof your address, add it (you can add an oficial proof of address that is related to the previous document to comply names and address)
  10. Submit your document and wait until they are verified (Do not let the session expires, continue click on the website normally)
  11. Go to BurpSuite CE Proxy > HTTP hisotry tab > searcch for the following request and send it to Repeater: 
```
PATCH /kyc_back/api/v2/surveys/personal_info
Host: my.exness.com
```
  12. Refresh your page after some time, like 15-30 minutes more or less. 
  13. The identity verification was completed
  14. Go to Burp Suite CE Repeater tab, scroll down and change the request body json data to the following:

```
{"first_name":"test-1","last_name":"test-2","test-3":"","dob":"1990-01-01","address":"test-4"}
```

  15. Send the request, you will get a HTTP 200 response with the following body: ***{"status":"OK"}***
  17. The information was changed, you can check it out by browsing https://my.exness.com/pa/settings/profile or https://my.exnesstrade.pro/settings/personalInfo

Information when verification was completed

{F1574748}

Information when verification was completed displayed in my.exness.pro
{F1574749}

Information changed after verification

{F1574752}


Information changed after verification and displayed in my.exness.pro

{F1574751}


## Impact
An attacker can use exness.com platform to start trading under someone's information and verify their account with oficial documents that does not corresponds to them. The business logic flaw in the platform makes it a not good-trusting site for any user being part of the platform or not due to it is possible to use someone's documents.

## Mitigation
Add photo to the profile and then, facial recognition to match the photo on the ID with the person presenting the card
Address recognition to match the address on the proof of address document presented


## Supporting Material/References:
https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html

## Impact

An attacker can use exness.com platform to start trading under someone's information and verify their account with oficial documents that does not corresponds to them. The business logic flaw in the platform makes it a not good-trusting site for any user being part of the platform or not due to it is possible to use someone's documents.

## Attachments
- Screenshot_8.png
- Screenshot_9.png
- Screenshot_11.png
- Screenshot_10.png
