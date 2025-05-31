# The authenticity_token can be reversed and used to forge valid per_form_csrf_tokens for arbitrary routes

## Report Details
- **Report ID**: 732415
- **URL**: https://hackerone.com/reports/732415
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-11-08T14:03:47.855Z
- **Disclosed**: 2020-08-27T16:25:50.354Z

## Reporter
- **Username**: jregele
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
When `per_form_csrf_tokens` is set to `true`, each form should protected against CSRF with a unique token that is not predictable by an attacker. The`per_form_csrf_token` is generated using a HMAC SHA-256 using a key that is exposed in a reversed `authenticity_token`. The `authenticity_token` is a Base64 encoding of

`one_time_pad | (one_time_pad XOR session[:csrf_token])`

Because the `one_time_pad` is the first half of the `authenticity_token`, it is not secret and an attacker can reverse the token to learn `session[:csrf_token]`.

From there the attacker can forge a hash for an arbitrary route (e.g. /articles/2):
`HMAC ( session[:csrf_token], "/articles/2#patch")`

To reproduce:
1. Have two Rails routes that accept only per form csrf tokens
2. Validate that the `authenticity_token` sent in the POST data returns an HTTP 422 when sent in the other form
3. Forge a per form token with the attached exploit script
   - the `authenticity_token` parameter is taken from the <meta> tag in the header of any page for the session
   - the `route` parameter is the action of the target HTML form (e.g /articles/2)
   - the `method` parameter is the value from `_method` parameter sent in the POST data (e.g. patch)
4. Take the forged token from the exploit script, URL-encode it, and send it as the `authenticity_token` in the POST data. For reliability, ensure that:
   -  the route parameter matches the endpoint,
   - the `_method` parameter in the POST data matches what used for `method` in the exploit script
   - the forged `authenticity_token` in the POST data is properly URL-encoded

## Impact

Exploitation allow an attacker to forge valid per-form CSRF tokens even in hardened situations where the global `authenticity_token` itself is not allowed.

For the attack to be successful, an attacker would need a valid global `authenticity_token`. This can be extracted out of a web page without any protections that cookies have (such as HTTP-Only). An attacker could leverage an XSS vulnerability to bypass per-form CSRF on unrelated pages. Because the token can be forged for any form, code execution on a page without forms could still lead to attackers bypassing CSRF protections of forms related to password changes, deletion of data, creation of new users, etc.

## Attachments
- perform_csrftoken_forgery.py
