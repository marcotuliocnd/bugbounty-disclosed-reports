# Unrestricted access to Eureka server on ██████

## Report Details
- **Report ID**: 304240
- **URL**: https://hackerone.com/reports/304240
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-01-12T09:30:34.962Z
- **Disclosed**: 2018-02-06T12:49:33.773Z

## Reporter
- **Username**: reptou
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: grab

## Vulnerability Information
Hi Grab Security Team, 

First of all, best wishes for 2018, empty of bugs if possible ;-) 

**Summary:** I found that the following endpoint is hosting Netflix Eureka Server █████ and that even if some URLs are requiring authentication (401 code for some of thems like /metrics for example), it is still possible to send requests to the REST API. 

**Description:** I think that this is a test infrastructure, however the dashboard some applications registered on Netflix Eureka server (please see screenshot attached "███") which targets private EC2 instance (nothing published on the Internet) are visible. 

Digging a little bit shows that Netflix provides a REST API described here :

```
https://github.com/Netflix/eureka/wiki/Eureka-REST-operations
```
I tried some requests and it seems that it does not require any kind of authentication. I prefer to do some tests that could not lead to any disruption (even if this seems to be a test infrastructure), but for example the following request returns 200 :

```
PUT ████████HTTP/1.1
Host: ██████myteksi.net
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Connection: close
Upgrade-Insecure-Requests: 1
```
And the response is the following 

```
HTTP/1.1 200 
Date: Fri, 12 Jan 2018 09:17:36 GMT
Content-Type: application/xml
Content-Length: 0
Connection: close
Server: Tengine/2.2.1
```

Following the description of the REST API, I think that an attacker could modify any propertie regarding the current instances registered or even register a new one with his own settings. As I am not sure if there is some production behind, I choose to report it directly without doing any modification on the current systems. 

## Browsers Verified In:

N/A

## Steps To Reproduce:

  1. Go to █████████ for the dashboard access (read only)
  1. Issue for example the above HTTP requestand check the server response (or any of the requests described in Netflix documentation)

## Supporting Material/References:

  * List any additional material (e.g. screenshots, video, logs, etc.)

Please let me know your thoughts,

Kind regards,

Reptou

## Impact

From my perspective, this could help an attacker registers his custom AWS EC2 instance into an application and make it part of the service load balancing provided by Eureka.

## Attachments
No attachments
