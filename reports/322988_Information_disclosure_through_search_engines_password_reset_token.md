# Information disclosure through search engines (password reset token)

## Report Details
- **Report ID**: 322988
- **URL**: https://hackerone.com/reports/322988
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-03-06T22:22:47.361Z
- **Disclosed**: 2018-03-13T18:31:38.883Z

## Reporter
- **Username**: luciann
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: upserve

## Vulnerability Information
Search on google for: 
site:"hq.breadcrumb.com"

Or access this link:
https://www.google.com/search?q=site%3A%22hq.breadcrumb.com%22&oq=site%3A%22hq.breadcrumb.com%22&aqs=chrome..69i57j69i58.6216j0j7&sourceid=chrome&ie=UTF-8

Note that this vulnerability can be obtain on other search engines.

## Impact

An attacker can obtain an unused password reset token found using google.com in order to get access to an user account. 

In order to better ensure the security of the application do not allow google indexing of the token/password reset controller.

## Attachments
- Selection_037.png
- Selection_038.png
