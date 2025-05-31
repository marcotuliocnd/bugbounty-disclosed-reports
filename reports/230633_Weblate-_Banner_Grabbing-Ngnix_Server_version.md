# Weblate- Banner Grabbing-Ngnix Server version

## Report Details
- **Report ID**: 230633
- **URL**: https://hackerone.com/reports/230633
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-05-22T10:57:32.016Z
- **Disclosed**: 2017-06-05T06:31:44.644Z

## Reporter
- **Username**: sadhu16
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hey, I have found in the HTTP response header from docs.weblate.org, the nginx web server version  is disclosed.

Ideally application server responds back to users error message in customzied manner by not revealing any sensitive information about webserver or underlying components in applicatio.

Please see the below attached screenshots for issue details.


Url on which i found this issue-https://docs.weblate.org/en/latest/

Please also refer -http://nginx.org/en/security_advisories.html

For More Info refer-https://www.owasp.org/index.php/Testing_for_Web_Application_Fingerprint

Note :Revealing the specific software version of the server might allow the server machine to become more vulnerable to attacks against software that is known to contain security holes. Server implementors are encouraged to make this field a configurable option.

## Attachments
- SERVER_VERSION_DISCLOSED.png
- Request_N_Response.png
- SERVER_VERSION_DISCLOSED-1.png
