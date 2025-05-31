# Script breaking tag (Forces website to render blank) (Informative)

## Report Details
- **Report ID**: 1355537
- **URL**: https://hackerone.com/reports/1355537
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-09-30T16:08:46.021Z
- **Disclosed**: 2021-10-23T14:50:08.754Z

## Reporter
- **Username**: ch1ck3n42
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: xvideos

## Vulnerability Information
## Summary:
This is a bug affecting core HTML and JS elements on the site via Search 

## Steps To Reproduce:


  1. Open https://www.xvideos.com
  2. Click to search enter payload=  "<!--<script>" (without quotes) 
  3. Hit enter or search, watch the page break and not load any content (content is loaded in console, renders page blank) 

To note this can possibly be expanded to XSS or another injection type.

xvideobroken2.png shows the HTML content cut off in the source of the page. 

## Supporting Material/References:


F1466873: xvideobroken.PN
F1466876: xvideobroken2.PNG

## Impact

Breaks page rendering due to broken JS (Script and HTML close tags) Seems to render the website inoperable. Also seems to hang and causes memory leak due to trying to constantly load content it can't.

## Attachments
- xvideobroken.PNG
- xvideobroken2.PNG
