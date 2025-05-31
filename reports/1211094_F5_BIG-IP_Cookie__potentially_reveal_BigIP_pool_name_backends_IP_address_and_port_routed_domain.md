# F5 BIG-IP Cookie  potentially reveal BigIP pool name, backend's IP address and port, routed domain.

## Report Details
- **Report ID**: 1211094
- **URL**: https://hackerone.com/reports/1211094
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-05-27T21:56:56.970Z
- **Disclosed**: 2021-06-28T11:19:10.188Z

## Reporter
- **Username**: reebak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
Hi Team,
I hope everything is well. I am Kabeer Saxena a Security Researcher and I have found a bug

Issue:
----------
 F5 BIG-IP Cookie Remote Information Disclosure

Vulnerable IP: 
----------------
██████:443 
Certificate Information: ==X509v3 Subject Alternative Name:==
==DNS:████████==

Summary:
------------
Team with the help of Shodan[https://www.shodan.io/host/███████]  I found that the IP was assigned with F5 Big IP cookie, The last request captured was of 20th May 2021 and the request was:
```
nginx1.14.2
HTTP/1.1 200 OK
Server: nginx/1.14.2
Date: Thu, 20 May 2021 14:46:00 GMT
Content-Type: text/html;charset=ISO-8859-1
Content-Length: 2257
Connection: keep-alive
Set-Cookie: JSESSIONID=██████████; Path=/informaticaCSM; HttpOnly
Set-Cookie: BIGipServercsm-pool=██████████; path=/; Httponly; Secure
```
Where we can see  BIGipServercsm-pool=███████ cookie.
The f5 Big-IP cookies potentially reveal BigIP pool name, backend's IP address and port, routed domain.

Team When I tried visiting the URL it redirected me to the network.informatica subdomain where BIGIP cookie has different name==[BIGipServernetwork-int-pool]==and was encrypted  ,So I took the cookie from the Shodan History which is ==BIGipServercsm-pool=█████==

Image of the shodan request with IP and Certificate : https://ibb.co/TctrWKB 

The remote host ███████:443   appears to have an F5 BIG-IP load balancer(or behind load balancer) and the unencrypted cookie may disclose BigIP pool name, backend's IP address and port, routed domain.
The remote host appears to be an F5 BIG-IP load balancer. The load balancer encodes the IP address of the actual web server that it is acting on behalf of within a cookie. Additionally, information after 'BIGipServer' is configured by the user and may be the logical name of the device. These values may disclose sensitive information, such as internal IP addresses and names.

Proof-Of-Concept:
--------------------
observe the cookies in the following request 
a Big-IP cookie represents [encoded IP].[encoded port].0000.

I followed https://sra.io/blog/finding-and-decoding-big-ip-and-netscaler-cookies-with-burp-suite/ for decoding the cookie and the final IP pool name and port decoded is

==█████==


Remediation:
-----------------
Encrypting the cookies from BigIP


I hope you find the report useful. Thankyou for your time

Related reports, best practices
--------------------------------
https://support.f5.com/csp/article/K14784?sr=45997495
http://www.systemadvise.com/2016/11/f5-big-ip-cookie-remote-information.html
https://www.rapid7.com/db/modules/auxiliary/gather/f5_bigip_cookie_disclosure

## Impact

Attacker can leaks backend information (pool name, backend's IP address and port, routed domain) through cookies inserted by the BigIP system.

## Attachments
No attachments
