# User Information Disclosure via REST API

## Report Details
- **Report ID**: 197786
- **URL**: https://hackerone.com/reports/197786
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-01-12T10:20:10.906Z
- **Disclosed**: 2017-04-19T14:08:17.176Z

## Reporter
- **Username**: 4websecurity
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: owncloud

## Vulnerability Information
Hello,

REST-API, allows anonymous access to functionality that allows a hacker to list all users who have published a post on a WordPress site. Unfortunately, this generally includes the admin account

POC: https://owncloud.com/wp-json/wp/v2/users/
https://owncloud.com/wp-json/wp/v2/users/1/


Kind Regards,
Alex.

## Attachments
No attachments
