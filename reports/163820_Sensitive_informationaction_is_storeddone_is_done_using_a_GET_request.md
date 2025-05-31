# Sensitive information/action is stored/done is done using a GET request

## Report Details
- **Report ID**: 163820
- **URL**: https://hackerone.com/reports/163820
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-27T14:22:15.682Z
- **Disclosed**: 2019-06-23T09:11:49.022Z

## Reporter
- **Username**: saurabhb
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: khanacademy

## Vulnerability Information
###Description:
The action **to remove an email from account** is done using a GET request and it has **security token**.

The URL is : `https://www.khanacademy.org/settings/unlinkaccount?email=█████&fkey=<security token here>`

It is never a good practice to have sensitive information in URL. Following are the reasons:
+ GET requests can be cached
+ GET requests remain in the browser history
+ GET requests can be bookmarked

Whereas:
+ POST requests are never cached
+ POST requests do not remain in the browser history
+ POST requests cannot be bookmarked

###Attack Scenario:
If the URL goes in the hands of malicious user then host a malicious website and perform a CSRF attack against the victim and this un-link that email address.




## Attachments
No attachments
