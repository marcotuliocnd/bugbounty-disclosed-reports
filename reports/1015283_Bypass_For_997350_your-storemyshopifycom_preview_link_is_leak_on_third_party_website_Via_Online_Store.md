# Bypass For #997350 your-store.myshopify.com preview link is leak on third party website Via Online Store

## Report Details
- **Report ID**: 1015283
- **URL**: https://hackerone.com/reports/1015283
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-10-21T13:47:54.036Z
- **Disclosed**: 2022-02-10T19:42:54.345Z

## Reporter
- **Username**: danishalkatiri
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi Security Team,

#Description
Full Description in #997350 


The owner of that website can perform a security compromise by grabbing those links.

#Solution:
The solution is very very SIMPLE. Just include the following HTML code in the following in code between <head> tags of the html of the page: <meta name="referrer" content="never" />
This will not send referrer headers to third party websites.

#Reproduction Instructions /
1)Open your Store & add  social media Links.
2)Click  F1045363. 
3)Now turn burp suite intercept on and click on Click on any social media link(on follow us section). Check for the requests having the Link in Referrer as third party website. And copy the Link.
4)Now turn intercept off and Open Link.(with that token) in other tab,browser or PC.
5)Now you you sucesfully catch/preview all action in your-store.myshopify.com from store owner without store password.

>Preview all action/Login

#Proof of Concept
F1045355
F1045356
F1045357
F1045358
F1045359
F1045360

#Additional Information:
Note also that if users can author content within the application then an attacker may be able to inject links referring to a domain they control in order to capture data from URLs used within the application.

## Impact

As you can see in the Referrer preview Link is getting leaked to third party sites. So, the person who has the complete control over that particular third party site can Use the Link to preview all action in your-store.myshopify.com from store owner without store password.

## Attachments
- 01.PNG
- 02.PNG
- 03.PNG
- 04.PNG
- 05.PNG
- Video_1.avi
- preview_Via_`Online_store`.PNG
