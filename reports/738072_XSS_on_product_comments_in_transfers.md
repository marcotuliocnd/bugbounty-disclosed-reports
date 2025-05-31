# XSS on product comments in transfers

## Report Details
- **Report ID**: 738072
- **URL**: https://hackerone.com/reports/738072
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-11-15T06:24:31.708Z
- **Disclosed**: 2019-12-09T19:55:32.859Z

## Reporter
- **Username**: chj2934
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
summery: 

You are able to copy and paste stored XSS code into the comment section of a product in the transfers tab and receive the error.

Reproduce:

1. Create a product with the name '"'><img src=x onerror=alert(domain.domain)>'
2. add a transfer with that product
3. now go back to the product use the code button and type the same code for the title . '"'><img src=x onerror=alert(domain.domain)>'
4. you will get a XSS pop-up however ignore it. as soon as you get here you need to get out of the code setting and into the normal text and copy the the little piece of code with the image.
5. delete the code that we put in the html for the XSS.
6. go back to transfers and paste the code that we copied there
7. error

## Impact

steal cookie

## Attachments
- hacker_one_test1___Transfers____T0002___Shopify_-_Google_Chrome_11_15_2019_12_23_06_AM.png
