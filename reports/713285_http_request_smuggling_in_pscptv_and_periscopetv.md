# http request smuggling in pscp.tv and periscope.tv

## Report Details
- **Report ID**: 713285
- **URL**: https://hackerone.com/reports/713285
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-10-13T19:22:23.338Z
- **Disclosed**: 2020-09-10T22:52:57.208Z

## Reporter
- **Username**: protostar0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Description:** 
the Description of HTTP request smuggling attacks : [here](https://portswigger.net/web-security/request-smuggling)

seems that many subdomains in pscp.tv and periscope.tv vulenrable

##1-Detect HTTP request smuggling attack [504 response with delay (30 s, 60s)] "DoS"

POC & Steps To Reproduce: in this video F606648
Resource: [https://portswigger.net/web-security/request-smuggling/finding] 


##2- [exploit HTTP request smuggling attack ] send two request as one request get two response as one response [low impact]
POC & Steps To Reproduce & impact : in this video F606663
**ps:**
-add the two CRLFs in the end of the second request in GET REQUEST.
-use the valid value of content-length in POST REQUEST.

##3-[exploit HTTP request smuggling attack ]  poison the VICTIM request

POC & Steps To Reproduce & impact : in this video
inject a get request to the victim request F606689 
inject a get request to the victim request F606704 
**ps:**
-don't add the two CRLFs in the end of the second request in GET REQUEST.
-use large value in content-length then the length of request body in POST REQUEST.
Resource:
[exploit] (https://portswigger.net/web-security/request-smuggling/exploiting)

## important:
on a live site with a high volume of traffic like [www.pscp.tv] .it can be hard to prove request smuggling exists without exploiting numerous genuine users in the process.
-in the poc F606704  , i edit the victim request  to my post request `editing the description of my account` and ignore the real victim request. and the description  will change.

## Impact

1-dos
2-bypass csrf token & inject cookie  allow to link attacker account with [google,twitter] victim account
  report : https://hackerone.com/reports/704489
see other impact in 
https://portswigger.net/web-security/request-smuggling/exploiting

## Attachments
- HTTPsmugReq_dos.mp4
- http_smug_2_requ_2resp_.mp4
- http_smug_get_request_.mp4
- http_smug_post_request_.mp4
