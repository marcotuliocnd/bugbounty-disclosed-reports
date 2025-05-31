# Rxss on █████████ via logout?service=javascript:alert(1)

## Report Details
- **Report ID**: 1406598
- **URL**: https://hackerone.com/reports/1406598
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-11-21T20:11:26.318Z
- **Disclosed**: 2021-12-22T16:21:43.142Z

## Reporter
- **Username**: m00n_knight
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
I found open redirect and xss (Rxss) at the ██████████ logout page, https://████/██████████/logout?service=https://google.com It also allows javascript URIs, leading to Xss

## Impact

Attacker can trick users to visit malicious websites or can lead to phishing and many other type of attacks, and can steal user token, IP & etc. with xss

## System Host(s)
████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Take this URL: https://███████/█████████/logout?service=https://google.com
  1. Change "https://google.com" to whatever URL you want to redirect to.
  1. Visit the URL and click on back button and you will be redirected to that site
  1. for xss replace https://www.google.com with you xss payload ex: https://██████████/██████/logout?service=javascript:alert(1)

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
