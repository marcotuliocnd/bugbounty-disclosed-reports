# Reflected XSS in https://███████ via search parameter

## Report Details
- **Report ID**: 975024
- **URL**: https://hackerone.com/reports/975024
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-09-05T03:13:30.489Z
- **Disclosed**: 2020-11-02T21:41:37.622Z

## Reporter
- **Username**: kegn
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
Reflected XSS in https://█████████

**Description:**
I noticed I got an error when visiting https://███.mil stating
```The provided hostname is not valid for this server```

I pinged the site to see that it resolves to https://██████

 ██████

Based on the content of the site I believe this asset is a DOD asset due to the logos and verbiage. The staff page has all @mail.mil email contacts. If I should report this to https://www.us-cert.gov/report instead, please allow me to self close this as the owner/operator on this one is tough to determine.

 ██████████

The search parameter is subject to Reflected XSS

 - Visit https://█████/search?search_text=%3Cscript%3Ealert%28document.domain%29%3C%2Fscript%3E
 - See the response in browser

 ████

## Impact

Reflected XSS allows an attacker to send seemingly legitimate links to a victim, potentially stealing cookies or other sensitive session data via unwanted javascript execution

## Attachments
No attachments
