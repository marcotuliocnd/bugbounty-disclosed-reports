# Unauthenticated cache purging

## Report Details
- **Report ID**: 1911568
- **URL**: https://hackerone.com/reports/1911568
- **State**: Closed
- **Severity**: none
- **Submitted**: 2023-03-18T07:27:54.041Z
- **Disclosed**: 2023-05-01T14:22:42.505Z

## Reporter
- **Username**: mr_prey3r
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: fastly-vdp

## Vulnerability Information
## Summary:
I found a vulnerability in https://fanout.io/ page known  as unauthenticated cache purging vulnerability. This vulnerability arises when cache purging requests are available to the unauthenticated users. 

## Steps To Reproduce:

  1. Go to any terminal of an OS which has curl installed in it.
  2. Type in the following command `curl --head https://fanout.io/` and hit enter. You will see that there are these following HTTP headers available
```http
via: 1.1 varnish
age: 7
x-served-by: cache-qpg1234-QPG
x-cache: HIT
x-cache-hits: 1
```
  3. This means that the page is caching the requests. So to reproduce the bug or to exploit it, type `curl -X PURGE https://fanout.io/` and in the response you'll see `{ "status": "ok", "id": "1237-1678993092-222436" }` (the id can be changed in your case)
This response proves that this endpoint is vulnerable to unauthenticated cache purging.

## Supporting Material/References:
F2235408

## Impact

In general, cache purging vulnerabilities can have a high severity level because they can allow an attacker to manipulate the cache of a web application, which can lead to various types of attacks such as website defacement, unauthorized access to sensitive data, or denial of service (DoS) attacks.

## Attachments
- 2023-03-18_12-55-20.mp4
