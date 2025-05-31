# Open Redirect in shopify app URL

## Report Details
- **Report ID**: 226408
- **URL**: https://hackerone.com/reports/226408
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-05-05T19:46:13.139Z
- **Disclosed**: 2017-07-21T12:17:59.757Z

## Reporter
- **Username**: pappan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi,

The Amazon Alexa app when installing calls a URL https://assistant-client.meteorapp.com/shopify/callback?code=6aae881ab9c4f12d5b264e6c871a108a&hmac=6109806a12b0439d6a2dce2d547344eb1c2c53e9691259f39eefbb93b9c9c97b&shop=pappuza-2.myshopify.com&timestamp=1494008598

The **shop** parameter will accept any domain and redirects. 
Don't know whether meteorapp.com is controlled by you but reporting this as this found as made by shopify in the app store.

If not going to resolve this, please do not mark as NA. I will do the needful.

## Attachments
No attachments
