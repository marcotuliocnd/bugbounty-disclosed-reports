# Attachment references in markdown don't warn before downloading 

## Report Details
- **Report ID**: 1386277
- **URL**: https://hackerone.com/reports/1386277
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-10-29T22:06:35.432Z
- **Disclosed**: 2022-02-25T17:06:07.850Z

## Reporter
- **Username**: iamr0000t
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
By default if any link of report is clicked, There will be a popup to user 
that you're visiting a third-party website please proceed at your own risk etc. 
However, when a user views the report all links are non clickable and file URI is appended. 
I have Found out that I can bypass this functionality by appending a " and ) in the end . 
For example if you view this link  as PDF and click the link it will simply redirect you to the URL. 

there will be a popup,  That you are visited a third party domain etc.
**Description:**

### Steps To Reproduce

1. create a H1 report with the following payload 

(https://example.com") 

2. view the report click export and view as pdf
3. hover the link and click . 
4. observe that you are directly redirected without any warning of going to third party domain. 

### Optional: Your Environment (Browser version, Device, etc)

 * 

### Optional: Supporting Material/References (Screenshots)

 *

## Impact

By using this vulnerability an attacker might be able to get a victims IP address , make them login etc.

## Attachments
No attachments
