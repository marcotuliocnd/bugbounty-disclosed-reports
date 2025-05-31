# No rate limiting - Create data

## Report Details
- **Report ID**: 1047100
- **URL**: https://hackerone.com/reports/1047100
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-11-30T14:47:50.445Z
- **Disclosed**: 2021-01-05T12:13:17.206Z

## Reporter
- **Username**: ofjaaaah
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripo

## Vulnerability Information
## Summary:

Hello team Stripo, how are you?

I found a rate limit for data creation.

Target = https://my.stripo.email/cabinet/#/my-services/298427?tab=data-sources

Request to Post:

```
POST /emailformdata/v1/amp-lists?projectId= HTTP/1.1
Host: my.stripo.email
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json;charset=UTF-8
Cache-Control: no-cache
Pragma: no-cache
Expires: Sat, 01 Jan 2000 00:00:00 GMT
X-XSRF-TOKEN: 3ef1a2b8-f640-457b-bac8-1d629d0f9498
Content-Length: 198
Origin: https://my.stripo.email
Connection: close
Referer: https://my.stripo.email/cabinet/
Cookie: amplitude_id_246810a6e954a53a140e3232aac8f1a9stripo.email=eyJkZXZpY2VJZCI6ImU1NjAwZjk3LTFiY2QtNDIzOS1iZTczLWNmNWVhYmMzMTJkZFIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTYwNjc0NjU3NzcwMCwibGFzdEV2ZW50VGltZSI6MTYwNjc0Njg1ODg3OCwiZXZlbnRJZCI6MCwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjB9; _pin_unauth=dWlkPU1UUTFZemczWlRFdE1HSXdOeTAwT1Rrd0xUbGxNVEl0TWpBeE16WmpZVE00WlRZNA; _ga=GA1.2.730792257.1605012362; _pin_unauth=dWlkPU1UUTFZemczWlRFdE1HSXdOeTAwT1Rrd0xUbGxNVEl0TWpBeE16WmpZVE00WlRZNA; G_ENABLED_IDPS=google; __stripe_mid=e5538cc4-3896-4b96-b703-711ef38535d3313b41; _ga=GA1.3.730792257.1605012362; _gid=GA1.2.1102057235.1606746578; __stripe_sid=fcbc15d6-fe33-41ca-bd12-ad2a6fd80eb5a7fc3c; token=eyJhbGciOiJSUzUxMiJ9.eyJhdXRoX3Rva2VuIjoie1widXNlckluZm9cIjp7XCJpZFwiOjI5NDA3NyxcImVtYWlsXCI6XCJqYWFhaGJvdW50eUBnbWFpbC5jb21cIixcImxvY2FsZUtleVwiOlwicHRcIixcImZpcnN0TmFtZVwiOlwic2NyaXB0XCIsXCJsYXN0TmFtZVwiOlwiYm91bnR5XCIsXCJmYWNlYm9va0lkXCI6bnVsbCxcIm5hbWVcIjpudWxsLFwicGhvbmVzXCI6W10sXCJhY3RpdmVcIjp0cnVlLFwiZ3VpZFwiOm51bGwsXCJhY3RpdmVQcm9qZWN0SWRcIjoyOTg0MjcsXCJzdXBlclVzZXJWMlwiOmZhbHNlLFwiZ2FJZFwiOlwiY2JlOWMzMjItMDNhNS00NzQxLTlkMjYtNTc3MTc1MGI0M2MwXCIsXCJvcmdhbml6YXRpb25JZFwiOjI5MzgxNCxcIm93bmVkUHJvamVjdHNcIjpbMjk4NDI3XSxcImZ1bGxOYW1lXCI6XCJzY3JpcHQgYm91bnR5XCJ9LFwiaXNzdWVkQXRcIjoxNjA2NzQ2NjIwODUxLFwiYXBpS2V5XCI6bnVsbCxcInByb2plY3RJZFwiOm51bGwsXCJ4c3JmVG9rZW5cIjpcIjNlZjFhMmI4LWY2NDAtNDU3Yi1iYWM4LTFkNjI5ZDBmOTQ5OFwiLFwicm9sZVwiOlwiQ0FCSU5FVF9VU0VSXCIsXCJhdXRob3JpdGllc1wiOltdfSIsImV4cCI6MTYwNjgzMzAyMH0.qRAbnSN-DZWyUTUezJREviXpSgK1o_8U-3Rgt0xioXjID4apoWkfmPjt0vSnMcTRiF3oNLZmLC2FqnnMlMqqZb_v1Pv9Dn_gHSWOAF2s9IHn0tfJVPPh0BMTxDYfcFlvfMnGz9DMx7v4ETv7PJcSUwDBlFCMXcQ-kEa0AcSjOj7edpMJ2T18Xje3MgLx0Iq_u44HhYWxMaclL8FisL6Dqa13hQKijlCiV-H_jJSxEGpHgtUE0RPBI7kmWSMdW6flncHdf43S7An15uNxe6Dq6dbkuP3wpO_nO6IwNJLcxnt6s9_-ETCHXZIjMuNTKTs5zi0GoOA1OJ_8A1kCkN2cGal5ghD3fKpC4Slk5HkriZCHSvGf7tBgWJY7JCWCNMvucuKsUAeDjucFxB-wscr7iX6q6huJpCsa8gNNL_qR6PzwYF1kHuBRPTHCtF_PEcuqnc6LGfe9mCe6khdfGDKELGoTg8FtjZ-ce84oIhNLOSajzkJ3pbQ2vXB8B3Sm4lkjU85RzTMYhrNAF0zz6ZOzYqShg-QG60Yr66i07OcUXbw66R0ZH8YmH-ildoRtoJKNyloEuVMi-mz-KYZcRda1GHdBX-iEMto3ZXW7YL08DjdM9y07f0GnsSY_lBr_--nq73PxFd415D1sduoKkTDoSzOYIGT3dBK2D2PXpxiUUTs; _gid=GA1.3.1102057235.1606746578; JSESSIONID=A774ECEC8E8D7FB9527BC02A723054F8; intercom-session-b1m243ec=VWpock85SEcyYnRMZlVJcms0N1VCelVvdXd5b0J6eTFEWFh1QWIrZUpzSUlwbW8yT2RpdnZJamRnM3JtL3QrNi0tSVpVekFtR0s5c3RYV29MOGg5OUpQdz09--5e28d4d448f59bec98135e9bf373ff2ad64ab50d; _gat_UA-96386569-1=1

{"projectId":298427,"name":"ukibxiv4daehs7wdnupej63kgbm1aq.burpcollaborator.net","description":"ukibxiv4daehs7wdnupej63kgbm1aq.burpcollaborator.net","url":null,"identifier":null,"sourceType":"JSON"}
```
Thanks @OFJAAAH

## Impact

The attacker can charge the application, creating massively.

## Attachments
- stripo2.png
- stripo1.png
