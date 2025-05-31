# Unvalidated redirect on user profile website

## Report Details
- **Report ID**: 143265
- **URL**: https://hackerone.com/reports/143265
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-06T03:04:50.478Z
- **Disclosed**: 2017-05-18T16:55:21.458Z

## Reporter
- **Username**: roshanpty
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
The user profile redirect request is not properly validated. The presence of parameter t which is being passed through the request is verified but same value can be reused to any unauthenticated or authenticated user to redirect them to any web site.

Sample link is given below.

https://www.zomato.com/redirect?u=http%3A%2F%2Ftest.com&t=38dc43d5f007f4c5d974f6c74f065158&g=user-profile-website

## Attachments
No attachments
