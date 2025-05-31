# Host Header Injection Attack - www.xnxx.com

## Report Details
- **Report ID**: 1630073
- **URL**: https://hackerone.com/reports/1630073
- **State**: Closed
- **Severity**: none
- **Submitted**: 2022-07-07T15:14:22.479Z
- **Disclosed**: 2022-11-08T19:25:00.170Z

## Reporter
- **Username**: 2_princeofpersia
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: xvideos

## Vulnerability Information
Host Header Injection Attack - www.xnxx.com

An attacker can manipulate the Host header as seen by the web application and cause the application to behave in unexpected ways. 

Very often multiple websites are hosted on the same IP address. This is where the Host Header comes in. This header specifies which website should process the HTTP request. The web server uses the value of this header to dispatch the request to the specified website. Each website hosted on the same IP address is called a virtual host.

But what happens if we specify an invalid Host Header? If Apache receives an unrecognized Host Header, it passes it to the first virtual host defined in httpd.conf. Therefore, it's possible to send requests with arbitrary Host Headers to the first virtual host. 

Another way to pass arbitrary Host headers is to use the X-Forwarded-Host Header. In some configurations this header will rewrite the value of the Host header. Therefore it's possible to make a request like:

#PoC Request -
GET / HTTP/1.1
Host: www.evil.com
Cookie: session_token=c679b2593ccbf131UluWiMWIZlNaClkTnBeFmtGoF9LW8CUvgTcRJ1QifNB9WBZD4tANB3m2QsO2qNx79pUK-m7tk2fRFm_ejHw_hEL2Hn1Milyoziqsi3GsBY7MbYOtDbwKmclffY4Yj0bsmbr7YHvmBNirDPcFfV59cscW9kqtCuYNhoigtklvNyJJulrkw1kjHwyZXeYF4t-MXTEP7GboN1B0JyVbEMsMaA%3D%3D; wpn_ad_cookie=0b43478923c27e53a385d969d9b4bca2
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.xnxx.com/
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Connection: close

#PoC Response -
HTTP/1.1 301 Moved Permanently
Content-length: 0
Location: http://www.evil.com/
Connection: close

#PoC Payload -
Host: evil.com

Please verify and fix the same.

## Impact

Tampering of Host header can lead to the following attacks:
Web Cache Poisoning-Manipulating caching systems into storing a page generated with a malicious Host and serving it to others and more.

## Attachments
- poc9.png
