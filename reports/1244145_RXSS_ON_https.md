# RXSS ON https://██████████

## Report Details
- **Report ID**: 1244145
- **URL**: https://hackerone.com/reports/1244145
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-06-25T12:14:22.126Z
- **Disclosed**: 2022-02-14T21:14:48.841Z

## Reporter
- **Username**: iam_a_jinchuriki
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
Cross-Site Scripting (XSS) attacks are a type of injection, in which malicious scripts are injected into otherwise benign and trusted websites. XSS attacks occur when an attacker uses a web application to send malicious code, generally in the form of a browser side script, to a different end user. Flaws that allow these attacks to succeed are quite widespread and occur anywhere a web application uses input from a user within the output it generates without validating or encoding it.

An attacker can use XSS to send a malicious script to an unsuspecting user. The end user’s browser has no way to know that the script should not be trusted, and will execute the script. Because it thinks the script came from a trusted source, the malicious script can access any cookies, session tokens, or other sensitive information retained by the browser and used with that site

## References

## Impact

XSS can have huge implications for a web application and its users. User accounts can be hijacked, credentials could be stolen, sensitive data could be exfiltrated, and lastly, access to your client computers can be obtained

## System Host(s)
████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1)Paste the payload and you will get a popup https://███/███=%3Cscript%3Ealert(document.domain)%3C/script%3E█████

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
