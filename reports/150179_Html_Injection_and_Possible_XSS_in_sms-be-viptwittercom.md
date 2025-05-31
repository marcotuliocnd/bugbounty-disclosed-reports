# Html Injection and Possible XSS in sms-be-vip.twitter.com

## Report Details
- **Report ID**: 150179
- **URL**: https://hackerone.com/reports/150179
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-09T04:46:26.833Z
- **Disclosed**: 2016-08-28T23:45:09.867Z

## Reporter
- **Username**: secgeek
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hi,
I would like to report HTML Injection and possible cross site scripting (XSS) vulnerability in **sms-be-vip.twitter.com**

##Overview

The **sms-be-vip.twitter.com** 404 error page appears to be vulnerable to XSS and HTML Injection as it doesn't encode the HTML tags in the path name such as ```https://sms-be-vip.twitter.com/<h1>TEST</h1>```.

But the HTML tags have to be send without URL encoding. Most of the modern web browsers will encode the HTML tags in the request before it being sent to the webserver. However In Internet Explorer 11 and lower versions it's possible to make the browser send the request without any URL encoding.

### How to make MSIE 7 - 11 send the request without URL encoding ?

Internet Explorer won't encode the URL if it was sent from a 302 Redirect.

So you can use a simple PHP page like the following:

```php
<?php
$url = $_GET['x'];
header("Location: $url");
?> 
```

Then use the  page and perform a redirection to the endpoint which is vulenrable to XSS.

``` http://secgeek.net/POC/redir.php?x=https://sms-be-vip.twitter.com/<h1>TEST</h1> ```


Now you could notice that the friendly HTTP error messages in Internet Explorer will appear instead of showing the **<h1>TEST</h1>** in the error page.

There is a simple workaround for this issue. 
According to Microsoft the HTTP friendly error message will appears if it meets two criteria

1.The HTTP Status code must be [400, 403, 404, 405, 406, 408, 409, 410, 500, 501, 505]
2.The HTTP Response body’s byte length must be shorter than a threshold value

```Ruby
 The default threshold value for 404 errors is 512 bytes.
```
So we can add more data in the request to be returned in the server response that will overcome this issue.

```http://secgeek.net/POC/redir.php?x=https://sms-be-vip.twitter.com/<h1>TEST</h1>.................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................... ```

##Techincal Details

##Impact:

The vulnerability allow a malicious user to inject html tags and execute Javascript in the same context of sms-be-vip.twitter.com domain which could lead to steal user's session, peform CSRF attacks or open a phishing page.

##Affected Domain:
sms-be-vip.twitter.com

##Affected Insertion point:
The path name in the url ```https://sms-be-vip.twitter.com/<XSS Injection here>```

##HTML Injection POC
http://secgeek.net/POC/Twitter-HTML-POC.php

##XSS POC
http://secgeek.net/POC/Twitter-XSS-POC.php

**Note:** This XSS POC will work only if the XSS Auditor is disabled in Internet Explorer. 

I've Attached Sreenshots for the two POCs.

Kindly check and review the issue.
Thanks in advance!






## Attachments
- POC2.png
- POC1.png
