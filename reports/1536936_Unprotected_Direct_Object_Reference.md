# Unprotected Direct Object Reference

## Report Details
- **Report ID**: 1536936
- **URL**: https://hackerone.com/reports/1536936
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-04-11T00:18:26.846Z
- **Disclosed**: 2022-12-01T17:24:05.518Z

## Reporter
- **Username**: coyemerald
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
Hello MTN Security Team,
During my hunting,
I discovered that there's an Insecure Direct Object Reference  on https://nin.mtnonline.com 
Vulnerable Path:  https://nin.mtnonline.com/nin/success?message=1

Steps To Reproduce:
You may not even require to submit any NIN before accessing this unprotected page,
Just visit https://nin.mtnonline.com/nin/success?message=1 

I discovered that, to  see other user's NIN, it only require 2 difference , example
https://nin.mtnonline.com/nin/success?message=3
https://nin.mtnonline.com/nin/success?message=5
https://nin.mtnonline.com/nin/success?message=7
https://nin.mtnonline.com/nin/success?message=9
https://nin.mtnonline.com/nin/success?message=11
https://nin.mtnonline.com/nin/success?message=1901
https://nin.mtnonline.com/nin/success?message=1903
https://nin.mtnonline.com/nin/success?message=8001

## Impact

This bug exposed all the submitted Nigerians National Identity Number (NIN) .which can be abused in other way else if found out by a malicious person

## Attachments
No attachments
