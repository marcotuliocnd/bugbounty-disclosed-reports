# http request smuggling in  twitter.com

## Report Details
- **Report ID**: 715996
- **URL**: https://hackerone.com/reports/715996
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-10-16T23:54:00.683Z
- **Disclosed**: 2020-11-18T00:25:13.213Z

## Reporter
- **Username**: protostar0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Summary:**
the same vulnerability reported in other domain , see this report [here](https://hackerone.com/reports/713285) 
**Description:** 
the Description of HTTP request smuggling attacks : [here](https://portswigger.net/web-security/request-smuggling)

##Detect HTTP request smuggling attack (subdomains vulnerable):
-to detect HTTP request smuggling attack with add header `Transfer-Encoding: chunked` 
and encode the body of request with chunked encode.
1. send request with a valid chunked encode and you will get response means that the **back-end server accept chunked encode**
2. send a large value in hex of chunked encode , if get ** delay of response**  means its vulnerable. 
resource: https://portswigger.net/web-security/request-smuggling/finding

## CONFIRMATION:

##POC:

in this POC i will use TWEET request as second request (payload) ,means that if the HTTP request smuggling attack success,
will get a new TWEET in my account 

F609847


## Steps To Reproduce:


ps : i use chrome browser,with burp
1- choose any valid POST request (or change GET to POST) from twitter.com and send it to repeater
2- delete this header (Connection: close  ,Accept-Encoding: gzip, deflate)
3- add this header <Transfer-Encoding: chunked>

4- add chunked encode    put a valid chunked code or   [ put just 0 with two CRLFs]
5-put the second request  [i use a TWEET request ]
6- send the attacker request

## Impact

impact of http request smuggling 
- https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn
- https://portswigger.net/web-security/request-smuggling/exploiting

## Attachments
- twitter_HTTP_SMUG_POC.mp4
