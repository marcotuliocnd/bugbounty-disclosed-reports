# Unauthenticated arbitrary file upload on the https://█████/ (█████████)

## Report Details
- **Report ID**: 698789
- **URL**: https://hackerone.com/reports/698789
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-09-20T12:33:21.405Z
- **Disclosed**: 2024-08-16T16:04:07.322Z

## Reporter
- **Username**: sp1d3rs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
##Description
I was able to identify unsafe upload endpoint on the https://█████/upload.php

##POC
1) Go to the https://█████████/upload.php
2) Upload some test file.
You will see success message:
████
3) Visit `https://███/delete.me` and you will see your uploaded file there
I uploaded example test file with string `test file`
█████████

## Impact

Arbitrary file upload, may lead to the Stored XSS, hosting attacker's content and code execution.

## Attachments
No attachments
