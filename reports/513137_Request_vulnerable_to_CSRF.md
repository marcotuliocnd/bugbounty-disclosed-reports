# Request vulnerable to CSRF

## Report Details
- **Report ID**: 513137
- **URL**: https://hackerone.com/reports/513137
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-03-21T12:33:42.910Z
- **Disclosed**: 2019-03-22T13:21:49.561Z

## Reporter
- **Username**: saidul_khan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: phabricator

## Vulnerability Information
There are 4 instances of this issue:
[+] /dashboard/panel/render/12/
[+] /dashboard/panel/render/22/
[+] /dashboard/panel/render/4/
[+] /dashboard/panel/render/6/

Issue background ==>
Cross-site Request Forgery (CSRF) is an attack which forces an end user to execute unwanted actions on a web application to which he/she is currently authenticated. With a little help of social engineering (like sending a link via email / chat), an attacker may trick the users of a web application into executing actions of the attacker's choosing. A successful CSRF exploit can compromise end user data and may allow an attacker to perform an account hijack. If the targeted end user is the administrator account, this can compromise the entire web application.

Issue remediation ==>
The application should implement anti-CSRF tokens into all requests that perform actions which change the application state or which add/modify/delete content. An anti-CSRF token should be a long randomly generated value unique to each user so that attackers cannot easily brute-force it.

It is important that anti-CSRF tokens are validated when user requests are handled by the application. The application should both verify that the token exists in the request, and also check that it matches the user's current token. If either of these checks fails, the application should reject the request.

## Impact

Cross-site Request Forgery (CSRF) is an attack which forces an end user to execute unwanted actions on a web application to which he/she is currently authenticated. With a little help of social engineering (like sending a link via email / chat), an attacker may trick the users of a web application into executing actions of the attacker's choosing. A successful CSRF exploit can compromise end user data and may allow an attacker to perform an account hijack. If the targeted end user is the administrator account, this can compromise the entire web application.

## Attachments
- csrf_report.html
