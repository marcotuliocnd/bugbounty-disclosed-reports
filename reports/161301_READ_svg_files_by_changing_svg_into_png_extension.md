# READ .svg files by changing .svg into .png extension

## Report Details
- **Report ID**: 161301
- **URL**: https://hackerone.com/reports/161301
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-19T12:21:17.289Z
- **Disclosed**: 2017-03-29T14:38:33.681Z

## Reporter
- **Username**: codertom
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: instacart

## Vulnerability Information
Good Day,
Instacart

In list and recipe we could see that we can upload a picture . It won't accept `.svg` files but by changing it to `.png`.
###Steps to Reproduce
1. Create a list and recipe under accounts
2. Upload a picture. We will upload an `svg` but with a `png` extension. I've attached an `svg` file please open it and save it as `file.png`
3. Now upload the photo and you will then now see that the svg we have made is reflected in the background photo area.

Regards,
TOM

## Attachments
- bypassed.svg.svg
