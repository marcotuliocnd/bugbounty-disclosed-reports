# Stored XSS at https://www.█████████.mil

## Report Details
- **Report ID**: 1081994
- **URL**: https://hackerone.com/reports/1081994
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-01-20T00:34:36.040Z
- **Disclosed**: 2021-02-01T17:48:48.502Z

## Reporter
- **Username**: 5050thepiguy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
Stored XSS exists at https://www.██████.mil. A user can fill out the form and upload a file containing javascript code to trigger XSS. 

**Description:**
Stored XSS exists at https://www.████.mil. A user can fill out the form and upload a file containing javascript code to trigger XSS. 


## Impact
A user can steal cookies, deface a site, etc. 

## Step-by-step Reproduction Instructions

(1) Go to https://www.██████.mil/jppso/vendor/WFDPMMiscInvoicingDocuments.aspx
(2) Fill out the form, upload a file, and add the file
(3) Once the file is uploaded right click to get to the Developer Tools.
(4) Inspect the page and find the path for the file -- █████\file.txt. For example, the file path for the file I uploaded is as follows: https://www.██████.mil/jppso/vendor/Data/cme1rjjcnjhnvdzhf5lgfbge-01192021-065856_testing-new.html
(5) Observe that XSS is triggered.

## Product, Version, and Configuration (If applicable)
https://www.████████.mil
Tested in Firefox

## Suggested Mitigation/Remediation Actions

## Impact

Stored XSS exists at https://www.█████.mil. A user can fill out the form and upload a file containing javascript code to trigger XSS.

## Attachments
No attachments
