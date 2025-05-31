# Report redaction doesn't apply to report title update activities

## Report Details
- **Report ID**: 196358
- **URL**: https://hackerone.com/reports/196358
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-01-06T18:54:28.012Z
- **Disclosed**: 2017-02-25T03:17:48.704Z

## Reporter
- **Username**: b21cbe5e1e1a9be6a2b9da3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
The *Redact* option doesn't redact all keywords identified in the report- which may leave sensitive information unredacted.

**Description (Include Impact):**
The option only search through reporter's initial report & follow-up comments, leaving other comments untouched. Furthermore, it doesn't search in changes to report status. For better clarity, please refer to my screenshot attached.   
For example, if a team member has changed the report title, it fails to redact changes. Any such status changes are left untouched which is insufficient prior to full disclosure IMO.  

### Steps To Reproduce
For easier reproduction, please;  
1. Change report Title prior to redact keywords  
2. Now, redact some texts from report title as in screenshot  

Screenshots:  
{F149867} 

## Attachments
- Screenshot_from_2017-01-07_00-25-46.png
