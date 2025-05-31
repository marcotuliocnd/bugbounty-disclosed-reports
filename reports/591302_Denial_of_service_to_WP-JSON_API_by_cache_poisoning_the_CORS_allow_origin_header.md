# Denial of service to WP-JSON API by cache poisoning the CORS allow origin header

## Report Details
- **Report ID**: 591302
- **URL**: https://hackerone.com/reports/591302
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-05-28T08:24:13.932Z
- **Disclosed**: 2020-04-16T11:47:55.468Z

## Reporter
- **Username**: nathand
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
The WP-JSON implementation on some wordpress.com websites I've tested is vulnerable to denial of service where by an attacker can provide an arbitrary `Origin` header in the request, which is then echoed back in the response via the `Access-Control-Allow-Origin` header, which is cached and served to other requests.

This response header is used by browsers to determine whether the requesting origin (if it is a cross origin request) is allowed to read the response in the request. In the event the victim website had another origin that used the WP-JSON API to request data from their wordpress.com site (e.g. a sub domain), this cache poisoning would deny access to such requests due to failed a CORS access control check. It appears that this vulnerability is only a concern if the WP-JSON API responses are cached, which you can determine by the presence of a `X-Cache: hit` header in the response.

## Proof of concept

For this test, I'm going to target `█████████.com`, a wordpress.com site. I will be doing this with a cache busting technique that doesn't really poison the live site's cache (by supplying a bespoke query string value) so this should be safe to repeat verbatim.

  1. First, open a HTTPS website - it doesn't matter which website, as long as it isn't `https://█████████.com` (to trigger browser CORS). For my test, I used my own website https://nathandavison.com.
  1. Open the javascript console and execute the following 5-10 times (to make sure the cache is poisoned across backends): `fetch('https://██████████.com/wp-json/?dontreallypoison1').then(res => res.json()).then(json => console.log(json))`
  1. Now, open another HTTPS website - it also doesn't matter which site it is, as long as it too isn't `https://███████.com`. Execute the same fetch as above.
  1. You should now experience a CORS error in your browser, such as: `Cross-Origin Request Blocked: The Same Origin Policy disallows reading the remote resource at https://█████████.com/wp-json/?dontreallypoison1. (Reason: CORS header ‘Access-Control-Allow-Origin’ does not match ‘https://nathandavison.com’).`

What's going on here? because the WP-JSON response is CORS aware, it is responding with a `Access-Control-Allow-Origin` header value. Presumably to offer wide support for CORS, the `Origin` value in the request is being echoed back. So far, I believe this is standard Wordpress WP-JSON behavior. However, automattic/wordpress.com is caching this response and is not keying the cache based on the request `Origin` value (which is `https://nathandavison.com` in step 1 above), so therefore is serving the poisoned response in step 4, and because the other origin is not `https://nathandavison.com`, CORS in the browser blocks the response coming back into the DOM.

I believe any wordpress.com website that caches WP-JSON responses is vulnerable to this. A quick way, as an attacker, to find potential victims would be a query like this:

https://publicwww.com/websites/%22If%20you're%20reading%20this,%20you%20should%20visit%20automattic.com%22/

## Attach scenario

To attack this, a victim site would have to:

  1. Use WP-JSON is a meaningful way in a browser context (or any other context that respects CORS headers)
  1. Use it from an origin that triggers CORS. For example, if the WP-JSON API is used on "foo.████.com" to request the blog posts from "█████.com". Another example may be a "headless" Wordpress site (e.g. api.x.com is Wordpress and x.com is the frontend, which uses the WP-JSON plugin to interact with the WP backend).

Once a target is found that satisfies these conditions, an attacker would then simply poison the CORS response with regular requests to specific endpoints. This poisoning would result (in the example above) in visitors to "foo.██████.com" failing to load the WP-JSON API requests to "██████████.com" due to CORS failures, causing a DoS for whatever service relies on this functionality.

## Fix

I believe to fix this, automattic should make sure that edge caches for WP-JSON requests are using the `Origin` header in the request to key the cache, so one value can't affect the cache served to another value. Preventing the echoing back of the `Origin` into the `Access-Control-Allow-Origin` response header without first passing through a configurable whitelist would also be a potential solution, but this may be harder to implement. 

## More information

Please see the following blog post for more information on this:

https://nathandavison.com/blog/corsing-a-denial-of-service-via-cache-poisoning

I wrote this post in response to disclosing a very similar vulnerability to another Wordpress SaaS provider.

## Impact

The impact of this vulnerability depends on how and where a client uses the WP-JSON plugin. If a wordpress.com customer uses WP-JSON in a context that relies on CORS, this technique could deny service to the WP-JSON endpoints in use.

## Attachments
No attachments
