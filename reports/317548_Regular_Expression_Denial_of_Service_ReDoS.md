# Regular Expression Denial of Service (ReDoS)

## Report Details
- **Report ID**: 317548
- **URL**: https://hackerone.com/reports/317548
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-02-19T11:29:12.393Z
- **Disclosed**: 2019-04-03T20:00:47.887Z

## Reporter
- **Username**: danny_grander
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
The issue was already fixed.

**Module:** is-my-json-valid

**Summary:** 
Affected versions of this package are vulnerable to Regular Expression Denial of Service (ReDoS) attacks. It used a regular expression (/^\S+@\S+$/) in order to validate emails. This can cause an impact of about 10 seconds matching time for data 90K characters long.

**Description:** 
Regex:
 formats.js
 exports[‘email’] = /^\S+@\S+$/
(introduced in 2014, 34a1a706)


## Supporting Material/References:

* https://github.com/mafintosh/is-my-json-valid/pull/159
* https://github.com/mafintosh/is-my-json-valid/commit/b3051b277f7caa08cd2edc6f74f50aeda65d2976

## Impact

Denial of service through blocking the event loop.

## Attachments
No attachments
