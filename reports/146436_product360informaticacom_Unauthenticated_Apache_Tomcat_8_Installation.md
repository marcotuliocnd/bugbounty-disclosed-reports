# [product360.informatica.com] Unauthenticated Apache Tomcat 8 Installation

## Report Details
- **Report ID**: 146436
- **URL**: https://hackerone.com/reports/146436
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-06-22T10:35:09.109Z
- **Disclosed**: 2016-12-08T21:01:25.904Z

## Reporter
- **Username**: zephrfish
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
The consultant identified that the affected url and port leads to an unprotected default Apache X configuration, this service should be protected or removed if not required. The affected link is as follows:

    http://product360.informatica.com:8443/

Upon visiting the URL, the consultant was presented with a default Apache X/Tomcat page, the attached screenshot shows what was displayed.

On it's own this poses no significant risk, however it should still be removed or protected. The consultant attempted to browse to the common Tomcat directories such as /manager and /docs/ however was presented with a standard 404 page. 

The remediation for this would be to ideally either remove the page or apply authentication/restrictions via Apache configuration 

GET Request:

    GET / HTTP/1.1
    Host: product360.informatica.com:8443
    User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-US,en;q=0.5
    Accept-Encoding: gzip, deflate
    Connection: close
    Cache-Control: max-age=0


Response:

    HTTP/1.1 200 OK
    Server: Apache-Coyote/1.1
    Content-Type: text/html;charset=UTF-8
    Date: Wed, 22 Jun 2016 09:58:41 GMT
    Connection: close
    Content-Length: 11408
    
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <title>Apache X</title>
            <link href="favicon.ico" rel="icon" type="image/x-icon" />
            <link href="favicon.ico" rel="shortcut icon" type="image/x-icon" />
            <link href="tomcat.css" rel="stylesheet" type="text/css" />
        </head>
    
        <body>
            <div id="wrapper">
                <div id="navigation" class="curved container">
                    <span id="nav-home"><a href="http://tomcat.apache.org/">Home</a></span>
                    ---SNIP---

## Attachments
- ApacheX.png
