# Reflected XSS - https://███

## Report Details
- **Report ID**: 1260823
- **URL**: https://hackerone.com/reports/1260823
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-07-13T18:06:48.287Z
- **Disclosed**: 2021-07-29T19:44:12.547Z

## Reporter
- **Username**: fiveguyslover
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Greetings, I just found an XSS vulnerability on a page of one of your websites

URL : 
https://████=%22%3E%3Cscript%3Ealert(1)%3C/script%3E

```
https://███="><script>alert(1)</script>
```
By the way, could you look at my "duplicated" report when it is not?
I don't mean any disrespect, but this is not the same page.
thank you - https://hackerone.com/reports/1260789

Best regards, 
fiveguyslover

## Impact

A reflected XSS vulnerability happens when the user input from a URL or POST data is reflected on the page without being stored, thus allowing the attacker to inject malicious content.

## System Host(s)
████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
URL : 
https://█████=%22%3E%3Cscript%3Ealert(1)%3C/script%3E
the alert will be displayed

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
