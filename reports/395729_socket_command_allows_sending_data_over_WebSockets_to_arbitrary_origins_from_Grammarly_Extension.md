# `socket` command allows sending data over WebSockets to arbitrary origins from Grammarly Extension

## Report Details
- **Report ID**: 395729
- **URL**: https://hackerone.com/reports/395729
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-08-16T04:25:52.208Z
- **Disclosed**: 2019-07-15T16:34:14.775Z

## Reporter
- **Username**: metnew
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: grammarly

## Vulnerability Information
## Summary

1. Attacker could trigger Grammarly extension's `socket` command using a crafted page to perform WS connection(and data sending) from extension's background page (with cookies and origin) to any URL.
2. Additionally, commands received from the attacker's server are handled by extension and could be used to trigger wrong business-logic behavior (misleading commands) or possibly(!) RCE.

## Description

> Disclaimer: the report is long enough.

### "socket" command vs content script

Next snippet handles "socket" commands received from `window.addEventListener('message')`. 
TL;DR: it sends received "socket" command to the background page.

``` js
function Z(e) {
           var t, n = e.action;
           ...
            "socket" === n && p.emitBackground(b.MessageTypes.client, e),
           ...
        }
```

### "socket" command vs background page

TL;DR: sent "socket" command handled using next snippet, when background page receives it:

``` js
this._onContentScriptSocketMessage = function(e, t, n) { // <-- e = action received from content script
                if (e && !m._getConnectionState().authToCapiDegradation) {
                    var r = e.socketId
                      , o = e.method
                      , i = "close" === o
                      , a = m._sockets[r];
                    if (a || !i) {
                        switch (a || (a = new d.BackgroundSocket(e,n,m._onBackgroundSocketEmit,m._fakeCapi),
                        m._sockets[r] = a), // <-- creates new high-level socket object
                        e.arg && "start" === e.arg.action && m._dialect && (e.arg.dialect = m._dialect),
                        o) {
                        case "connect": // <-- connect method
                            m._refreshUser(!0, "onSessionStart").then(function() {
                                return a.connect(e.arg)
                            });
                            break;
                        case "send":
                            a.send(e.arg); // <-- "send" with an attacker-controllable property as argument
                            break;
                        case "reconnect": <-- Other methods (wsPlay/wsPause/etc.) are under attacker's control too
                            a.reconnect();
                            break;
                        case "release":
                            a.release();
                            break;
                        case "close":
                            a.close();
                            break;
                        case "wsPlay":
                            a.wsPlay();
                            break;
                        case "wsPause":
                            a.wsPause();
                            break;
                        default:
                            p.error("Unknown method", o)
                        }
                        i && (a.close(),
                        a.overrideEmitToNoOp(),
                        delete m._sockets[r])
                    }
                }
            }
```

The final proof that it's possible to connect to any origin  - `connect` method:
``` js
 function E(n) { // <-- e = event received from content script
                w.isConnected() || (A("connect to url: " + e.url),
                t = new u(e.url), // <-- e.url is under attacker's control
                p = !1,
                d = !1,
                t.onopen = function() {
                    g = v,
                    d = !0,
                    h && (h = !1,
                    w.close()),
                    n && e.resetQueueOnReconnect ? b = [] : O(),
                    w.emit("connect"),
                    n && (w.emit("reconnect"),
                    c = !1)
                }
                ,
                t.onmessage = function(t) {
                    s && console.log("%c Received: %s", "color: #46af91;", t.data), // <--- Screencast!
                    S(t.data),
                    function(t) {
                        try {
                            t = JSON.parse(t)
                        } catch (e) {
                            C(e.stack || e, t)
                        }
                        e.useQueue ? (y.push(t),
                        T()) : w.emit("message", t) // <-- t = command could be received from attacker's server
                    }(t.data)
                }
                ,
               ...
}
```

### Websockets 101 (important for understanding)

> Websockets differs from XHRs - As opposite to XHR, CORS doesn't apply to WS.

1. Page could initiate WS connection to any cross-origin resource.
2. There is no browser-level mechanism to prevent WS connection from one origin to another. (like CORS for XHR)
3. Connection through `wss://` includes all user's cookies.

WS server is responsible for validating `Origin` header to check is connection trusted.

#### Example

1. `evil.com` sends XHR to `good.com` = CORS rejects requests (assuming no `Access-Control-Allow-Origin` was specified in response)
2. `evil.com`  connects to `ws://good.com` using WS = server at `good.com` is responsible for `Origin` header validation.

### Attack mechanism

[Page] -> (socket action) -> [Content script] -> (socket action) -> [Background page] -> [WS server]

### Summary [1/3]

Page could exploit "socket" command to :

1. connect to arbitrary WS endpoint from Grammarly extension origin
2. send arbitrary data from Grammarly extension origin to any WS endpoints

### `w.emit("message", t)` [received command vs background page]

You probably noticed this line in `t.onmessage` handler.
Shortly, background page handles events received from remote WS server.
Grammarly uses `wss://capi.grammarly.com/freews` endpoint for text processing.

> I guess "capi" is an abbreviature for Command API.

