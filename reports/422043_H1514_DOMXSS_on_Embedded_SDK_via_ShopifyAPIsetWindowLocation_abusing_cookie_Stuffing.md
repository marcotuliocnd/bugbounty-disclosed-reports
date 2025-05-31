# H1514 DOMXSS on Embedded SDK via Shopify.API.setWindowLocation abusing cookie Stuffing

## Report Details
- **Report ID**: 422043
- **URL**: https://hackerone.com/reports/422043
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-10-10T09:31:18.935Z
- **Disclosed**: 2019-04-17T14:40:38.473Z

## Reporter
- **Username**: filedescriptor
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi Team!

I'm reporting a rather unusual DOMXSS that allows an attacker to perform a XSS attack on any Shopify apps that use the Embedded SDK. To exploit this, several techniques were chained together: Cookie Stuffing -> Login CSRF -> (Not Open) Redirect -> DOMXSS.

#Details
Inspired by #381192, I decided to check all pages to see if there's any broken origin validation. The results were frustrating since they all seemed to be done properly. However I noticed embedded apps did it in a way that it verifies if the coming origin is the logged-in store. Say if I am an admin on foobar.myshopify.com, then an embedded app will check if in-coming messages originate from https://foobar.myshopify.com. I went ahead to look up some [documentations](https://help.shopify.com/en/api/embedded-apps/embedded-app-sdk/initialization), confirming this is by design (`shopOrigin`):

```javascript
ShopifyApp.init({
  shopOrigin: 'https://CURRENT_LOGGED_IN_SHOP.myshopify.com'
[...]
```

Now this is interesting because by design we can execute any JavaScript on our own stores. That means, I can iframe an embedded app on my store, then post any message to it and it will accept it. So I quickly beautify the SDK source code to see if there's any interesting event. Checking common DOMXSS sinks I found that it registers the `Shopify.API.setWindowLocation` event that navigates to a said destination.

https://cdn.shopify.com/s/assets/external/app.js
```javascript
e.setWindowLocation = function(e) {
    return window.location = e
}, e.bindWindowLocation = function() {
    return _Shopify.Messenger.addHandler("Shopify.API.setWindowLocation", function(e) {
        return function(t, n) {
            return e.setWindowLocation(n)
        }
    }(this))
}
```

By navigate to a *javascript:* pseudo URL it can lead to XSS. This can be verified by opening any embedded apps and execute the following code in the DevTools' console
```javascript
$$('iframe')[0].contentWindow.postMessage('{"message":"Shopify.API.setWindowLocation","data":"javascript:alert(document.domain);0[0]"}','*')
```
{F358299}

**However this XSS is almost useless** because the embedded app is authenticated as us, the attacker. When we try to exploit it on a victim it won't work because they are not logged into our store. So you could say this is, a self DOMXSS. Well, almost. 

What if we use Login CSRF to force a victim to be logged into our store? After the victim is logged in to our store, we can then instruct user's browser to log into the embedded app as us by navigating to `/admin/oauth/authorize`. Then the current logged in store will be ours. I came up with an idea to stuff the session cookies using JavaScript.

The session cookies consist of `_secure_admin_session_id` and `_master_udr`. While I could simply write `_secure_admin_session_id` with `docuemnt.cookie` API, I realized a problem with `_master_udr`. Unlike `_secure_admin_session_id`, `_master_udr` is scoped to `.myshopify.com`. If we triy to write our `_master_udr`, then this will happen:

```http
GET https://canvasfoobar.myshopify.com/admin/oauth/authorize?client_id=d25e45407e508f96409c2dd796e9bd95&redirect_uri=https%3A%2F%2Fscript-editor.shopifycloud.com%2Fauth%2Fshopify%2Fcallback&response_type=code&scope=write_scripts%2Cread_products%2Cread_customers&state=a HTTP/1.1
Host: canvasfoobar.myshopify.com
Cookie: _master_udr=LEGIT; _master_udr=EVIL; _secure_admin_session_id=EVIL
```

The legitimate `_master_udr` will override our evil one and the server will refuse to authenticate as us. There is a trick fortunately. 

>“Cookies with longer paths are listed before cookies with shorter paths.” –RFC 6265

By setting a cookie with a very specific (`/admin/oauth` in this case) we can outrun the original one. The code that we will use to force a login will be:

```javascript
document.cookie = '_secure_admin_session_id=EVIL;path=/admin/oauth';
document.cookie = '_master_udr=EVIL;path=/admin/oauth';
```

Another problem is even after all this, the victim will be logged into the embedded app **as us**. That means, all actions only affect our store. 

To solve this we can simply relog in the victim to the embedded app. Since the victim is still logged in their store, we can navigate the victim to https://victim.myshopify.com/admin/oauth/authorize to trigger the auth flow for the embedded app. The drawback is we need to know which store the victim is logged in as. Luckily https://www.shopify.com/path will redirect to the last logged in store of a user, therefore navigating to https://www.shopify.com/admin/oauth/authorize will lead them to https://victim.myshopify.com/admin/oauth/authorize.

Eventually we have our XSS running on the embedded app's domain running with the victim's session.

#Steps to Reproduce

In the PoC, Script Editor will be used as an example.

1. Be logged into your store as an admin and have [Script Editor](https://apps.shopify.com/script-editor) installed
2. Navigate to https://canvasfoobar.myshopify.com/products/canary
3. After the iframe turns grey, click it
4. After a while, a fake modal dialog will show up and a *New Script* will be created

I'm also attaching a video demo.

#Fix

I recommend fixing this issue by validating the URL for `Shopify.API.setWindowLocation`. The other small issues are by design so they are hard to fix.

## Impact

Perform unauthorized actions on a store admin on any embedded apps.

## Attachments
- Screen_Shot_2018-10-10_at_2.58.16_PM.png
- shopify-embedded-sdk-xss.mov
