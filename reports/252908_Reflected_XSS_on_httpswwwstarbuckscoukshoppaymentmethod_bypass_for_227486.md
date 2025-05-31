# Reflected XSS on https://www.starbucks.co.uk/shop/paymentmethod/ (bypass for 227486)

## Report Details
- **Report ID**: 252908
- **URL**: https://hackerone.com/reports/252908
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-07-24T08:14:25.062Z
- **Disclosed**: 2020-06-16T21:19:02.783Z

## Reporter
- **Username**: bayotop
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
Hi guys,

I am now able to prove my concerns from #227486 (see my last comment). `"`s are still not correctly encoded when rendered into the page in the `<link rel="canonical" href="current_full_url" />` element on almost any https://starbucks.co.uk/ page.

The WAF is bypassed by encoding `"`s as `%2522` in the URL path. This won't work when the payload is part of the query string.

**Description**

Take a look on the source code of https://www.starbucks.co.uk/shop/card/egift/anthing%2522. You can see a quote is injected to break the `href` attribute context.

```html
<link rel="canonical" href="https://www.starbucks.co.uk/shop/card/egift/anthing"" />
```

**Exploitation**

Using the same tricks as described in #227486 this injection can be leveraged to achieve arbitrary JS execution on `/shop/paymentmethod/`. Also note that this is just **one** example and more ways may exist to achieve JS execution. Steps to reproduce (use **Firefox**):

1. Login at https://www.starbucks.co.uk and add a card into basket on https://www.starbucks.co.uk/shop/card/egift/birthday
2. Visit https://www.starbucks.co.uk/shop/paymentmethod/hkjhk%2522onclick=%2522confirm(/-/g+this.ownerDocument.domain)%2522id=%2522checkoutButton
3. Click somewhere around the Checkout header. 
4. An alert showing the current domain pops up.

**Recommendation**

Again, correctly encode the URL before reflecting it back in the response. 

In #227486 the fix was blocking requests containing `%u0022` in the query string. This was shown to be bypassable so fixing this issue by blocking `%2522` in URL paths could be bypassed again in future. 



## Attachments
No attachments
