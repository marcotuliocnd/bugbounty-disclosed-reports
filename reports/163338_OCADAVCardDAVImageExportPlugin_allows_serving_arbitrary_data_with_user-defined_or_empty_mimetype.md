# \OCA\DAV\CardDAV\ImageExportPlugin allows serving arbitrary data with user-defined or empty mimetype

## Report Details
- **Report ID**: 163338
- **URL**: https://hackerone.com/reports/163338
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-08-25T13:26:40.644Z
- **Disclosed**: 2016-12-03T21:59:28.846Z

## Reporter
- **Username**: lukasreschke
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
The SabreDAV plugin `\OCA\DAV\CardDAV\ImageExportPlugin` is used for displaying pictures of a VCF. It registers on a GET request on a CardDAV element and acts when the query parameter `photo` is sent.

The logic can be seen below:
```
/**
 * Intercepts GET requests on addressbook urls ending with ?photo.
 *
 * @param RequestInterface $request
 * @param ResponseInterface $response
 * @return bool|void
 */
function httpGet(RequestInterface $request, ResponseInterface $response) {

	$queryParams = $request->getQueryParameters();
	// TODO: in addition to photo we should also add logo some point in time
	if (!array_key_exists('photo', $queryParams)) {
		return true;
	}

	$path = $request->getPath();
	$node = $this->server->tree->getNodeForPath($path);

	if (!($node instanceof Card)) {
		return true;
	}

	$this->server->transactionType = 'carddav-image-export';

	// Checking ACL, if available.
	if ($aclPlugin = $this->server->getPlugin('acl')) {
		/** @var \Sabre\DAVACL\Plugin $aclPlugin */
		$aclPlugin->checkPrivileges($path, '{DAV:}read');
	}

	if ($result = $this->getPhoto($node)) {
		$response->setHeader('Content-Type', $result['Content-Type']);
		$response->setStatus(200);

		$response->setBody($result['body']);

		// Returning false to break the event chain
		return false;
	}
	return true;
}
```

As can be seen the the content-type is read from `$this->getPhoto($node)` as well as the body, looking at it's implementation shows that the data is directly read from the vCard:

```
function getPhoto(Card $node) {
	// TODO: this is kind of expensive - load carddav data from database and parse it
	//       we might want to build up a cache one day
	try {
		$vObject = $this->readCard($node->get());
		if (!$vObject->PHOTO) {
			return false;
		}

		$photo = $vObject->PHOTO;
		$type = $this->getType($photo);

		$val = $photo->getValue();
		if ($photo->getValueType() === 'URI') {
			$parsed = \Sabre\URI\parse($val);
			//only allow data://
			if ($parsed['scheme'] !== 'data') {
				return false;
			}
			if (substr_count($parsed['path'], ';') === 1) {
				list($type,) = explode(';', $parsed['path']);
			}
			$val = file_get_contents($val);
		}
		return [
			'Content-Type' => $type,
			'body' => $val
		];
	} catch(\Exception $ex) {
		$this->logger->logException($ex);
	}
	return false;
}
```

This means if somebody uploads a VCF with the following content this will deliver the content `<html><font color="red">test</font></html>` with an empty Content-Type. The photo is a base64 encoding of before mentioned string.

```
BEGIN:VCARD
VERSION:3.0
FN:test
UID:5cf6e5e2-ec37-4798-abb7-3c261eda92c9
PHOTO;ENCODING=b:PGh0bWw+PGZvbnQgY29sb3I9InJlZCI+dGVzdDwvZm9udD48L2h0bWw+
END:VCARD
```

Then it's sufficient to just access http://10.211.55.7/stable9/remote.php/dav/addressbooks/users/admin/contacts/5cf6e5e2-ec37-4798-abb7-3c261eda92c9.vcf?photo, the easiest to reproduce this is by enabling `debug` mode and using Internet Explorer since we employ CSP which largely mitigates the issue.

As another remark, we should replace the `file_get_contents` with another implementation. This seems currently like a too risky implementation for me.

{F114833}

## Attachments
- 2016-08-25_15-26-06.png
