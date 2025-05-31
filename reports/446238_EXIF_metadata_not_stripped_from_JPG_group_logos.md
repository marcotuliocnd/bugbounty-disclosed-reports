# EXIF metadata not stripped from JPG group logos

## Report Details
- **Report ID**: 446238
- **URL**: https://hackerone.com/reports/446238
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-11-17T03:01:12.894Z
- **Disclosed**: 2020-09-08T14:02:33.063Z

## Reporter
- **Username**: jackb898
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
**Summary:** When uploading JPEG images as group logos on Gitlab, the EXIF metadata is not removed or changed in any way.

**Description:** When setting up a group on Gitlab, you can upload a logo, and if you upload a JPEG with EXIF metadata on it, it isn't stripped. This can lead to disclosure of location where photo was taken or other personal information by the photo uploader if their group is public, as anyone can download the logo and check the metadata.

## Steps To Reproduce:

1. Upload a testing image w any EXIF tags filled in (you can test with the attached download.jpg image on this report)
2. Make the group public
3. Visit the group page unauthenticated and download the image
4. Use Windows properties tool or any EXIF viewer, check the metadata. Whatever was there when uploaded should be there when downloaded, including the exact file name (though the file name part isn't an actual reportable problem, it's good practice to just encode/make it a random file name in case the user uploading forgets to remove personal information in the file name)

## PoC
Check out my group: https://gitlab.com/gthgh
Try downloading the logo. The metadata for it should show "egginfo" under Copyright.

## Impact

An attacker could download public group logos and find sensitive metadata. Some phones attach metadata with the latitude/longitude of where the photo was taken which could leak important information, and it's just best practice as well to strip all metadata from images when uploaded.

## Attachments
- download.jpg
