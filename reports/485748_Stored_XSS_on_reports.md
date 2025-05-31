# Stored XSS on reports.

## Report Details
- **Report ID**: 485748
- **URL**: https://hackerone.com/reports/485748
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-01-25T08:22:50.228Z
- **Disclosed**: 2019-04-01T16:39:45.718Z

## Reporter
- **Username**: giddsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Summary:** 
Stored XSS can be submitted on reports, and anyone who will check the report the XSS will trigger. 

**Description:**
Stored XSS, also known as persistent XSS, is the more damaging than non-persistent XSS. It occurs when a malicious script is injected directly into a vulnerable web application. 

## Steps To Reproduce:

  1. Go to https://app.mopub.com/reports/custom/
  2. Click **New network report**.
  3. On the name, enter payload: **"><img src=x onerror=alert(document.domain)>**
  4. Click **Run and save** then XSS will trigger. 

**Demonstration of the vulnerability:**
PoC: ████


Tested on Firefox and chrome.

## Impact

The attacker can steal data from whoever checks the report.

## Attachments
No attachments
