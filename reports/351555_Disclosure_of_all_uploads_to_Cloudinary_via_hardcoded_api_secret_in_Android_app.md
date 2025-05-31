# Disclosure of all uploads to Cloudinary via hardcoded api secret in Android app

## Report Details
- **Report ID**: 351555
- **URL**: https://hackerone.com/reports/351555
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-05-14T18:04:19.725Z
- **Disclosed**: 2018-09-08T14:51:22.220Z

## Reporter
- **Username**: bagipro
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reverb

## Vulnerability Information
Hi, in file ``` com/reverb/app/CloudinaryFacade.java ``` you have hardcoded the following config:
```java
private static final java.lang.String CONFIG = "cloudinary://434762629765715:█████@reverb";
```
where ``` 434762629765715:████████ ``` is basic auth details.

It shouldn't be disclosed to third parties as official docs say (https://github.com/cloudinary/cloudinary_android):
> Note: You should only include the ``` cloud_name ``` in the value, the api secret and key should be left out of the application.

I was able to access your account data
{F297519}
{F297520}

Those keys give me ability to not only access the files, but also replace and delete them, change different their settings. Also this url https://api.cloudinary.com/v1_1/reverb/usage discloses statistics regarding stored files
```json
"requests":1894689201,
"resources":36029794,
"derived_resources":256178843
```

## Impact

Disclosure of all uploads to Cloudinary via hardcoded api secret in Android app

## Attachments
- 2018-05-14_20-48-00.jpg
- 2018-05-14_20-48-42.jpg
