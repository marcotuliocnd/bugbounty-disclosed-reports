# Stored XSS in https://productreviews.shopifyapps.com/proxy/v4/reviews/product

## Report Details
- **Report ID**: 168458
- **URL**: https://hackerone.com/reports/168458
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-14T23:26:18.715Z
- **Disclosed**: 2019-11-08T11:03:47.871Z

## Reporter
- **Username**: zombiehelp54
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi , I have found a stored XSS issue in `https://productreviews.shopifyapps.com`
#Details:
Going to `https://productreviews.shopifyapps.com/proxy/v4/reviews/product?product_id=8254331011&version=v4&shop=zh5403-attacker.myshopify.com&_=cache&callback=test` will show you the details of a product with the id `8254331011` in JSON format.
Having the `callback` parameter in the url will return `Content-Type:application/javascript` in the response headers, however, if the url does not contain that parameter, the response won't contain **Content-Type** header in the response so the browser will display the page as **text/html**. 
#PoC:
I have created a product with an XSS payload in the title and added the id in the url.
`https://productreviews.shopifyapps.com/proxy/v4/reviews/product?product_id=8254331011&version=v4&shop=zh5403-attacker.myshopify.com&_=cache&callback=test`

PS: This was originally found at `https://productreviews.shopifycdn.com/proxy/v4/reviews/product?product_id=8254331011&version=v4&shop=zh5403-attacker.myshopify.com&_=xxxxxxxx` but I found that it also works for `https://productreviews.shopifyapps.com`


## Attachments
No attachments
