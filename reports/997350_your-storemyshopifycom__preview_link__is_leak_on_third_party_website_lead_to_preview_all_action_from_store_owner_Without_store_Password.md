# your-store.myshopify.com  preview link  is leak on third party website lead to preview all action from store owner Without store Password.

## Report Details
- **Report ID**: 997350
- **URL**: https://hackerone.com/reports/997350
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-10-03T21:30:41.492Z
- **Disclosed**: 2021-07-12T20:33:47.935Z

## Reporter
- **Username**: danishalkatiri
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi Security Team,

#Description
It has been identified that the application is leaking Link to third party sites. In this case it was found that the Linkis being leaked to third party sites which is a issue knowing the fact that it can allow any malicious users to use the Link to catch/preview all action in `your-store.myshopify.com` from store owner without store password.

The owner of that website can perform a security compromise by grabbing those links.


#Solution: 
The solution is very very SIMPLE. Just include the following HTML code in the following in code between <head> tags of the html of the page: <meta name="referrer" content="never" />
This will not send referrer headers to third party websites.

#Reproduction Instructions /
1.Create new products & click Preview .F1013353
2)Now turn burp suite intercept on and click on Click on any social media link(on follow us section). Check for the requests having the Link in `Referrer` as third party website. And copy the Link.
3)Now turn intercept off and Open Link.(with that token) in other tab,browser or  PC.
4)Now you you sucesfully catch/preview all action in `your-store.myshopify.com` from store owner without store password.

>Preview all action/ 

`Store
Products
Collections
Available`


#Proof of Concept
F1013350
F1013351
F1013352
F1013356


#Additional Information:
Note also that if users can author content within the application then an attacker may be able to inject links referring to a domain they control in order to capture data from URLs used within the application.

## Impact

As you can see in the `Referrer` preview Link is getting leaked to third party sites. So, the person who has the complete control over that particular third party site can Use the Link to preview all action in your-store.myshopify.com from store owner without store password.

## Attachments
- 01.PNG
- 02.PNG
- 03.PNG
- Preview.PNG
- Video_1.avi
