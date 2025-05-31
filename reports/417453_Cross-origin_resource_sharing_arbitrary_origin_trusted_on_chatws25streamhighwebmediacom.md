# Cross-origin resource sharing: arbitrary origin trusted on chatws25.stream.highwebmedia.com

## Report Details
- **Report ID**: 417453
- **URL**: https://hackerone.com/reports/417453
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-10-02T09:08:38.677Z
- **Disclosed**: 2018-10-04T08:37:56.883Z

## Reporter
- **Username**: mase289
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: chaturbate

## Vulnerability Information
*Very low-quality reports, such as those which only contain automated output, will be rejected.*

##Summary##
Hi, i was able to discover a number of  instances on chatws25.stream.highwebmedia.com were the application accepts an arbitrarily supplied origin. 

The application implements an HTML5 cross-origin resource sharing (CORS) policy for requests that allows access from any domain.  
POC
The application allowed access from the requested origin https://vazeeukllvua.com  

## Steps To Reproduce:

  1. Using an intercepting proxy , make the following request ;
GET /ws/info HTTP/1.1
Host: chatws25.stream.highwebmedia.com
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
Origin: https://vazeeukllvua.com
Cookie: __cfduid=dc7d8e518c8e0f8610c6c317c31c6f46e1538467160

  2. Observe the following request which proves that the application is vulnerable:
HTTP/1.1 200 OK
Date: Tue, 02 Oct 2018 08:25:48 GMT
Content-Type: application/json; charset=UTF-8
Connection: close
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: https://vazeeukllvua.com
Cache-Control: no-store, no-cache, must-revalidate, max-age=0
Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Server: cloudflare
CF-RAY: 4635c7cb98c72ca2-MBA
Content-Length: 79

{"websocket":true,"cookie_needed":false,"origins":["*:*"],"entropy":600356669}
  1. [add step]


## Supporting Material/References:
https://cwe.mitre.org/data/definitions/942.html
https://portswigger.net/blog/exploiting-cors-misconfigurations-for-bitcoins-and-bounties

## Impact

Since the Vary: Origin header was not present in the response, reverse proxies and intermediate servers may cache it. This may enable an attacker to carry out cache poisoning attacks.

An HTML5 cross-origin resource sharing (CORS) policy controls whether and how content running on other domains can perform two-way interaction with the domain that publishes the policy. The policy is fine-grained and can apply access controls per-request based on the URL and other features of the request.

Trusting arbitrary origins effectively disables the same-origin policy, allowing two-way interaction by third-party web sites. Unless the response consists only of unprotected public content, this policy is likely to present a security risk.
If the site specifies the header Access-Control-Allow-Credentials: true, third-party sites may be able to carry out privileged actions and retrieve sensitive information. Even if it does not, attackers may be able to bypass any IP-based access controls by proxying through users' browsers

## Attachments
No attachments
