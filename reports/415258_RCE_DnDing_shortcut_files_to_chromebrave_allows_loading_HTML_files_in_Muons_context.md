# RCE: DnDing shortcut files to chrome://brave allows loading HTML files in Muon's context

## Report Details
- **Report ID**: 415258
- **URL**: https://hackerone.com/reports/415258
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-09-27T11:45:41.134Z
- **Disclosed**: 2018-10-22T20:12:43.978Z

## Reporter
- **Username**: metnew
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

> \#395737 has shown that Brave supports `chrome://brave/<local_file>` URLs.
> The Brave team introduced a patch which blocks navigation to `chrome://brave` and removed `chrome.remote.require` to prevent command execution on the machine.

### Navigation to `chrome://brave` via shortcut files

> ~~From my understanding:~~

1. Brave allows DnDing files
2. DnD of shortcut files is handled on Chromium-level (shortcut files : e.g., `.webloc` on macOS or `.desktop` on Linux) 
3. DnDing a shortcut => navigation to URL the file points to.

This approach allows navigating to `chrome://brave/` origin.

#### Attack requirements

- The victim has to dnd a shortcut file to a tab
- Attacker needs **MITM** OR **local reflected XSS** OR an attacker-supplied **HTML file which absolute path** is known.

> MITM is the easiest way so far.

### Local files reading

Yeah, reading local files from `chrome://brave` is possible.
The same PoC as in #390362, but the origin is `chrome://brave`:

``` html
<head>
    <!-- Local files reading -->
    <script>
        function show() {
            var file = link.import.querySelector('body')
            alert(file.innerHTML)
        }
    </script>
    <link id="link" onload="show()" rel="import" as="document" href="chrome://brave/etc/passwd">
</head>
```

### `ipcRender` and `ipcMain`

HTML file loaded in `chrome://brave/` context has access to private APIs, like `ipcRenderer` and `ipcMain`:

``` js
let ipcMain = chrome.remote.getBuiltin('ipcMain')
let ipcRenderer = chrome.ipcRenderer
```

Sending arbitrary IPC commands -> full control over the browser.
**RCE through arbitrary IPC commands:** #188086 (includes PoC)

Impact: UXSS, URL spoofing, changing browser settings, etc.

### `chrome.remote.getBuiltin(module)`

Sending arbitrary IPC commands is a serious problem, but the impact isn't limited to it.

`chrome.remote.getBuiltin(module)` returns `electron[module]`.
``` js
// Alias to remote.require('electron').xxx.
binding.getBuiltin = function (module) {
  return metaToValue(ipcRenderer.sendSync('ELECTRON_BROWSER_GET_BUILTIN', module))
}
```

It's possible to leverage this func to obtain some "hidden" modules like `autoUpdater`, `Tray`, `protocol` and other.

#### Running attacker's executables on machine (download `.terminal` via IPC + <lack-of-quarantine> + `chrome.shell.openExternal`)

IPC allows doing many damaging things and possibly running shell commands too.

But there is an alternative way for an RCE:
1. IPC downloads a `.terminal` file from the web
2. #374106 - `.terminal` files could execute shell commands without `-x` permission
3. `chrome.remote.shell.openExternal` opens downloaded `.terminal` file
4. Commands from `.terminal` get executed

> No PoC provided, since the impact is already apparent, but could make it if required

#### Persistence

I'm sure, it's clear for the Brave team that it allows an attacker to persist on the device via changing browser settings.
However, I want to highlight that `chrome.remote.getBuiltin(module)` allows accessing `protocol` module, which allows:

```js
registerBufferProtocol: (...)
registerHttpProtocol: (...)
registerNavigatorHandler: (...)
registerServiceWorkerSchemes: ƒ ()
registerStandardSchemes: (...)
registerStringProtocol: ƒ ()
```

### MITM in Brave

- `chrome://brave` is always vulnerable to MITM even when HTTPSE is active
- `file://` is vulnerable to MITM, when HTTPSE is inactive

> Not sure whether HTTPSE is turned on by default.
> As far as I know, HTTPS Everywhere isn't enabled by default.

## Products affected: 

Brave: 0.24.0 
V8: 6.9.427.23 
rev: f657f15bf7e0e0c50a2b854c6b05edb59bfc556c 
Muon: 8.1.6 
OS Release: 17.7.0 
Update Channel: Release 
OS Architecture: x64 
OS Platform: macOS 
Node.js: 7.9.0 
Brave Sync: v1.4.2 
libchromiumcontent: 69.0.3497.100

## Steps To Reproduce:

### PoC for shortcut navigation

1. Open any page in Brave
2. DnD `etc-passwd.webloc` file to Brave
3. Brave opens `chrome://brave/etc/passwd` showing `/etc/passwd` file in `chrome://brave` origin's context

### Exploit (macOS)

-1. Make sure to stop `httpd` on macOS
0. Insert next line into your `/etc/hosts`: `127.0.0.1 maps.googleapis.com`
1. `sudo node server.js` - starts MITM server
2. Open any page in Brave
3. DnD `exploit.webloc` file
4. Opened page shows an alert with `/etc/passwd` contents + working `<webview>` tag  + starts `Calculator.app`

## Supporting Material/References:

Screencast attached.

## Impact

A remote attacker with a MITM access (or specific conditions like reflected XSS on `file:///` origin) could send arbitrary IPC commands(trigger RCE) when a user drag-n-drops 
crafted shortcut file into Brave.

## Attachments
- chrome-brave.webloc
- etc-passwd.webloc
- server.js
- brave-dnd-shortcut-chrome-brave-origin.mp4
