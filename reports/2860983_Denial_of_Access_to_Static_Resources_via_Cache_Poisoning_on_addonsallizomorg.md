# Denial of Access to Static Resources via Cache Poisoning on addons.allizom.org

## Report Details
- **Report ID**: 2860983
- **URL**: https://hackerone.com/reports/2860983
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-11-23T00:50:17.228Z
- **Disclosed**: 2025-01-08T10:39:30.045Z

## Reporter
- **Username**: jabiyev
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mozilla

## Vulnerability Information
## Summary:
An attacker can poison the cache and block access to static files (e.g., image, JS) that are delivered with the homepage. 

## Steps To Reproduce:

To reproduce cache poisoning for an image file: 

  1. `curl -H "X-HTTP-Method-Override: HEAD" https://addons.allizom.org/static-server/img/addon-icons/default-64.d144b50f2bb8.png?dontpoisoneveryone=1`
  2. Visit https://addons.allizom.org/static-server/img/addon-icons/default-64.d144b50f2bb8.png?dontpoisoneveryone=1 to see it is not accessible anymore.

To reproduce cache poisoning for a JS file: 

For example, `/static-frontend/amo-6203ce93d8491106ca21.js` is one of the JS files delivered with the homepage. We did not find a way to safely test (i.e., using `?dontpoisoneveryone=1`), since it does not include the query string as a part of the cache key. However, we noticed that the `X-HTTP-Method-Override: HEAD`header is honored in the same way.

1. `curl -s https://addons.allizom.org/static-frontend/amo-6203ce93d8491106ca21.js/notexist` (see the error message in the response body)
2.  `curl -s -H "X-HTTP-Method-Override: HEAD" https://addons.allizom.org/static-frontend/amo-6203ce93d8491106ca21.js/notexist` (see the empty response body)

## Supporting Material/References:
Behind the scenes, the origin server honors the X-HTTP-Method-Override header and treats the request as a HEAD request. Therefore, it generates a "200 OK" response with an empty body, which gets cached and as a result the resource becomes unavailable for all users. To learn more about the attack, you can read the document listed below.

  * https://cpdos.org/#HMO

## Impact

## Summary:

An attacker can make static resources such as images and JS files that are delivered with the homepage inaccessible to all users.

## Attachments
No attachments
