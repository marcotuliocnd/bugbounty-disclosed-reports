# Open Akamai ARL XSS on http://master-config-████████

## Report Details
- **Report ID**: 1315907
- **URL**: https://hackerone.com/reports/1315907
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-08-22T19:00:14.676Z
- **Disclosed**: 2024-07-26T15:02:02.760Z

## Reporter
- **Username**: renzi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**

Hello,
I found a Reflected Cross site Scripting (XSS) Open Akamai ARL on  http://master-config-██████████, With this security flaw is possible executing JS codes...

## References
https://owasp.org/www-community/attacks/xss/
https://community.akamai.com/customers/s/article/WebPerformanceV1V2ARLChangeStartingFebruary282021?language=en_US

## Impact

The attacker can execute JS code.

## System Host(s)
master-config-█████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Go to http://master-config-████████/7/0/33/1d/www.citysearch.com/search?what=x&where=place%22%3E%3Csvg+onload=confirm(document.domain)%3E

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
