# Unauthenticated arbitrary file upload on the https://█████/ (█████.mil)

## Report Details
- **Report ID**: 698793
- **URL**: https://hackerone.com/reports/698793
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-09-20T12:36:21.975Z
- **Disclosed**: 2024-07-19T14:36:19.202Z

## Reporter
- **Username**: sp1d3rs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
##Description
I was able to identify unsafe upload endpoint on the https://██████/upload.php

##POC
1) Go to the https://██████/upload.php
2) Upload some test file.
You will see success message, leaking some internal paths
3) Visit `https://██████████/delete.me` and you will see your uploaded file there
I uploaded example image file there:
█████

## Impact

Arbitrary file upload, may lead to the Stored XSS, hosting attacker's content and code execution.

## Attachments
No attachments
