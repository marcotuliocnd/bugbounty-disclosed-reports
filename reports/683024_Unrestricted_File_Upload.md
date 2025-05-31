# Unrestricted File Upload

## Report Details
- **Report ID**: 683024
- **URL**: https://hackerone.com/reports/683024
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-08-27T14:51:39.563Z
- **Disclosed**: 2020-05-11T16:40:09.327Z

## Reporter
- **Username**: javilarx8
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
The endpoint at https://███████/ui/core/index.html required authentication, but navigating to https://█████/ui/core/index.html?mode=public#expl-tabl./SHARED/rpchllmd/CSAT allow for read/write access.

**Description:**
The endpoint at https://████/ui/core/index.html?mode=public#expl-tabl./SHARED/rpchllmd/CSAT allowed for read as well as write access. It was possible to create directories and upload images as well as .exe files such as putty.exe. 

## Impact
An attacker can attempt to use the site to host malware, or perform social engineering attacks since the domain URL will be a .mil address.

## Step-by-step Reproduction Instructions

1. Navigate to:
https://████/ui/core/index.html?mode=public#expl-tabl./SHARED/rpchllmd/CSAT
2. Create sub-directory 
3. Upload test files
4. Files are then uploaded and hosted on a .mil website without authenticating to the application.

## Product, Version, and Configuration (If applicable)
FileCloud software
https://www.getfilecloud.com/
## Suggested Mitigation/Remediation Actions
Enforce authentication on endpoints of the application, restrict file uploads to only necessary business requirements. If possible restrict uploads to .jpg .pfd .docx. Don't allowed upload of executable files

## Impact

An attacker can attempt to use the site to host malware, or perform social engineering attacks since the domain URL will be a .mil address.

## Attachments
No attachments
