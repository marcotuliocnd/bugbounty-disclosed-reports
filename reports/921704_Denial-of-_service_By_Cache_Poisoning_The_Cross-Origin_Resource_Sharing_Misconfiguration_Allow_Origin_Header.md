# Denial-of- service By Cache Poisoning The Cross-Origin Resource Sharing Misconfiguration Allow Origin Header

## Report Details
- **Report ID**: 921704
- **URL**: https://hackerone.com/reports/921704
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-07-12T21:41:43.002Z
- **Disclosed**: 2020-08-14T19:53:32.516Z

## Reporter
- **Username**: hannanhaseeb
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summery:

The `wp-json` implementation on some WordPress websites I've tested is vulnerable to Denial-of-service where by an attacker can provide an arbitrary origin header in the request, which is then echoed back in the response via the `Access-Control-Allow-Origin` header, which is cached and served to other requests. This response header is used by browsers to determine whether the requesting origin is allowed to read the response in the request. In the event the victim website had another origin that used the `wp-json` API to request data from their WordPress site, this cache poisoning would deny access to such requests due to failed a Cross-Origin Resource Sharing access control check. It appears that this vulnerability is only a concern if the `wp-json` API responses are cached, which you can determine by the presence of a `X-Cache: hit` header in the response.

## Description:

How does this lead to a Denial-of-service? Well, consider the possibility that this WordPress site is the back end of a headless or decoupled CMS style web application. While custom frontends unrestricted by the CMS theming engine are used as the presentation layer to the user, and communication between the two is often achieved via some sort of API and front end JavaScript framework pairing. What I have been requesting above is one such API, and it turns out WordPress has had this REST like JSON API called `wp-json` API inbuilt into its core package since v4.7, so you could say out of the box WordPress is ready to be used as a headless CMS. If by some chance the front end of the application in question happens to sit in a different origin than the WordPress site for instance www.site.com for the frontend and www.api.site.com for the WordPress instance, then the front end would require Cross-Origin Resource Sharing to be configured to allow it access to `wp-json` API, and this cache poisoning vulnerability could impact the availability of such an application, as the mismatch between a legitimate origin value in a request compared to the attacker's poisoned `Access-Control-Allow-Origin` value in the response will result in an error like in the following screenshot.

## Steps To Reproduce:

For this test, I'm going to target [site](https://en.instagram-brand.com/wp-json), a WordPress site. I will be doing this with a cache busting technique that doesn't really poison the live site's cache by supplying a bespoke query string value so this should be safe to repeat verbatim.

* First open an HTTPS website, it doesn't matter which website, as long as it trigger browser Cross-Origin Resource Sharing. For my test, I used this [website](https://www.shawarkhan.com/).
* Open the JavaScript console and execute the following command 5 to 10 times to make sure the cache is poisoned across back end. You can also do this Burp Suite by sending request multiple times.

```javascript
fetch('https://en.instagram-brand.com/wp-json/').then(res => res.json()).then(json => console.log(json))
```

* Now, open another HTTPS website, it also doesn't matter which site it is, as long as it's execute the same fetch as above.
* You should now experience a Cross-Origin Resource Sharing error in your browser console while fetching.
* What's going on here? because the `wp-json` response is Cross-Origin Resource Sharing aware, it is responding with a` Access-Control-Allow-Origin` header value. Presumably to offer wide support for Cross-Origin Resource Sharing, the origin value in the request is being echoed back. So far, I believe this is standard WordPress` wp-json` behavior. However, WordPress is caching this response and is not keying the cache based on the request origin value, so therefore is serving the poisoned response, and because the other origin is not previous one, Cross-Origin Resource Sharing in the browser blocks the response coming back into the Document Object Model.

## Reference:

Please click on the following blog post [link](https://nathandavison.com/blog/corsing-a-denial-of-service-via-cache-poisoning) and report [link](https://hackerone.com/reports/591302) with the same issue for more information.

## Mitigation:

I believe to fix this you should make sure that edge caches for `wp-json` requests are using the origin header in the request to key the cache, so one value can't affect the cache served to another value. Preventing the echoing back of the Origin into the `Access-Control-Allow-Origin` response header without first passing through a configurable white list would also be a potential solution, but this may be harder to implement.

## Impact

The impact of this vulnerability depends on how and where a client uses the `wp-json` plugin. If a WordPress customer uses `wp-json` in a context that relies on Cross-Origin Resource Sharing, this technique could deny service to the  `wp-json` endpoints in use.

## Attachments
- Screencast_07-12-2020_02_57_09_PM.webm
