# Cloudflare /cdn-cgi/ path allows resizing images from unauthorised sources on enjinusercontent.com

## Report Details
- **Report ID**: 2545994
- **URL**: https://hackerone.com/reports/2545994
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-06-11T09:27:27.279Z
- **Disclosed**: 2024-06-19T10:35:37.087Z

## Reporter
- **Username**: 19whoami19
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: enjin

## Vulnerability Information
##Summary

Hello team,
During a review of the website: https://nft.production.enjinusercontent.com/ I discovered that any resource hosted under any external CDN can be rendered on the website without any restrictions. This behavior leads display of images or resources on the website, which may cause confusion for users or expose potentially sensitive assets or otherwise deface the websites or carry our misinformation or malware campaigns.

- You Achive :
1- HTML INJECTION
2- SSRF and Portal Scanning
3- Unrestricted rendering of resources from external CDNs

##Steps to Reproduce :

1- For HTMLi Visit : https://nft.production.enjinusercontent.com/cdn-cgi/image/width=1000,format=auto/https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/cloudflare.svg

{F3347763}

## Impact

Misuses of the cdn-cgi Misconfig to render external resources
Access control Bypass by smuggling in external resources to render at the company url unrestricted
Misinformation and platform manipulation for displayed content to any user without interaction
Attacker can redirect users to another websites, virtual defacement of your website etc.
Webpage modifications
HTML Injection

## Attachments
- image.png