As of extension could connect to any WS endpoint, it will handle commands received from attacker's endpoint too.

I don't show the full call stack, however, `w.emit("message", commandFromServer)` is handled in this snippet:
``` js
this._onBackgroundSocketEmit = function(e, t, n) { // <-- e = command from attacker's server
                var o = e.event
                  , i = e.socketId
                  , a = e.msg;
                if (p.trace("from ws " + o + " " + i, {
                    msg: a,
                    messageType: t
                }),
                a && a.error && "not_authorized" === a.error)
                    return m._tryToFixSession();
                var c = setTimeout(function() {
                    var e = m._sockets[i];
                    e && (e.release(),
                    e.overrideEmitToNoOp(),
                    delete m._sockets[i])
                }, m._releaseTimeout);
                m._message.emitTo(n, t, r({}, e, { // <-- send command from server to content script
                    id: s.guid()
                }), function(e) {
                    return e && clearTimeout(c)
                })
            }
```

Shortly, `emitTo` emits the command (from attacker's server) from background page to content script.

### Summary [2/3]

Background page:
1. Connects to attacker's WS endpoint 
2. Receives a command from the WS endpoint
3. Handles received command
4. Sends received command to the content script

### \#394518

First of all, #394518 is about user data.
It's possible to get the latest available `socketId` property and send random malformed data to `capi.grammarly.com` under current `socketId`. However, I think it has zero impact :(

### received command vs content script

Received commands handled in next function:
``` js
this._onMessage = function(e, t) {
                var r = n._sockets[e.socketId]; // <-- e.socketId from previous "connect" command
                if (r) {
                    var i = e.msg || {}; // <-- e.msg - msg received from attacker's server 
                    i.action && "error" === i.action.toLowerCase() && n._telemetry.soketCsErrorMsg(i),
                    t("ok"),
                    r.emit(e.event, e.msg) <--- emit "message" event in content script with attacker-supplied command
                }
            }
```

#### `r.emit(e.event, e.msg)`

I was able to call `r.emit(e.event, e.msg)` from the snippet above a few times [No PoC, however, It was documented during research]. 
However, after analyzing listeners of this `emit` (and ancestor calls) I realized the API is too high-level and It can't lead to script execution in the content script.

List of available actions to trigger from server:
```
add: [ƒ]
alert: (2) [ƒ, ƒ]
capiError: [ƒ]
disconnect: (2) [ƒ, ƒ]
finish: (2) [ƒ, ƒ]
finished: [ƒ]
frequent_not_authorized_error: [ƒ]
frequent_runtime_error: [ƒ]
plagiarismChecked: [ƒ]
remove: [ƒ]
sending: [ƒ]
serviceState: [ƒ]
socketConnect: [ƒ]
socketError: [ƒ]
socketFailCount: [ƒ]
socketReconnect: (2) [ƒ, ƒ]
socketReconnectAfterError: [ƒ]
socketStart: (2) [ƒ, ƒ]
start: (2) [ƒ, ƒ]
stats:timing: [ƒ]
submit_ot: [ƒ]
synonyms: [ƒ]
too_many_runtime_error: [ƒ]
```
I didn't test this function call too much.

## Browsers Verified In:

1. Chrome 68.0.3440.106 stable
2. Chrome 70.0.3521.0 canary
3. Grammarly 14.861.1790

## Steps To Reproduce:

#### `localhost:8080`

1. Open `exploit.html`
2. Start server (`npm i ws && node server.js`)
3. Click "Connect to localhost"
4. Check server process logs - "Connection received" logged
3. Click "Send "{"grammarly": "1"}" to localhost" and then "Connect to localhost"
4. Check server process logs - "Message event {"grammarly":"1"}" logged

#### `wss://dox.grammarly.com` origin

1. Click "Connect to dox.grammarly.com from page origin" -> see 403 error in console
2. Click "Connect to dox.grammarly.com from extension"
3. Check "Network" tab in background page's devtools
4. Connection to `dox.grammarly.com` origin was established.

## Supporting Material/References:

Screencast for `localhost:8080` and `ws://dox.grammarly.com` attached.

## Impact

### "connect" + "send" to any origin
Attacker could connect and send data to any WS endpoint from extension origin.
It's not as impactful as #389108 by itself, because of WS policies.

### "connect" + "send" to Grammarly's endpoints
As of Grammarly's WS APIs allows connections from Grammarly extension origin, attacker could send arbitrary data with user's credentials to:
1. `wss://dox.grammarly.com/`
2. `wss://capi.grammarly.com/`
3. And other Grammarly WS endpoints (and Grammarly extension origin "friendly" endpoints, if any)

Example of impactful WS connection: `wss://dox.grammarly.com/documents/<document_id>/ws` - allows editing document with `<document_id>`

### Response handling
As a bonus, it's possible to connect to attacker's WS endpoint, receive data and handle received commands in background page and content script. No PoC or possible exploitation, however, that's potentially a bad behavior.

> I hope Grammarly team could imagine the effort I put into this research :( 
> Set "High" impact, because of arbitrary WS connection + handling of commands received from attacker's server.

## Attachments
- exploit.html
- server.js
- grammarly-ws-socket-action.mp4
