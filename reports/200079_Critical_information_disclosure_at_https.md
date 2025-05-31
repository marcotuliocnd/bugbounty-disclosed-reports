# Critical information disclosure at https://█████████

## Report Details
- **Report ID**: 200079
- **URL**: https://hackerone.com/reports/200079
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-01-21T00:24:00.149Z
- **Disclosed**: 2019-12-02T18:35:17.934Z

## Reporter
- **Username**: juliocesar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**

There is a critical information disclosure at https://████████/rserver/rdPage.aspx?rdReport=db_Dashboard&rdShowModes=

**Description:**

As you can see in the video the  https://████████/rserver/rdPage.aspx?rdReport=db_Dashboard&rdShowModes= loads a page with a debug this page functions enabled, which gives the user access to server side information such some sql structure, the path to the webroot  plus some other information.

POC video : 
https://█████


## Impact

The impact here can be great, since the user have access to sql structure.

## Step-by-step Reproduction Instructions

1. Log in to the application and open the following link:  https://██████/rserver/rdPage.aspx?rdReport=db_Dashboard&rdShowModes=

## Product, Version, and Configuration (If applicable)

Tested on firefox latest version

## Suggested Mitigation/Remediation Actions

Reference: https://www.owasp.org/index.php/Full_Path_Disclosure

**Mitigation**

Turn of the debugger trace report or limit the access only to administrator

## Attachments
No attachments
