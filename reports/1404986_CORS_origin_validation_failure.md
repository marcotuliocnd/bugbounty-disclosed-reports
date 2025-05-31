# CORS origin validation failure

## Report Details
- **Report ID**: 1404986
- **URL**: https://hackerone.com/reports/1404986
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-11-19T08:01:01.849Z
- **Disclosed**: 2021-12-07T20:24:29.425Z

## Reporter
- **Username**: jupiter-47
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: upchieve

## Vulnerability Information
Hi team,

I hope you are doing well on the other side.

## Summary:

I found that ```https://hackers.upchieve.org/``` is using cross-origin resource sharing in an insecure way. The web application fails to properly validate the Origin header and returns the header Access-Control-Allow-Credentials: true. This means that any website can issue requests with **user credentials** and read the response.

## Steps To Reproduce:

1- intercept the request to any path in the vulnerable asset.
2- modify the origin header as such:

```
GET / HTTP/1.1
Origin: https://hackers.upchieve.org.evil.com
Cookie: connect.sid=s%3AjSy6_1N-Y3zG4zqifYrsos2idZrkZePH.%2BjgtEn3a1wuxhiDk86FMXfhg0bPYfJ2jGxytqmA%2BU7Q
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Encoding: gzip,deflate
Host: hackers.upchieve.org
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36
Connection: Keep-alive
```
3- you can see that our input is reflected in this header and also with credentials being true:

Access-Control-Allow-Origin: https://hackers.upchieve.org.evil.com
Access-Control-Allow-Credentials: true

```
HTTP/1.1 200 OK
Date: Fri, 19 Nov 2021 07:09:54 GMT
Content-Type: text/html; charset=utf-8
Connection: keep-alive
content-security-policy: base-uri 'self';block-all-mixed-content;connect-src 'self' https://p.upchieve.org https://gitlab.com https://*.ingest.sentry.io https://api.cdnjs.com upc-photo-ids.s3.us-east-2.amazonaws.com upc-session-photos.s3.us-east-2.amazonaws.com https://js-agent.newrelic.com https://bam.nr-data.net https://www.googletagmanager.com https://www.google-analytics.com https://uptime.gleap.io https://api.gleap.io https://gitlab.com/api/v4/feature_flags/unleash/23285197 wss://hackers.upchieve.org https://hackers.upchieve.org;default-src 'self' https://hackers.upchieve.org 'unsafe-inline' https://player.vimeo.com https://docs.google.com https://upc-training-materials.s3.us-east-2.amazonaws.com;font-src 'self' https: data:;img-src 'self' https://www.googletagmanager.com https://www.google-analytics.com upc-photo-ids.s3.amazonaws.com upc-photo-ids.s3.us-east-2.amazonaws.com upc-session-photos.s3.amazonaws.com upc-session-photos.s3.us-east-2.amazonaws.com https://cdn.upchieve.org data: blob: https://hackers.upchieve.org;object-src 'none';script-src 'self' https://hackers.upchieve.org https://www.googletagmanager.com https://www.google-analytics.com https://cdn.upchieve.org https://cdnjs.cloudflare.com https://p.upchieve.org https://js-agent.newrelic.com https://bam.nr-data.net https://code.jquery.com https://stackpath.bootstrapcdn.com https://cdn.jsdelivr.net https://widget.gleap.io 'unsafe-eval' 'unsafe-inline';script-src-attr 'none';style-src 'self' https: 'unsafe-inline';upgrade-insecure-requests
x-dns-prefetch-control: off
expect-ct: max-age=0
strict-transport-security: max-age=15552000; includeSubDomains
x-download-options: noopen
x-content-type-options: nosniff
x-permitted-cross-domain-policies: none
referrer-policy: no-referrer
x-xss-protection: 0
access-control-allow-origin: https://hackers.upchieve.org.evil.com
vary: Origin
access-control-allow-credentials: true
cache-control: no-cache,max-age=0
x-envoy-upstream-service-time: 5
CF-Cache-Status: DYNAMIC
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=RbNq71MjvFkD73NP7L%2BRtM80b%2FkHNNrdCWZZ7QofiEKovAmLhlpbbu5u%2BcN4q7n%2FJDHbVl%2FKllDdX9HPJa6cNJzqPkIHm7LT0N%2FLVfi2afRLlXVUcoLO7hebszLvwq32GslRcJ9w"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6b079d9dfbb441d4-AMS
Original-Content-Encoding: gzip
Content-Length: 31614
```

Note: we could bypass filtering with this method -> prefix origins are accepted (www.example.com trusts example.com.evil.com).

## Impact

I tried to sign up for an account, but it seems that the process is complicated, and I also don't live in the US. I'm sure that after signing in, I can exploit the misconfiguration and obtain session cookies to takeover the account. Furthermore, I have tried on every possible unauthenticated path I can get to, and they are all vulnerable.

Kind regards,

-@Jupiter-47

## Attachments
No attachments
