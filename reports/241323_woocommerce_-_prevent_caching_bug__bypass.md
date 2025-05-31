# woocommerce - prevent_caching() bug / bypass

## Report Details
- **Report ID**: 241323
- **URL**: https://hackerone.com/reports/241323
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-06-19T13:42:48.428Z
- **Disclosed**: 2017-09-16T07:52:21.202Z

## Reporter
- **Username**: b258ea62bf297b02afa9854
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
As guest visit the following links and look at the headers. Yup there are not caching headers in the response. 
(https://woocommerce.com/.cart/)[https://woocommerce.com/.cart/]
(https://woocommerce.com/+cart/)[https://woocommerce.com/+cart/]
(https://woocommerce.com/-cart/)[https://woocommerce.com/-cart/]

```
accept-ranges:bytes
age:0
content-encoding:gzip
content-type:text/html; charset=UTF-8
date:Mon, 19 Jun 2017 13:25:20 GMT
link:<https://woocommerce.com/wp-json/>; rel="https://api.w.org/"
link:<https://woocommerce.com/?p=18552>; rel=shortlink
server:nginx
set-cookie:woocommerce_items_in_cart=1; path=/
set-cookie:woocommerce_cart_hash=c670f81df612aa5e067bc7d1a33673da; path=/
set-cookie:wp_woocommerce_session_241766cd983ad3375c92fb5411ecef50=159536bf377374fa447e91a16437e611%7C%7C1498051468%7C%7C1498047868%7C%7Cbfae081ff1a2c69f9e4feda8128c7579; expires=Wed, 21-Jun-2017 13:24:28 GMT; Max-Age=172748; path=/
status:200
x-cache:pass
x-hacker:If you're reading this, you should visit automattic.com/jobs and apply to join the fun, mention this header.
x-pingback:https://woocommerce.com/xmlrpc.php
x-rq:vie1 87 24 3240
```
What happens?

Function `prevent_caching()` in the `class-wc-cache-helper.php` have the following line of code:
```
if ( stristr( trailingslashit( $_SERVER['REQUEST_URI'] ), $uri ) ) {
```
in order to protect the `cart`, `my-account` and `checkout` dynamic pages from being cached by caching wordpress plugins ( defines the caching constants ) or cloud proxies (sets no caching headers).

But from the wordpress itself we got the following e.g. pagename query param is passed trough `sanitize_title_with_dashes` and only thing left for successful exploitation/attack in case of woocomerce instance remains to defeat the `redirect_canonical` which is bypassed by `-`, `+` and `.` characters. This means that $_SERVER['REQUEST_URI'] will have this type of value `/+my-account/` and needle will be `/my-account/`  and this will return false ofc. :)

This way in case of existing caching plugin set up to cache the wordpress pages even for logged in users, woocommerce store that allows guests to buy products or some another cases of web setups cache  deception  attack is ready to go. 

Fix: Don't rely on the `$_SERVER['REQUEST_URI']` param, but use it query object to get the pagename.

## Attachments
No attachments
