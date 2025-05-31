# Reflected XSS on ███████ page

## Report Details
- **Report ID**: 915573
- **URL**: https://hackerone.com/reports/915573
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-07-04T22:02:35.204Z
- **Disclosed**: 2020-07-30T17:54:08.060Z

## Reporter
- **Username**: scraps
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
The page at https://█████/NtMView.php is vulnerable to reflected cross-site scripting. 

**Description:**
The page takes a user input in the form of a drop down list, then uses that text in the resulting page ( ███████ ). An attacker can intercept the query to the page and insert an XSS payload, as shown in ██████████. 

This input is then displayed back to the user, popping up the XSS payload ██████████. The XSS payload is actually inserted a number of times into the resulting HTML, which can be seen in ████████. This results in numerous pop ups to the user. 

## Step-by-step Reproduction Instructions
While intercepting requests with a proxy such as Burp, carry out the following steps

1. Visit the page at https://██████/usnotice.php
2. Select a value from the drop down list and press "View Now"
3. Add an XSS payload to the POST parameters,  eg, ``<script>alert('xss')</script>``
4. Observe on the next page the XSS pop-ups


## Suggested Mitigation/Remediation Actions
Any user controlled input should be filtered by the application to remove special characters such as  ``<`` and ``>``, as well as special words such as ``script``. 

For further guidance, see: https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html

## Impact

In this instance, the only person the XSS affects is myself, ie, Self-XSS. This could be weaponised to affect other users though, for example by being placed in a web form on an attacker controlled page, then tricking a user to click the link to visit the .mil page. An attacker who exploited this vulnerability could rewrite the contents of the page, potentially redirecting users to further malicious sites, or temporarily defacing the .mil page

## Attachments
No attachments
