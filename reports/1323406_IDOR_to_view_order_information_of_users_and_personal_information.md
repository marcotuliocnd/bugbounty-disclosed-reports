# IDOR to view order information of users and personal information

## Report Details
- **Report ID**: 1323406
- **URL**: https://hackerone.com/reports/1323406
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-08-30T03:36:08.209Z
- **Disclosed**: 2021-12-06T18:39:11.824Z

## Reporter
- **Username**: xfiltrer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: affirm

## Vulnerability Information
## Summary:
[Broken access control is the method of controlling which users can perform a certain type of action or view set of data. Broken access control is a vulnerability that allows an attacker to circumvent those controls and perform more actions than they are allowed to, or view content they typically don’t have access to. Such vulnerability, when exploited, could lead to massive loss of data.]

## Steps To Reproduce:

Navigate to https://razer.com and purchase something

Now select the option to use “Affirm” as a financing option

Look for the POST parameter of /api/██████/ and the request will inform you of the “checkout_ari”:“XXXXXXXXXXXXXXXX” generated for that specific purchase.

Forward this Request to the repeater, then change the value “checkout_ari”:“XXXXXXXXXXXXXXXX” to “checkout_ari”:“YYYYYYYYYYYYYYYYY” and the back-end will return the requested order with all the user’s purchase information from his full address, means payments, and products.

Please check the attachments for POCs

## Supporting Material/References:
 image.png1(██████████)
image2(██████████)
image3(██████)
image4(████)
video(███)

  Remediation Recommendations
Implement proper access control measures around data sets and functions. Ensure that only authorized users are able to view data or perform the functions they are intended. Implement object-based access controls. This will ensure that users who circumvent UI restrictions are still restricted from retrieving any sensitive data or perform restricted actions without proper authorization. Please review the OWASP foundations recommendations for more specific details on Broken Access Control.

References
https://www.owasp.org/index.php/Category:Access_Control

https://www.owasp.org/index.php/Access_Control_In_Your_J2EE_Application

https://www.owasp.org/index.php/Broken_Access_Control

## Impact

Once a flaw is discovered, the consequences of a flawed access control scheme can be devastating. In addition to viewing unauthorized content, an attacker might be able to change or delete content, perform unauthorized functions, or even take over site administration.

## Attachments
No attachments
