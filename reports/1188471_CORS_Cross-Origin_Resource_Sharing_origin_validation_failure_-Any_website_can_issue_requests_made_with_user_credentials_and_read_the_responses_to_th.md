# CORS (Cross-Origin Resource Sharing) origin validation failure -Any website can issue requests made with user credentials and read the responses to th

## Report Details
- **Report ID**: 1188471
- **URL**: https://hackerone.com/reports/1188471
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-05-07T19:37:58.718Z
- **Disclosed**: 2021-06-10T15:00:35.502Z

## Reporter
- **Username**: bader2
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
Welcome!
==In this report I want to describe a high-level bug that can seriously put a user account at risk.==


>CORS (Cross-Origin Resource Sharing) defines a mechanism to enable client-side cross-origin requests. This application is using CORS in an insecure way.

>The web application fails to properly validate the Origin header (check Details section for more information) and returns the header Access-Control-Allow-Credentials: true.

>In this configuration any website can issue requests made with user credentials and read the responses to these requests. Trusting arbitrary origins effectively disables the same-origin policy, allowing two-way interaction by third-party web sites.


CORS (Cross-Origin Resource Sharing) origin validation failure

URL:
https://sifchain.finance/wp-json/


>Attack Details

>Access-Control-Allow-Origin:https://sifchain.finance/wp-json/
>Access-Control-Allow-Credentials: true Prefix origins are accepted (www.example.com)

>Vulnerability Description

>CORS (Cross-Origin Resource Sharing) defines a mechanism to enable client-side cross-origin requests. This application is using CORS in an insecure way.

The web application fails to properly validate the Origin header (check Details section for more information) and returns the header Access-Control-Allow-Credentials: true.

>In this configuration any website can issue requests made with user credentials and read the responses to these requests. Trusting arbitrary origins effectively disables the same-origin policy, allowing two-way interaction by third-party web sites.

>Discovered by CORS (Cross-Origin Resource Sharing) origin validation failure









**[+]HTTP Request[+]**

```
GET /wp-json/ HTTP/1.1
Origin: https://sifchain.finance.evil.com
Cookie: __cfduid=da5ef3c17e04aebc9116ae15cd01be3561620412712;wordpress_test_cookie=WP%20Cookie%20check;jetpack_sso_nonce=roj2x7yk6yj00kjzh1lm;jetpack_sso_redirect_to=https%3A%2F%2Fsifchain.finance%2F
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36
Host: sifchain.finance
Connection: Keep-alive
```



How to fix this vulnerability
=====================
Allow only selected, trusted domains in the Access-Control-Allow-Origin header.
------------------------------------------------------------------------------------



**[+] Classification[+]**
- CWE
- CWE-942
- CVSS
- Base Score: 5.4 - CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:N
- Attack Vector: Network
- Attack Complexity: Low
- Privileges Required: None
- User Interaction: Required
- Scope: Unchanged
- Confidentiality: Low
- Integrity: Low
- Availability: None









Web References

This is an [CORS Security Considerations](https://fetch.spec.whatwg.org/#security/).




#PoC

1-Run the proxy
 2- Enter the Firfox or any Browser 
3- Enter URL: https://sifchain.finance/wp-json/
4- open Burp suite
 5-intercopt is on 
6- Request intercepted
 7- Send to Repeater
 8- Go

An example of a request+
```
GET /wp-json/ HTTP/1.1
Origin: https://sifchain.finance.evil.com
Cookie: __cfduid=da5ef3c17e04aebc9116ae15cd01be3561620412712;wordpress_test_cookie=WP%20Cookie%20check;jetpack_sso_nonce=roj2x7yk6yj00kjzh1lm;jetpack_sso_redirect_to=https%3A%2F%2Fsifchain.finance%2F
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36
Host: sifchain.finance
Connection: Keep-alive
```
9- Done

## Impact

**Any website can issue requests made with user credentials and read the responses to these requests.**

## Attachments
No attachments
