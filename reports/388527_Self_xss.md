# Self xss

## Report Details
- **Report ID**: 388527
- **URL**: https://hackerone.com/reports/388527
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-07-30T16:06:47.936Z
- **Disclosed**: 2020-04-05T10:26:43.041Z

## Reporter
- **Username**: iwallplace
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hello,

I found self xss your main domain.

I m sending details and I attached poc video.

Pls open 

https://nextcloud.com/about/

Use burp suite and active intercept.

Refresh this url.

And pls add this payload your url.

></title>"><script>alert(205)</script>'"><marquee><h1>nextcloud.com</h1></marquee>


Pls click intercept off and page refreshing.

Now you see xss alert.

## Impact

https://github.com/dxa4481/XSSJacking

Exploit and Impact kit for self xss

Regards.

## Attachments
- nextcloud-xss.mp4
