# Open Redirection in index.php page

## Report Details
- **Report ID**: 320376
- **URL**: https://hackerone.com/reports/320376
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-02-27T17:35:48.568Z
- **Disclosed**: 2018-03-07T16:39:13.032Z

## Reporter
- **Username**: prashantkumar96
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Redirection is performed by HackerOne website when **index.php** page is visited. The parameter to **index.php** is used in redirection. By manipulating this parameter, an attacker can redirect victim outside www.hackerone.com

**Description:**
When a user visit www.hackerone.com/index.php/xyz, he/she is redirected to www.hackerone.com/xyz. However, when visiting www.hackerone.com/index.php/index.phpxyz, user will be redirected to www.hackerone.comxyz (without a slash between **com** and **xyz**).

Further, when visiting www.hackerone.com/index.php/index.php.hacker0ne.com, user will be redirected to www.hackerone.com.hacker0ne.com, a domain **hacker0ne.com**

### Steps To Reproduce

1. Visit https://www.hackerone.com/index.php/index.php.hacker0ne.com
2. Notice that the site redirects to https://www.hackerone.com.hacker0ne.com/

## Impact

Attacker can phish users

## Attachments
No attachments
