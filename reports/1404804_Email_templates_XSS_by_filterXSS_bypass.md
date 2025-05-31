# Email templates XSS by filterXSS bypass

## Report Details
- **Report ID**: 1404804
- **URL**: https://hackerone.com/reports/1404804
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-11-19T01:19:30.319Z
- **Disclosed**: 2022-05-25T07:45:26.623Z

## Reporter
- **Username**: caue
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: judgeme

## Vulnerability Information
## Summary:
`js-xss` is used to prevent XSS on email templates previews but the custom `onIgnoreTag` function can be used to bypass this filter. This leads to a Self-XSS scenario that can be used to achieve Account Takeover in 1-click.

```js
onIgnoreTag: function (e, t) {
   return "!--[if" === e || "![endif]--" === e || "<!-->" === t ? t : void 0; 
},
```

## XSS

The way how `js-xss` parse tags starting with `<![` differ from how browser parse it, so it's possible to abuse this in this way:
```html
<![endif]-- onerror="<![endif]-->" onload="<img src=1 onerror='alert(1)' />">
```
Sending this as the HTML email template will trigger an XSS when the email is previewed. Since email templates are private and only the owner of the template can preview it, this can be considered a Self-XSS. But there is a way to do another user preview it, leading to an account takeover in 1-click.
We can use HMAC authentication feature to force another user login in our account and preview the malicious email:
```
https://www.judge.me/shop/emails/2243518/edit?no_iframe=1&shop_domain=wordpress.caueo.me&platform=woocommerce&hmac=████
```
This URL authenticates as admin on `wordpress.caueo.me` domain, where the malicious email will be. The HMAC hash is created on this way (taken from wordpress plugin):
```php
$hmac       = hash_hmac( 'sha256', "no_iframe=1&platform=woocommerce&shop_domain={$domain}", $token, false );
```

Having this XSS with the victim logged in my account is possible to leak HTML content of a page that was loaded with victim's account cookie:

1. Load an iframe with the victim's page (HTML content to leak) - Authenticated as victim
2. Load another iframe with the XSS (Use HMAC authentication) - Authenticated as me
3. We can use the XSS to read `parent.frames[0]` HTML content since it is same-origin

## CSP bypass
At a first sight we can't load an iframe to victim's page, since it has a CSP that whitelists iframe origins:
```
frame-ancestors https://wordpress.caueo.me http://wordpress.caueo.me wordpress.caueo.me https://woocommerce-adapter.judge.me/ *.judge.me
```
To bypass it we can use the XSS to load the iframes, but we need to do it on another subdomain, because to trigger this XSS is needed to login in my account and then it would not be possible to load the victim's page authenticated as victim's account later. So we trigger the XSS on `www.judge.me` subdomain.

## Limitation to 0-click account takeover
At this point it is already **possible to read HTML content of almost any page authenticated as victim**. To achieve account takeover we only need to get the private API token from victim because it is used as the key of HMAC authentication.
The problem is that the endpoint that retrieves the API private token checks if the `Referer` header starts with `https://judge.me/settings`, so is not possible to load this endpoint in an iframe.

## Clickjacking
We can load an iframe to `https://judge.me/settings` where has a button that retrieves the API token from the endpoint successfully. So it is possible to perform a clickjacking to that button, and if the victim clicks on it, we can get the API private token. 

## PoC
I made a PoC on how is possible to perform this account takeover with user interaction and leak some stuffs without user interaction.
[PoC](https://www.judge.me/shop/emails/2243518/edit?no_iframe=1&shop_domain=wordpress.caueo.me&platform=woocommerce&hmac=█████████)

In this PoC I leaked FreshChat token without clickjacking, so we can impersonate another user in support chat without needing a user click.

## Impact

Shop account takeover (user interaction)
Impersonation on support chat
Private content leak

## Attachments
No attachments
