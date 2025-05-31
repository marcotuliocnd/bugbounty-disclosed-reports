# New link opening method makes hackerone vulnerable to tabnabbing

## Report Details
- **Report ID**: 1159398
- **URL**: https://hackerone.com/reports/1159398
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-04-09T19:12:56.352Z
- **Disclosed**: 2021-07-07T08:49:31.383Z

## Reporter
- **Username**: recon_ninja
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Hackerone recently changed how it opens the external links and this new way is vulnerable to tabnabbing.
**Description:**
Please see the POC.
### Steps To Reproduce

1.  Click here:  https://awasthi7.github.io/
2.  Click on proceed when warning appears.
3.  The site will open in new tab and hackerone tab will be replaced by Google.

### Optional: Your Environment (Browser version, Device, etc)

 * 

### Optional: Supporting Material/References (Screenshots)

 *

## Impact

Unvalidated redirect

## Attachments
No attachments
