# XSS on www.mapbox.com/authorize

## Report Details
- **Report ID**: 143220
- **URL**: https://hackerone.com/reports/143220
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-05T18:00:42.415Z
- **Disclosed**: 2017-08-14T17:19:52.016Z

## Reporter
- **Username**: stefanovettorazzi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mapbox

## Vulnerability Information
Description
---
When you don't include the parameter __client_id__ in the request to the endpoint at https://www.mapbox.com/authorize/, the template __template-modal-unauthorized__ (included in the client code of the endpoint)  is rendered with the value of the parameter __redirect_uri__ sent in the request without escaping:
```html
Code at https://www.mapbox.com/authorize/
<% if (obj.redirect) { %>
      <div class='fill-gray pad2y pad4x center'>
        <a href='<%= obj.redirect %>' class='button col12 close'>Back</a>
      </div>
<% } %>
```
```javascript
Code at https://www.mapbox.com/authorize/authorize.js
}).fail(function(err) {
        Views.modal.show('unauthorized', {
            msg: err.statusText,
            redirect: (App.param('redirect_uri')) ?
                App.param('redirect_uri') :
                false
        });
});
```
The problem is that you can pass any value to __redirect_uri__ and it is going to be added as HTML code, which allows to break the `<a>` element using a `'` and a `>`.

Reproduction
---
Load the following URL on Chrome, Firefox, Safari, Internet Explorer 11, or Edge.
```
https://www.mapbox.com/authorize/?redirect_uri=%27%3E%3Csvg%20onload=%27alert%28document.domain%29%27%3E
```
I'm going to share a link to the video in a comment, because the size is greater than 10MB.

---

Let me know if you need more information.

## Attachments
No attachments
