# Potential directory traversal in OC\Files\Node\Folder::getFullPath

## Report Details
- **Report ID**: 1765631
- **URL**: https://hackerone.com/reports/1765631
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-11-08T06:56:54.642Z
- **Disclosed**: 2023-05-04T07:59:49.938Z

## Reporter
- **Username**: nickvergessen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
https://github.com/nextcloud/server/blob/67551f379f3105d117b9d19095dd381450fe40dd/lib/private/Files/Node/Folder.php#L68-L73
is validating and normalizing the string in the wrong order.

Validation checks for `/../` kind of situations and `normalizePath` later on replaces `\` with `/`, so it would be possible to get `/../` again.

```php
	public function getFullPath($path) {
		if (!$this->isValidPath($path)) {
			throw new NotPermittedException('Invalid path');
		}
		return $this->path . $this->normalizePath($path);
	}
```

## Impact

The function seems to be used in newFile() and newFolder() items, allowing to create paths outside of ones own space and overwriting stuff from others.

## Attachments
No attachments
