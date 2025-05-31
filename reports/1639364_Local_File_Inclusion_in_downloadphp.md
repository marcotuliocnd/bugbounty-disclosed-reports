# Local File Inclusion in download.php

## Report Details
- **Report ID**: 1639364
- **URL**: https://hackerone.com/reports/1639364
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-07-17T04:04:26.623Z
- **Disclosed**: 2024-07-19T14:42:27.032Z

## Reporter
- **Username**: tokyoenigma
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Able to download arbitrary files using directory traversal via *filePathDownload* parameter provided the attacker knows a valid file path of an externally-facing document.

To reproduce:
1. Go to https://███████.mil/download.php?filePathDownload=data_products/MISC/frida_cal/../../../../../../../../etc/passwd

This appears to only work if a valid file directory that is externally-facing is utilized before the directory traversal (in this case, data_products/MISC/frida_cal/)

## Impact

The ability to download arbitrary files could lead to:
-Sensitive information disclosure
-In certain cases, code execution on the server

## System Host(s)
████.mil

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Go to https://███.mil/download.php?filePathDownload=data_products/MISC/frida_cal/../../../../../../../../etc/passwd

This appears to only work if a valid file directory that is externally-facing is utilized before the directory traversal (in this case, data_products/MISC/frida_cal/)

## Suggested Mitigation/Remediation Actions
Implement the parameter in such a way that externally-facing files are identified and referred to by IDs instead of by file path. In this way, directory traversal is not possible.
Ex. download.php?docID=d14fb1aa-dd71-4c76-8e41-ba047efb7dfe

Additionally, avoid trusting user input by validating that only expect values are submitted and accepted.



## Attachments
No attachments
