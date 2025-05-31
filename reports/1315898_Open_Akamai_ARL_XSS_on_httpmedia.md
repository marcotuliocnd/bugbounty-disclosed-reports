# Open Akamai ARL XSS on http://media.████████

## Report Details
- **Report ID**: 1315898
- **URL**: https://hackerone.com/reports/1315898
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-08-22T18:54:22.821Z
- **Disclosed**: 2024-07-26T15:01:38.873Z

## Reporter
- **Username**: renzi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**

Hello,
I found a Reflected Cross site Scripting (XSS) Open Akamai ARL on  http://media.████, With this security flaw is possible executing JS codes...

## References
https://owasp.org/www-community/attacks/xss/
https://community.akamai.com/customers/s/article/WebPerformanceV1V2ARLChangeStartingFebruary282021?language=en_US

## Impact

The attacker can execute JS code.

## System Host(s)
media.███

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Go to http://media.██████/7/0/33/1d/www.citysearch.com/search?what=x&where=place%22%3E%3Csvg+onload=confirm(document.domain)%3E

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
