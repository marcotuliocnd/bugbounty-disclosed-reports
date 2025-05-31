# Torrent extension: Cross-origin downloading + "URL spoofing" + CSP-blocked XSS

## Report Details
- **Report ID**: 378864
- **URL**: https://hackerone.com/reports/378864
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-07-07T14:50:05.579Z
- **Disclosed**: 2018-09-24T23:40:38.734Z

## Reporter
- **Username**: metnew
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

> \#378809 allows navigating to `chrome-extension://`
> \#378805 allows displaying alert windows on `chrome-extension://` origin

As I said in #378809, navigation to `chrome-extension://` allows attacking dependencies/components of extensions.

Brave has only 3 extensions installed by default (w\o Metamask):
- Brave Sync - according to my observations, it doesn't have vulnerable components
- PDF
- Torrent

### Torrent

#### "Save Torrent File..."

We need alert modal from #378805 to ask a user to click "Save Torrent File" button.
"Save Torrent File" initiates navigation using `a [rel=noopener] [download]` to `location.hash.slice(1)`

#### `http://www.google.com` - "URL spoofing"

Omnibox in Torrent extension displays only `location.hash.slice(1)`. Hence, `chrome-extension://fmdpfempfmekjkcfdehndghogpnpjeno/webtorrent.html#https://www.google.com` will be shown in the address bar as `https://www.google.com`. 
> In reality, it's hard to leverage this bug, but that looks like bad behavior. 

#### `http://www.google.com` - websites downloading

As I said, "Save Torrent File" initiates downloading. CORS page downloads are forbidden.
However, click on "Save Torrent File" in `chrome-extension://fmdpfempfmekjkcfdehndghogpnpjeno/webtorrent.html#https://www.google.com` downloads `www.google.com`.
 
> Because of Torrent extension privileges

#### `file:///etc/passwd` - local files downloading

**URL:** `chrome-extension://fmdpfempfmekjkcfdehndghogpnpjeno/webtorrent.html#file:///etc/passwd`

Click on "Save Torrent File" initiates downloading of local files.
Same "useless URL spoofing". (`file://etc/passwd` in omnibox)

#### `ssh://`

Torrent can't trigger ssh sessions without confirmation (like privileged `about:blank`). Not interesting.

#### `javascript:` - CSP-blocked XSS

The most interesting case. 
**URL:** `chrome-extension://fmdpfempfmekjkcfdehndghogpnpjeno/webtorrent.html#javascript:alert()`
As of `a` element initiates navigation, it's possible navigating to `javascript:` URI to initiate code execution.
Unfortunately, this XSS is blocked by CSP :(

## Products affected: 

Brave: 0.23.31 
V8: 6.7.288.46 
rev: 3148acef36dba0fce89108638bb27927c4937f90 
Muon: 7.1.5 
OS Release: 17.6.0 
Update Channel: Release 
OS Architecture: x64 
OS Platform: macOS 
Node.js: 7.9.0 
Brave Sync: v1.4.2 
libchromiumcontent: 67.0.3396.103

## Steps To Reproduce:

1. Start ftp server (sample ftp server attached, `npm i ftpd && node ftp-server.js`)
2. Open ftp://localhost:7002/exploit.html

## Impact

An attacker could init an alert modal to trick the user into pressing "Save Torrent file" button using #378805.

It's possible to download local files and files from the web (websites too) using "Save Torrent file" in Torrent extension (requires user gesture).

It's also possible to initiate CSP-blocked XSS by clicking on "Save Torrent File".

## Attachments
- ftp-server.js
- exploit.html
