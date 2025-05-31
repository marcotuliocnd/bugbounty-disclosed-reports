# Open Redirect at █████

## Report Details
- **Report ID**: 1634105
- **URL**: https://hackerone.com/reports/1634105
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-07-12T06:06:11.586Z
- **Disclosed**: 2022-11-18T18:37:37.835Z

## Reporter
- **Username**: angeltsvetkov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Open Redirect on https://███

User can be redirect to malicious site
POC: ████████/texis/search/redir.html?query=1234&pr=External+Meta&prox=page&rorder=500&rprox=500&rdfreq=500&rwfreq=250&rlead=500&rdepth=62&sufs=3&order=r&u=http://evil.com&m=0&p=2

I hope you know the impact of open redirect and more info refer

https://cwe.mitre.org/data/definitions/601.html

## Impact

User can be redirect to malicious site.

## System Host(s)
███████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Just open:  █████/texis/search/redir.html?query=1234&pr=External+Meta&prox=page&rorder=500&rprox=500&rdfreq=500&rwfreq=250&rlead=500&rdepth=62&sufs=3&order=r&u=http://evil.com&m=0&p=2

Vulnerable parameter: u=

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
