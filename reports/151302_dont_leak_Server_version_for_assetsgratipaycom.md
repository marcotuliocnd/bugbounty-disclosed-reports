# don't leak Server version for assets.gratipay.com

## Report Details
- **Report ID**: 151302
- **URL**: https://hackerone.com/reports/151302
- **State**: Closed
- **Severity**: none
- **Submitted**: 2016-07-14T10:33:39.594Z
- **Disclosed**: 2017-08-21T13:31:18.820Z

## Reporter
- **Username**: ahsan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Hey, I've captured the HTTP request while visiting assets.gratipay.com

**_The whole HTTP response is as following_**:
```
GET / HTTP/1.1
Host: assets.gratipay.com:443
Accept: */*
Accept-Encoding: gzip, deflate, sdch, br
Accept-Language: en-US,en;q=0.8
Origin: https://www.youtube.com
Referer: https://www.youtube.com/watch?v=0-gIBjd8Hws
User-Agent: Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36
X-Chrome-UMA-Enabled: 1
X-Client-Data: CIq2yQEIpLbJAQjEtskBCPGcygE=

HTTP/1.1 404
cache-control: no-cache
content-encoding: gzip
content-type: text/html; charset=UTF-8
date: Thu, 14 Jul 2016 10:28:14 GMT
server: NetDNA-cache/2.2
status: 404
via: 1.1 vegur
x-content-type-options: nosniff
x-frame-options: SAMEORIGIN
x-gratipay-version: 1976
x-xss-protection: 1; mode=block
```

So as you can see that the "server: NetDNA-cache/2.2" is showing the NetDNA-cache server and version!

I hope you'll fix it!

Note: If you are not going to fix this one, please close this as informative! :)

Thanks,
Ahsan Tahir

## Attachments
No attachments
