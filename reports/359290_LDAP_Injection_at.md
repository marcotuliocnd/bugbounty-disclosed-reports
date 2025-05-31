# LDAP Injection at ██████

## Report Details
- **Report ID**: 359290
- **URL**: https://hackerone.com/reports/359290
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-05-29T13:21:41.942Z
- **Disclosed**: 2019-12-02T19:05:49.524Z

## Reporter
- **Username**: tampe125
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
An LDAP Injection has been found at the mentioned domain

**Description:**
While performing a user registration, is it possible to edit the request and inject invalid characters, resulting in a LDAP injection

## Step-by-step Reproduction Instructions
1. Visit page https://█████████/Registration/Home/New
2. Start a new registration process with "regular" data
3. The request is correctly processes  
4. Start a new registration process and use a double quote as first name
5. You will get a fatal error

Attached you can find the rogue request and the screenshot of the fatal error.  
Error `0x80005000` is specific of LDAP, this means that the application is trying to handle user data without sanitizing it

## Suggested Mitigation/Remediation Actions
Application should sanitize **all** user input before trying to store it in any way.

## Impact

Attacker could enumerate current domain or exfiltrate data.  
On more practical terms, since user should be manually validated, attacker could bypass such activation.
That's a serious threat, because all requests must be approved and verified by other US Officers.

## Attachments
No attachments
