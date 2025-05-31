# Reflected XSS on ██████.mil

## Report Details
- **Report ID**: 1799562
- **URL**: https://hackerone.com/reports/1799562
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-12-11T14:19:02.383Z
- **Disclosed**: 2023-01-27T18:38:36.662Z

## Reporter
- **Username**: alishah
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
While looking for *.mil, I found a website that is vulnerable to reflected XSS.

## Impact

An attacker can use it to fetch cookies/tokens from any website which requires login by using a CORS bug if the site is vulnerable to CORS.

## System Host(s)
████.mil

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Go to this URL: https://███████████████████html
2. On the search bar, write this payload. <script>alert(document.cookie)</script>
3. & you'll see the pop-up.

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
