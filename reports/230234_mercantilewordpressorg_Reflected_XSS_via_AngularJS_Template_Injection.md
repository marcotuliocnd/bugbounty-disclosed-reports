# [mercantile.wordpress.org] Reflected XSS via AngularJS Template Injection

## Report Details
- **Report ID**: 230234
- **URL**: https://hackerone.com/reports/230234
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-05-20T13:56:49.092Z
- **Disclosed**: 2017-06-14T18:35:23.938Z

## Reporter
- **Username**: ysx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
Hi,

By injecting a crafted AngularJS payload into the `search` endpoint on the WordPress Swag Store, it was possible to achieve reflected XSS further to resolved report #221893.

I came across a potential exploitation vector after noticing that a search query for `{{2*2}}` returned `4` in the site title response.

## Conditions Verified In
* Firefox 52.0.3 – stable
* Safari 10.1 – stable

## Proof of Concept URL
```
https://mercantile.wordpress.org/search/{{constructor.constructor('alert(document.domain)')()}}
```

## Screenshot

{F186517}

Thanks!

## Attachments
- Mercantile_XSS.png
