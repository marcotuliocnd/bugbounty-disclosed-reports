# [oneclickdrsfdc-test.informatica.com] Tomcat Example Scripts Exposed Unauthenticated

## Report Details
- **Report ID**: 147161
- **URL**: https://hackerone.com/reports/147161
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-06-25T11:41:02.922Z
- **Disclosed**: 2016-11-02T19:11:01.780Z

## Reporter
- **Username**: zephrfish
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
#####Issue
The consultant identified that there is an unauthenticated installation of apache tomcat installed on the affected host. This particular installation has the /examples directory exposed which contains several scripts that execute server side code, these scripts can also be leveraged to carry out other attacks.

----------
#####Affected URLs
    https://oneclickdrsfdc-test.informatica.com/examples/servlets/index.html
    https://oneclickdrsfdc-test.informatica.com/examples/jsp/index.html

####Risk: **Medium**
This issue has been marked as medium due to the amount of executable scripts that are available in both the jsp and servlets directories.  Both of which can lead to:

 1. Significant Source Code Disclosure
 2. Significant Information Disclosure

#####Remediaton
Implement http authentication on the affected directories, or alternatively  remove the examples folder entirely to prevent the attack surface.  Consider following a lockdown procedure against the installation and updating Tomcat to a newer instance. 

#####References

 - [OWASP: Securing Tomcat](https://www.owasp.org/index.php/Securing_tomcat)
 - [Apache Tomcat 7 Security Considerations](https://tomcat.apache.org/tomcat-7.0-doc/security-howto.html)
 - [Improving Apache Tomcat Security ](https://www.mulesoft.com/tcat/tomcat-security)

#####Request & Response
GET Request

    GET /examples/jsp/index.html HTTP/1.1
    Host: oneclickdrsfdc-test.informatica.com
    Accept: */*
    Accept-Language: en
    Connection: close

   
Response

    HTTP/1.1 200 OK
    Server: Apache-Coyote/1.1
    Accept-Ranges: bytes
    ETag: W/"16288-1367228170000"
    Last-Modified: Mon, 29 Apr 2013 09:36:10 GMT
    Content-Type: text/html
    Content-Length: 16288
    Date: Sat, 25 Jun 2016 11:39:21 GMT
    Connection: close
    
    ---SNIP---
    -->
    <head>
       <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
       <meta name="GENERATOR" content="Mozilla/4.61 [en] (WinNT; I) [Netscape]">
       <meta name="Author" content="Anil K. Vijendran">
       <title>JSP Examples</title>
    </head>
       ---SNIP---



## Attachments
- oneclick1.png
