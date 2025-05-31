# CORS Misconfiguration, could lead to disclosure of sensitive information

## Report Details
- **Report ID**: 1199527
- **URL**: https://hackerone.com/reports/1199527
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-05-17T09:13:00.759Z
- **Disclosed**: 2021-06-09T19:01:18.200Z

## Reporter
- **Username**: riski0912
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: upchieve

## Vulnerability Information
Summary:
Cross Origin Resource Sharing Misconfiguration | Lead to sensitive information.

Description:
An HTML5 cross-origin resource sharing (CORS) policy controls whether and how content running on other domains can perform two-way interaction with the domain that publishes the policy. The policy is fine-grained and can apply access controls per-request based on the URL and other features of the request.
Trusting arbitrary origins effectively disables the same-origin policy, allowing two-way interaction by third-party web sites. Unless the response consists only of unprotected public content, this policy is likely to present a security risk.
If the site specifies the header Access-Control-Allow-Credentials: true, third-party sites may be able to carry out privileged actions and retrieve sensitive information. Even if it does not, attackers may be able to bypass any IP-based access controls by proxying through users' browsers.

Steps To Reproduce:
Proof Of Concept 1:

Request:
GET /dashboard HTTP/1.1
Host: app.upchieve.org
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en-US,en-GB;q=0.9,en;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36
Connection: close
Cache-Control: max-age=0
Origin: https://yiopwxxzxvtf.com

Response:
HTTP/1.1 200 OK
Date: Mon, 17 May 2021 07:37:24 GMT
Content-Type: text/html; charset=utf-8
Connection: close
x-powered-by: Express
access-control-allow-origin: https://yiopwxxzxvtf.com
vary: Origin
access-control-allow-credentials: true
set-cookie: connect.sid=s%3A-B7Wt1PQXUC7BtBz0ulAFKO3Eq5IsYdO.a0e20ezO2zcBQS4j4mlAsPKWaXH71hSNoAL3%2FHZ3P14; Path=/; Expires=Fri, 16 Jul 2021 07:37:24 GMT
cache-control: no-cache,max-age=0
x-envoy-upstream-service-time: 4
CF-Cache-Status: DYNAMIC
cf-request-id: 0a1adb2d6c0000023fdbb9d000000001
Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report?s=Z9CuAhWGEHzcFGQsIdF0YRfLAK1Ian64mv%2Ffzse3iqdbc8uFvvLhy1O3wlv8IKmC%2B8IYGRNG9GSarf%2Buh8xhPpIyAUSAq6T8aJdmau8Db6SX"}],"group":"cf-nel","max_age":604800}
NEL: {"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 650b2e28ae81023f-SJC
Content-Length: 31520

Laporan Referensi: - https://hackerone.com/reports/426165

## Impact

Attacker would treat many victims to visit attacker's website, if victim is logged in, then his personal information is recorded in attacker's server.
If the site specifies the header Access-Control-Allow-Credentials: true, third-party sites may be able to carry out privileged actions and retrieve sensitive information. Even if it does not, attackers may be able to bypass any IP-based access controls by proxying through users' browsers.

## Attachments
No attachments
