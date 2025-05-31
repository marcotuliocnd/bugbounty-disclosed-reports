# Cross Site Scripting

## Report Details
- **Report ID**: 2587844
- **URL**: https://hackerone.com/reports/2587844
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-07-06T09:57:02.745Z
- **Disclosed**: 2024-08-16T16:10:05.230Z

## Reporter
- **Username**: prakhar0x01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hii Team,

Through researching your asset, I found a XSS vulnerability at `www.███.████████`.

**The only concern is that it only works in the Firefox browser.**

## Impact

An attacker could execute arbitrary javascript in the client browser.

## System Host(s)
www.███.██████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1 - Open Firefox browser.
2 - Navigate to `https://www.██████.███████/852585B6003EBA25/Login.html?open&ErrMsg=invalidlogin%22%20test=%22X%22%20onclick=%22confirm(%27H4CKED%20BY%20PRAKHAR0X01%27)`
3 - Press : `ALT+SHIFT+X` on **Windows/Linux**, and on **OS X**, it’s `CTRL+ALT+X`.

**_NOTE: we need to convince the user to press a specific key combination. In Firefox on Windows/Linux, it’s `ALT+SHIFT+X`, and on OS X, it’s `CTRL+ALT+X`._**

███████

## Suggested Mitigation/Remediation Actions
- Sanitize the input effectively.



## Attachments
No attachments
