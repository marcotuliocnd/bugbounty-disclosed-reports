# Reflected XSS in https://blocked.myndr.net

## Report Details
- **Report ID**: 824433
- **URL**: https://hackerone.com/reports/824433
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-03-19T09:22:27.529Z
- **Disclosed**: 2020-03-19T15:44:45.933Z

## Reporter
- **Username**: thilakesh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: myndr

## Vulnerability Information
##Summary:
Reflected XSS in Domain (https://blocked.myndr.net)

## Steps To Reproduce:
1. Go to the https://blocked.myndr.net.
2. Find the endpoint in the domain -https://blocked.myndr.net/?trg=1
3. Add the payload ?trg="><script>alert(1)</script>
4. You can see the pop up in your browser.

## Impact

With the help of XSS, a hacker or attacker can perform social engineering on users by redirecting them from real websites to fake ones. the hacker can steal their cookies and download malware on their system, and there are many more attacking scenarios a skilled attacker can perform with XSS.

## Attachments
- xss.png
