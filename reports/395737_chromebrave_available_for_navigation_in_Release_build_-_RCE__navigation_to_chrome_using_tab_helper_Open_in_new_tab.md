# `chrome://brave` available for navigation in Release build [-> RCE] + navigation to `chrome://*` using tab_helper ["Open in new tab"]

## Report Details
- **Report ID**: 395737
- **URL**: https://hackerone.com/reports/395737
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-08-16T04:53:51.685Z
- **Disclosed**: 2018-09-25T00:23:34.580Z

## Reporter
- **Username**: metnew
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

### `chrome://brave` is available for navigation

Navigation to `chrome://brave` + `<local_file_path>` requires local file at `<local_file_path>`.

The file loaded in this context has access to **private Muon APIs** such as `chrome.ipcRenderer/remote/webFrame/webViewRequest`.

Muon API allows executing code on the device. (e.g. with `chrome.remote.require('child_process').exec`)

> In addition, Brave isn't sandboxed (on all OS).

That's clearly a vulnerability, not a feature:
1. it's in Release channel, not in Debug builds
2. Could lead to RCE

> Note: attacker knows the correct `<local_file_path>` after loading the file from `file://` origin (`window.location.pathname`).

### Navigation to `chrome://brave`

I've already shown the way to navigate to `file://` URLs in  #369218, which was fixed in 0.23.80.

>  I mentioned in the report that it's possible navigating to `chrome://` URLs too in #369218. However, [the fix](https://github.com/brave/browser-laptop/pull/14973) was incomplete. It only works for `about:` and `file:`URLs.

### PoC

1. Shows that `<webview>` works
2. Launches `Calculator.app` on macOS

## Products affected: 
 
Brave: 0.23.79 (0.23.80 and 0.23.100 too, where #369218 is patched)
V8: 6.8.275.24 
rev: 51b49051a779f0db94fbcfd0df5faca781299ea0 
Muon: 8.0.7 
OS Release: 17.7.0 
Update Channel: Release 
OS Architecture: x64 
OS Platform: macOS 
Node.js: 7.9.0 
Brave Sync: v1.4.2 
libchromiumcontent: 68.0.3440.84

## Steps To Reproduce ||  Attack Scenario:

1. Download `exploit.html`
2. Open link in the file using "Open in new tab"
3. The new tab opens with private `<webview>` tag + `Calculator.app` starts

## Patch

Preventing navigation to `chrome://brave` origin seems ok.

### Additional resources

Screencast attached.

## Impact

Crafted HTML file allows executing code on the device. 

> Requires user gesture - "Open in a new tab". Set impact to "High", because requires downloading the file.

## Attachments
- exploit.html
- brave-chrome-brave-new-tab.mp4
