#  SQL Injection on cookie parameter

## Report Details
- **Report ID**: 761304
- **URL**: https://hackerone.com/reports/761304
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-12-18T21:54:24.783Z
- **Disclosed**: 2020-05-03T08:58:13.945Z

## Reporter
- **Username**: w31rd0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
Hello team. It seams one of the parameters in the cookies is vulnerable to SQL injection. Below requests has the lang parameter in cookies. If you inject one quote mark like '. You get SQL error with the syntax. By injecting a second you have the error removed.
I did not attempt to exfiltrate data as this is obvious indication of SQLi.

```
GET /index.php/search/default?t=1&x=0&y=0 HTTP/1.1
Host: mtn.com.ye
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: PHPSESSID=86ce3d04baa357ffcacf5d013679b696; lang=en'; _ga=GA1.3.1859249834.1576704214; _gid=GA1.3.1031541111.1576704214; _gat=1; _gat_UA-44336198-10=1
Upgrade-Insecure-Requests: 1
```

I would like to ask for permission for further exploiting this issue.

## Impact

Web application is vulnerable to SQL injection, allowing access to data

## Attachments
- SQLi.png
