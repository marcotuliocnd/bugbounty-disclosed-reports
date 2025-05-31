# Clickjacking on https://download.nextcloud.com

## Report Details
- **Report ID**: 658011
- **URL**: https://hackerone.com/reports/658011
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-07-24T13:15:37.331Z
- **Disclosed**: 2019-11-11T15:24:09.625Z

## Reporter
- **Username**: bibek1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
This page is vulnerable to clickjacking https://download.nextcloud.com

Steps to Reproduce:

1. Copy the following code and save it as clickjacking.html
<html>
   <head>
     <title>Clickjack test page</title>
   </head>
   <body>
     <p>Website is vulnerable to clickjacking!</p>
     <iframe src="https://download.nextcloud.com" width="500" height="500"></iframe>
   </body>
</html>

2. Open it in browser

You can see the website is vulnerable to clickjacking

## Impact

Anyone can be tricked to download files without their intention

## Attachments
- nxtcloud.JPG
