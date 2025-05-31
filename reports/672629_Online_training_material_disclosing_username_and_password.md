# Online training material disclosing username and password

## Report Details
- **Report ID**: 672629
- **URL**: https://hackerone.com/reports/672629
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-08-13T19:48:08.714Z
- **Disclosed**: 2019-10-08T18:41:39.814Z

## Reporter
- **Username**: scraps
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
A training document is revealing username and password details for what appears to be a DoD training system

**Description:**
Using the google dork ``site:*.mil ext:ppt intext:password``, I was able to find a number of powerpoint documents on .mil websites that include username and passwords.

This document appears to be some old training materials

Slide 39 of www.███████/█████████ 

See: █████████

In this instance, the document relates to an online training platform at https://████████/, so if the credentials are still valid, anyone who reads that presentation could potentially access that system and any data it holds. Training databases often have elements of sensitive data left over from old production databases, so this may expose sensitive information.

**Please note that I did not attempt to login using the credentials, as I didn't want to violate any terms of your policy.**

If you would like me to attempt to login to test this vulnerbility, please let me know. 

## Step-by-step Reproduction Instructions

Using the google dork ``site:*.mil ext:ppt intext:password``, examine any results which appear to include usernames or passwords

See: ███

## Impact

Attackers may be able to access the contents of either system, which could include sensitive data.

## Attachments
No attachments
