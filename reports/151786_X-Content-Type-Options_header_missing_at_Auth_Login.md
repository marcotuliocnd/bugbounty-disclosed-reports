# X-Content-Type-Options header missing at Auth Login

## Report Details
- **Report ID**: 151786
- **URL**: https://hackerone.com/reports/151786
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-16T16:25:52.299Z
- **Disclosed**: 2016-08-18T08:43:38.406Z

## Reporter
- **Username**: kiraak-boy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gocd

## Vulnerability Information
Hello Again,

The doesn't have a header settings for X-Content-Type Options which means it is vulnerable to MIME sniffing. The only defined value, "nosniff", prevents Internet Explorer and Google Chrome from MIME-sniffing a response away from the declared content-type. This also applies to Google Chrome when downloading extensions. This reduces exposure to drive-by download attacks and sites serving user uploaded content that by clever naming could be treated by MSIE as executable or dynamic HTML files.

URL :- http://arbaz:8153/go/auth/login

Thanks!

## Attachments
No attachments
