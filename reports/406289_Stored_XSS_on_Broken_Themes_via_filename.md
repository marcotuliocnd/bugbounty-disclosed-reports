# Stored XSS on Broken Themes via filename

## Report Details
- **Report ID**: 406289
- **URL**: https://hackerone.com/reports/406289
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-09-06T06:37:59.749Z
- **Disclosed**: 2020-08-25T15:56:24.873Z

## Reporter
- **Username**: apapedulimu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
Hi, I've found something here, 

##Description 
XSS Stored because filename of theme when broken, So when theme is broken, Wordpress will inform the name of  theme who has been broken which is the folder name of  theme and inform the error with description message.

{F342862}

Looks like the filename is reflected, on the `Name` of the detail broken themes. I try to rename the folder to malicious name ( payload : <img src=x onerror=alert(1)> ) and the payload it'll be execute.

{F342863}

##POC
1. Upload theme
1. Delete the style.css ( or you can make new folder on theme path with payload name )
1.  Rename the folder to `<img src=x onerror=alert(1)>` 
1. See theme page. 

##Video 
https://youtu.be/IuJrcR_BoKo

## Impact

XSS will be execute , because the filename is stored on page without any filter, and this is possible to make stored XSS.

It'll be good to filter / encoding the illegal character, like wordpress do on themes upload.

## Attachments
- Screen_Shot_2018-09-06_at_1.25.01_PM.png
- Screen_Shot_2018-09-06_at_1.32.24_PM.png
