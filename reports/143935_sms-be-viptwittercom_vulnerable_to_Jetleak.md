# [sms-be-vip.twitter.com] vulnerable to Jetleak

## Report Details
- **Report ID**: 143935
- **URL**: https://hackerone.com/reports/143935
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-09T18:41:45.085Z
- **Disclosed**: 2018-04-02T18:13:04.670Z

## Reporter
- **Username**: molejarka
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Version of Jetty installed on sms-be-vip.twitter.com (9.2.6.v20141205) is vulnerable to Jetleak.
Jetleak allows to read arbitrary data from previous requests submitted to the server by other users.

More information about Jetleak here:
https://blog.gdssecurity.com/labs/2015/2/25/jetleak-vulnerability-remote-leakage-of-shared-buffers-in-je.html 

Tool to check Jeleak:
https://github.com/GDSSecurity/Jetleak-Testing-Script

Below sample HTTP request and response:
GET / HTTP/1.1
Host: sms-be-vip.twitter.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:46.0) Gecko/20100101 Firefox/46.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
DNT: 1
Connection: close

HTTP/1.1 200 OK
Date: Thu, 09 Jun 2016 18:31:04 GMT
Content-Type: text/html; charset=ISO-8859-1
Connection: close
Server: Jetty(9.2.6.v20141205)

<html>
 <head>
  <title>Stratus.025: Welcome</title>
  <style type="text/css">
   h1, p, table, a, body { font-family: Helvetica,Verdana,Arial; font-size: 11px; }
   h1 { font-size: 13px; font-weight: bold; }
   table { border: solid 1px #999999; border-collapse:collapse; empty-cells: show; padding:2px; }
   th { font-weight: bold; background-color:#666666; color:#FFFFFF; text-align: left; }
   th, td  { border-collapse:collapse; border: solid 1px #999999; }
   tr.queue  { background-color:#F5F5F5; }
   tr.warn  { background-color:#FF9090; }
  </style>
 </head>
 <body>
<h1>Stratus.025</h1>
 </body>
</html>


## Attachments
No attachments
