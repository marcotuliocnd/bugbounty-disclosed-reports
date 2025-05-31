# XSS in express-useragent through HTTP User-Agent

## Report Details
- **Report ID**: 362702
- **URL**: https://hackerone.com/reports/362702
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-06-06T11:28:49.469Z
- **Disclosed**: 2018-07-06T13:34:36.850Z

## Reporter
- **Username**: b9b86c2fc8409c628fb3de6
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hello, 

I would like to report an XSS in express-useragent  module  due  a lack of validating User-Agent header. Please note I already created an [Github issue](https://github.com/biggora/express-useragent/issues/98) and asked for CVE ( [CVE-2018-9863](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-9863)). I did not know about Node.js third-party modules on hackerone.

## Description
express-useragent is simple NodeJS/ExpressJS middleware exposing User-Agent details to your application and views. Basically it parses User-Agent and return it in structured JSON format.

## The issue
while parsing User-Agent there are no escaping or sanitization mechanism. User-Agent header is controlled by the user. An attacker can craft a malicious script and inject it through the HTTP header.

## Steps to reproduce
* git clone https://github.com/biggora/express-useragent 
* cd express-useragent
* ```node test/http.js```  (an HTTP server should listen on 3000 tcp)
* ```curl "http://localhost:3000" -H 'User-Agent: <script>alert("XSS")</script>' > poc.html```
* open poc.html with your favorite web browser
* you should see an alertbox popup 

### Proof of concept (screenshots)
{F305913}
{F305914}

### Proof of concept with a fix (video) {F305912}

## Mitigation
Correctly escape and sanitize user input ( HTTP User-Agent ). Please note I proposed a fix in the video

## Impact

An attacker could execute javascript code that could lead to XSS.

## Attachments
- express_useragent_xss.mkv
- Screenshot_from_2018-04-09_18-50-35_(1).png
- Screenshot_from_2018-04-09_18-51-21_(1).png
