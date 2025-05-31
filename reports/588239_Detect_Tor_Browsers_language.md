# Detect Tor Browser's language

## Report Details
- **Report ID**: 588239
- **URL**: https://hackerone.com/reports/588239
- **State**: Closed
- **Severity**: none
- **Submitted**: 2019-05-23T01:21:29.119Z
- **Disclosed**: 2019-05-29T09:58:51.005Z

## Reporter
- **Username**: ryotak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
#Summary
Some error pages uses Tor Browser's language based text, and iframe can steal it.

#Details
Since the language of Tor Browser is used for the title of the link tag on 404 error page, an attacker can obtain the language of Tor Browser even if the user has set privacy.spoof_english to 2.
I attached a PoC and a video for this.

If the server returns empty response, Tor Browser will show this page in iframe:
```html
<html class="mozwebext">
    <head>
        <link rel="alternate stylesheet" type="text/css" href="resource://content-accessible/plaintext.css" title="Wrap Long Lines">
    </head>
    <body>
        <pre></pre>
    </body>
</html>
```

but if user uses Japanese (This is example, it can be used in other languages) version of Tor Browser, it'll show this page:
```html
<html class="mozwebext">
    <head>
        <link rel="alternate stylesheet" type="text/css" href="resource://content-accessible/plaintext.css" title="長い行を折り返す">
    </head>
    <body>
        <pre></pre>
    </body>
</html>
```

so parent window can steal it:
``` 
title="長い行を折り返す"
```

Maybe there are similar vulnerability in other error page.

## Impact

Attacker can steal language of Tor Browser even if the user has set privacy.spoof_english to 2.

## Attachments
- PoC-binary.jar
- PoC-src.zip
- PoC.mov
