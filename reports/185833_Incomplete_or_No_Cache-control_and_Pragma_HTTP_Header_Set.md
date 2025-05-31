# Incomplete or No Cache-control and Pragma HTTP Header Set

## Report Details
- **Report ID**: 185833
- **URL**: https://hackerone.com/reports/185833
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-11-27T16:22:25.984Z
- **Disclosed**: 2017-03-17T19:01:10.112Z

## Reporter
- **Username**: lulliii
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Hello,
The cache-control and pragma HTTP header have not been set properly or are missing allowing the browser and proxies to cache content.

HTTP/1.1 200 OK
Connection: keep-alive
Server: gunicorn
Date: Sun, 27 Nov 2016 16:18:06 GMT
Content-Type: text/html; charset=UTF-8
X-Gratipay-Version: 2014
Set-Cookie: csrf_token=chYzzQF9UYGunrz4V68ggeuvV6MpTjTZ; expires=Sun, 04 Dec 2016 16:18:06 GMT; Path=/; secure
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
X-Xss-Protection: 1; mode=block
Cache-Control: no-cache
Via: 1.1 vegur

Solution:
Whenever possible ensure the cache-control HTTP header is set with no-cache, no-store, must-revalidate, private; and that the pragma HTTP header is set with no-cache.

## Attachments
No attachments
