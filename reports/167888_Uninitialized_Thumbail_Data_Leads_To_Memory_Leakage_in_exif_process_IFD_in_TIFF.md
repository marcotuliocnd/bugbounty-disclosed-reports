# Uninitialized Thumbail Data Leads To Memory Leakage in exif_process_IFD_in_TIFF

## Report Details
- **Report ID**: 167888
- **URL**: https://hackerone.com/reports/167888
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-13T03:12:37.859Z
- **Disclosed**: 2019-11-12T09:27:23.211Z

## Reporter
- **Username**: hoangnguyen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
I found other code chunk that leads to memory leakage.
```
	exif_process_IFD_in_TIFF(ImageInfo, entry_offset, sub_section_index);
	if (section_index!=SECTION_THUMBNAIL && entry_tag==TAG_SUB_IFD) {
		if (ImageInfo->Thumbnail.filetype != IMAGE_FILETYPE_UNKNOWN
		&&  ImageInfo->Thumbnail.size
		&&  ImageInfo->Thumbnail.offset
		&&  ImageInfo->read_thumbnail
		) {
#ifdef EXIF_DEBUG
			exif_error_docref(NULL EXIFERR_CC, ImageInfo, E_NOTICE, "%s THUMBNAIL @0x%04X + 0x%04X", ImageInfo->Thumbnail.data ? "Ignore" : "Read", ImageInfo->Thumbnail.offset, ImageInfo->Thumbnail.size);
#endif
			if (!ImageInfo->Thumbnail.data) {
				ImageInfo->Thumbnail.data = safe_emalloc(ImageInfo->Thumbnail.size, 1, 0);
				php_stream_seek(ImageInfo->infile, ImageInfo->Thumbnail.offset, SEEK_SET);
				fgot = php_stream_read(ImageInfo->infile, ImageInfo->Thumbnail.data, ImageInfo->Thumbnail.size);
				if (fgot < ImageInfo->Thumbnail.size) {
					EXIF_ERRLOG_THUMBEOF(ImageInfo)
				}
				exif_thumbnail_build(ImageInfo);
			}
		}
	}
```
As you can see this code is processing SUB_IFD_TAG and not verify offset of Thumbnail data. Because lack of checking ImageInfo->Thumbnail.offset if an attack set ImageInfo->Thumbnail.offset larger than ImageInfo->FileSize then *php_stream_read* return 0 to fgot, because  EXIF_ERRLOG_THUMBEOF was defined as : 
```
#define EXIF_ERRLOG_THUMBEOF(ImageInfo)   exif_error_docref(NULL EXIFERR_CC, ImageInfo, E_WARNING, "%s", EXIF_ERROR_THUMBEOF);

```
As you can see there is no exit after this error is output.

This bug does same problem with this bug i reported before https://bugs.php.net/bug.php?id=72627

Here tiff file : https://drive.google.com/file/d/0B0D1DYQpkA9USUt4c2ZBT21SWE0/view?usp=sharing

Bug here : https://bugs.php.net/bug.php?id=72926

## Attachments
No attachments
