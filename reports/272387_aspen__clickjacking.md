# aspen | clickjacking

## Report Details
- **Report ID**: 272387
- **URL**: https://hackerone.com/reports/272387
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-09-27T13:23:13.508Z
- **Disclosed**: 2017-09-27T14:29:26.494Z

## Reporter
- **Username**: sadhu16
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: aspen

## Vulnerability Information
Hi Team,

Found vulnerability of clickjacking on the domain "aspen.io".

Please refer the below attached screenshot as POC.

<html>
<head>
<title>Clickjack test page</title>
</head>
<body>
<p>Website is vulnerable to clickjacking!</p>
<iframe src="http://django.aspen.io/en/latest/" height="500"></iframe>
</body>
</html>

2.save it as <anyname>.html eg cj.html
3.and just simply open that in browser

Issue Details :Clickjacking (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on, thus potentially revealing confidential information or taking control of their computer while clicking on seemingly innocuous web pages.

The server didn't return an X-Frame-Options header which means that this website could be at risk of a clickjacking attack. The X-Frame-Options HTTP response header can be used to indicate whether or not a browser should be allowed to render a page in a <frame> or <iframe>. Sites can use this to avoid clickjacking attacks, by ensuring that their content is not embedded into other sites.

This vulnerability affects Web Server.

As far as i know this data is enough to prove that your site is vulberable to Clickjacking..
according to OWASP its more than enough..
https://www.owasp.org/index.php/Testing_for_Clickjacking_(OWASP-CS-004)

Solution

https://www.owasp.org/index.php/Clickjacking_Defense_Cheat_Sheet
check this out..here is the solution for that.

Refer the attached screenshot for issue details.


## Attachments
- clickjacking-aspen.png
