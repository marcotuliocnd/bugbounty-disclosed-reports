# Cache purge requests are not authenticated

## Report Details
- **Report ID**: 1994585
- **URL**: https://hackerone.com/reports/1994585
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-05-19T19:34:19.879Z
- **Disclosed**: 2023-05-20T15:10:42.419Z

## Reporter
- **Username**: dhananjay09
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:

Hello team,
Anyone can issue a PURGE request for any resource and invalidate your caches. That can lead to increased bandwidth costs but also potential Denial of Service attacks.

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1.{Fundefined}

Unauthenticated cache purge request:

 curl 'https://curl.se/' -X PURGE
{ "status": "ok", "id": "21729-1683784658-593921" }  
  2.{Fundefined}
  

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]
https://sapt.medium.com/apple-hall-of-fame-for-a-small-misconfiguration-unauth-cache-purging-faf81b19419b

## Impact

That can lead to increased bandwidth costs but also potential Denial of Service attacks

## Attachments
No attachments
