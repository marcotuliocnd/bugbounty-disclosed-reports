# SAML authentication bypass

## Report Details
- **Report ID**: 812064
- **URL**: https://hackerone.com/reports/812064
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-03-06T10:09:08.702Z
- **Disclosed**: 2020-06-18T17:23:50.076Z

## Reporter
- **Username**: tomp1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
## Summary

When using SAML authentication, responses are not checked properly. This allows attacker to inject/modify any assertions in the SAML response and thus, for example, authenticate as administrator.

## Description

Following code snippets are from *app/meteor-accounts-saml/server/saml_utils.js*
When checking the signature, the first Signature element which is found in the whole response XML is used:

`316 const signature = xmlCrypto.xpath(doc, '//*[local-name(.)=\'Signature\' and namespace-uri(.)=\'http://www.w3.org/2000/09/xmldsig#\']')[0];`

 After the XML signature has been verified, the code proceeds to use the first Response element found in the whole XML to get assertions and attributes. 

`516 const response = doc.getElementsByTagNameNS('urn:oasis:names:tc:SAML:2.0:protocol', 'Response')[0];`

**However there is no check that the signature that was checked relates to the response element that is being used.** Thus attacker can take a valid SAML response, with some valid signature, and add Response element, that has no signatures, in the beginning of the XML. The code finds the original signature and validates that, but proceeds to use the malicious Response element, which is found first in the document.

Also the validating the status from the response happens before signature validation

`501 const statusValidateObj = self.validateStatus(doc);`

## Releases Affected:

Tested on 3.0.3 but appears to affect all versions based on the history of saml_utils.js file.

## Steps To Reproduce (from initial installation to vulnerability):

  1. Configure the application to use SAML authentication
  1. When logging in, intercept the POST request with a proxy tool
  1. Use the attached `samlbypasspoc.py` file to create a new value for the parameter `SAMLResponse`. Run the script in python3 with the URL encoded SAMLResponse as argument.
  1. Replace the parameter value with the one given by the POC script and forward the request

This requires altering the POC to suite the configuration. Beginning from the line 25, you can alter the response elements as needed to desired values. 

In the sample POC file, attributes `OrganizationName` and `Email` and the element `NameID` are changed. In the setup I tested this resulted in login as a newly created admin.

## Supporting Material/References:

  * samlbypasspoc.py

## Suggested mitigation

  * Refactor the code so that the same elements (references) are used when checking the signature and when reading the attributes
  * Do not use hard coded indexes when selecting the elements

## Impact

SAML authentication can be bypassed and attacker can log in as any user (e.g. admin user)

## Attachments
- samlbypasspoc.py
