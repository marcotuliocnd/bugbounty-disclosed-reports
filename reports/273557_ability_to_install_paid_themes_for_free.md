# ability to install paid themes for free

## Report Details
- **Report ID**: 273557
- **URL**: https://hackerone.com/reports/273557
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-10-01T07:24:01.328Z
- **Disclosed**: 2018-05-16T15:10:43.906Z

## Reporter
- **Username**: flashdisk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi,

#Discription
while searching for access control issues on shopify I noticed a subdomain of shopify https://themes.shopify.io which gave me the opportunity to install and download paid 
themes for free.

#POC

1. go to https://themes.shopify.io/login and login
2. select one of the paid themes and press on ``buy theme`` button
3. you will be facing this screen on your shop:
 {F225469}
4. press on ``apporve charge`` button and the theme will be installed after getting to this screen:
{F225470}

#IMPACT

any user can download any paid themes and also can save them and modify them to upload them again 

#FIX

you should limit the access to  https://themes.shopify.io/ since it is for testing only.

thanks.

## Attachments
- free_themes.png
- free_themes_install.png
