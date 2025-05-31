# WebLogic Server Side Request Forgery

## Report Details
- **Report ID**: 300513
- **URL**: https://hackerone.com/reports/300513
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-12-25T21:57:03.064Z
- **Disclosed**: 2019-12-02T19:02:34.799Z

## Reporter
- **Username**: linkks
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Universal Description Discovery and Integration (UDDI) application is publicly available on this WebLogic server. The SearchPublicRegistries.jsp page can be abused by unauthenticated attackers to cause the WebLogic web server to connect to an arbitrary TCP port of an arbitrary host. Responses returned are fairly verbose and can be used to infer whether a service is listening on the port specified. This vulnerability affects Oracle Fusion Middleware 10.0.2, 10.3.6.

The impact of this vulnerability
An attacker can force the WebLogic web server to connect to an arbitrary TCP port of an arbitrary host.

How to fix this vulnerability
Apply the Oracle Critical Patch Update Advisory from July 2014 or restrict access to the UDDI application.

https://blog.gdssecurity.com/labs/2015/3/30/weblogic-ssrf-and-xss-cve-2014-4241-cve-2014-4210-cve-2014-4.html

## Impact

https://███████/uddiexplorer/SearchPublicRegistries.jsp?operator=http://127.0.0.1:80&rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Business+location&btnSubmit=Search

## Attachments
No attachments
