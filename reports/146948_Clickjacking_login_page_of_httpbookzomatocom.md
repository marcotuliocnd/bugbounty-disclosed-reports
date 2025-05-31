# Clickjacking login page of http://book.zomato.com/

## Report Details
- **Report ID**: 146948
- **URL**: https://hackerone.com/reports/146948
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-24T05:50:20.989Z
- **Disclosed**: 2017-05-18T16:55:58.640Z

## Reporter
- **Username**: benoculars
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
The login page on book.zomato.com (http://book.zomato.com/account/login.aspx) is vulnerable to a clickjacking attack.

### Reproduction steps:

1. Paste the following HTML into a text editor and save the file as .html

```
<html>
<body>
<iframe src="http://book.zomato.com/account/login.aspx" width="500" height="500">
</body>
</html>
```

2. Open the file in a web browser
3. Note that the iframe appears with the login page inside

### Remediation:
Using the X-Frame-Options header.

OWASP: https://www.owasp.org/index.php/Clickjacking_Defense_Cheat_Sheet




## Attachments
No attachments
