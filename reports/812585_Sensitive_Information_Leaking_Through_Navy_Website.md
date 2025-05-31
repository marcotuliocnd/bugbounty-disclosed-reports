# Sensitive Information Leaking Through Navy Website. [█████]

## Report Details
- **Report ID**: 812585
- **URL**: https://hackerone.com/reports/812585
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-03-07T03:32:51.234Z
- **Disclosed**: 2020-05-14T17:59:19.800Z

## Reporter
- **Username**: rootuser
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
 While performing recon work on websites owned by DoD i came up with a Navy website which is leaking sensitive information.

**Description:**
The website is leaking information such as- first name and last name, email address, phone number, location, rank, and other information of trainees in a clear readable pdf document. This is a high severity issue and requires immediate fixation. It is also a clear privacy violation and insufficient protection mechanism involved in data storage.
 
## Step-by-step Reproduction Instructions

1. Open a web browser of your choice.
2. Now open this URL: https://███████/sites/██████/Documents/health-promotion-wellness/reproductive-and-sexual-health/██████████

## Suggested Mitigation/Remediation Actions
Remove document from the internet or put applicable authorization mechanism(s) in order to access sensitive documents.

## Impact

Any person can access this document and cause:
1. Information leakage.
2. Impersonation a person.
3. Commit crimes under a fake identity.

## Attachments
No attachments
