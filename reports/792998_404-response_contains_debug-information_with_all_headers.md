# 404-response contains debug-information with all headers

## Report Details
- **Report ID**: 792998
- **URL**: https://hackerone.com/reports/792998
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-02-11T08:34:34.732Z
- **Disclosed**: 2020-05-16T07:56:41.796Z

## Reporter
- **Username**: p4fg
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

When requesting a page that does not exist under `www.hackerone.com` the page returns a hidden HTML-element `#debugData` that reflects all headers in the GET-request, including http-only cookies.

**Description:**

This in itself is not a serious vulnerablity, but as the program description mentions, the site runs drupal and probably have an administrative interface somewhere. If (when) an XSS is found on the domain, this page can be used to fetch all cookies for an administrator and take over their session on the site.

The response does not have `X-Frame-Options` or CSP so it can be read over a iframe on the same domain.

### Steps To Reproduce

1. Visit `https://www.hackerone.com/resources/read/ajax_issueWidgets_p4fg` using a browser
2. View source of the recieved data


### Supporting Material

Sent GET-request (with added headers and cookies to prove the point):

```
GET /resources/read/ajax_issueWidgets_p4fg HTTP/1.1
Host: www.hackerone.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: ███ super_secret_made_up_cookie=VERY_VERY_SECRET
Upgrade-Insecure-Requests: 1
X-HackerOne-Research: p4fg
X-Other-Custom-Header: WILL_BE_REFLECTED
```


The response (cut to show relevant portions):

```
HTTP/1.1 404 Not Found
Date: Tue, 11 Feb 2020 08:29:55 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
P3p: CP="NOI ADM DEV PSAi COM NAV OUR OTRo STP IND DEM"
Referrer-Policy: unsafe-url
X-Content-Type-Options: nosniff
X-Xss-Protection: 1; mode=block
CF-Cache-Status: DYNAMIC
Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Server: cloudflare
CF-RAY: 5634f5362977d147-GOT
Content-Length: 6334

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
    	<title>Page Not Found (404)</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">        <link href="https://fonts.googleapis.com/css?family=Lato:300|Montserrat:300,400" rel="stylesheet" type="text/css">
    	<style>
			body, html {margin:0;background:#252525;}
            body{padding:7% 20%;font-family: "Montserrat",sans-serif;}
			h1{color:#4b4b4b;font-size:55px;margin:0 0 8px;font-weight:400;}
            div{border-top:1px solid #4b4b4b;width: 40px;height:1px;margin:0 0 45px -20px;}
            h2{color:#fff;font-size:22px;margin-bottom:12px;font-weight:300;}
            p{color:#ddd;font-size:18px;margin-bottom:60px; font-family: "Lato",sans-serif;font-weight:300}
		</style>
    </head>          
    <body>
		<h1>404</h1>
        <div></div>
        <h2>Hey, we can't find what you're looking for...</h2>
        <p>The requested URL doesn't exist.</p>
        <pre id="debugData" style="display: none;">
            {
    &quot;headers&quot;: {
        &quot;Host&quot;: &quot;www.hackerone.com&quot;,
        &quot;User-Agent&quot;: &quot;Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit\/605.1.15 (KHTML, like Gecko) Version\/12.1.1 Safari\/605.1.15&quot;,
        &quot;Accept&quot;: &quot;text\/html,application\/xhtml+xml,application\/xml;q=0.9,image\/webp,*\/*;q=0.8&quot;,
        &quot;Accept-Encoding&quot;: &quot;gzip&quot;,
        &quot;Accept-Language&quot;: &quot;en-US,en;q=0.5&quot;,
        &quot;Cdn-Loop&quot;: &quot;cloudflare&quot;,
        &quot;Cf-Connecting-Ip&quot;: &quot;109.228.159.19&quot;,
        &quot;Cf-Ipcountry&quot;: &quot;SE&quot;,
        &quot;Cf-Ray&quot;: &quot;5634f5362977d147-BOS&quot;,
        &quot;Cf-Visitor&quot;: &quot;{\&quot;scheme\&quot;:\&quot;https\&quot;}&quot;,
        &quot;Cookie&quot;: &quot;███ super_secret_made_up_cookie=VERY_VERY_SECRET&quot;,
        &quot;Upgrade-Insecure-Requests&quot;: &quot;1&quot;,
        &quot;X-Forwarded-For&quot;: &quot;109.228.159.19, 172.68.54.33&quot;,
        &quot;X-Forwarded-Host&quot;: &quot;www.hackerone.com&quot;,
        &quot;X-Forwarded-Port&quot;: &quot;443&quot;,
        &quot;X-Forwarded-Proto&quot;: &quot;https&quot;,
        &quot;X-Hackerone-Research&quot;: &quot;p4fg&quot;,
        &quot;X-Other-Custom-Header&quot;: &quot;WILL_BE_REFLECTED&quot;,
        &quot;X-Real-Ip&quot;: &quot;172.68.54.33&quot;
    },
    &quot;requestMethod&quot;: &quot;GET&quot;,
    &quot;requestedUrl&quot;: &quot;\/resources\/read\/ajax_issueWidgets_p4fg&quot;,
    &quot;host&quot;: &quot;www.hackerone.com&quot;,
    &quot;baseHubUrl&quot;: &quot;https:\/\/www.hackerone.com\/resources&quot;,
    &quot;currentPageRequest&quot;: &quot;https:\/\/www.hackerone.com\/resources\/read\/ajax_issueWidgets_p4fg&quot;,
    &quot;https&quot;: true,
    &quot;timestamp&quot;: &quot;2020-02-11T03:29:55-05:00&quot;
}        </pre>
    </body>
</html>

```

## Impact

This could be an essential part in escalating a future XSS to session takeover for the site.

## Attachments
No attachments
