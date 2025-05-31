# Usernames ending in .json are not restricted

## Report Details
- **Report ID**: 161935
- **URL**: https://hackerone.com/reports/161935
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-21T14:22:39.025Z
- **Disclosed**: 2017-07-10T10:03:36.541Z

## Reporter
- **Username**: karthic
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Desciption:
Username  in *.json   is not restricted.

disallowed *.json is allowed in username  restriction

URL   :  https://gratipay.com/robots.txt

User-agent: *
Disallow: /*.json
Disallow: /on/*

POC URL:
https://gratipay.com/~karthic.json/  and you will end up at my profile page.

## Attachments
No attachments
