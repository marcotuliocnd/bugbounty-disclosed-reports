# Arbitrary File Deletion via Path Traversal in image-edit.php

## Report Details
- **Report ID**: 1081878
- **URL**: https://hackerone.com/reports/1081878
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-19T21:18:41.229Z
- **Disclosed**: 2022-03-22T22:56:38.526Z

## Reporter
- **Username**: egix
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: impresscms

## Vulnerability Information
## Summary:
The vulnerability is located in the `/libraries/image-editor/image-edit.php` script:

```
161.		if (@copy ( ICMS_IMANAGER_FOLDER_PATH . '/temp/' . $simage_temp, $categ_path . $simage->getVar ( 'image_name' ) )) {
162.			if (@unlink ( ICMS_IMANAGER_FOLDER_PATH . '/temp/' . $simage_temp )) {
163.				$msg = _MD_AM_DBUPDATED;

[...]

190.		} else {
191.			if (copy ( ICMS_IMANAGER_FOLDER_PATH . '/temp/' . $simage_temp, $categ_path . $imgname )) {
192.				@unlink ( ICMS_IMANAGER_FOLDER_PATH . '/temp/' . $simage_temp );
193.			}
```

User input passed through the "image_temp" parameter is not properly sanitized before being used in a call to the `unlink()` function at lines 162 and 192. This can be exploited to carry out Path Traversal attacks and delete arbitrary files in the context of the web server process.

**NOTE**: before being deleted, the file will be copied into the `/uploads/imagemanager/logos/` directory. As such, by firstly deleting the `index.html` file in that directory, it might be possible to disclose the content of arbitrary files in case the web server allows for directory listing.

## ImpressCMS branch :
The vulnerability has been tested and confirmed on ImpressCMS version 1.4.2 (the latest at the time of writing).

## Steps To Reproduce:
  1. Login into the application as any user (this should work both for Webmasters and Registered Users) 
  1. Go to: `http://[impresscms]/libraries/image-editor/image-edit.php?op=save&image_id=1&image_temp=../../../mainfile.php`
  1. The `mainfile.php` script will be deleted, rendering the website unusable

## Impact

This vulnerability might allow authenticated attackers to delete arbitrary files, potentially leading to a Denial of Service (DoS) condition or destruction of users data.

## Attachments
No attachments
