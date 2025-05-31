# Authenticated XXE

## Report Details
- **Report ID**: 1095645
- **URL**: https://hackerone.com/reports/1095645
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-02-04T17:34:58.231Z
- **Disclosed**: 2021-05-18T13:52:04.479Z

## Reporter
- **Username**: sonarsource
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
## Description:

The WordPress core Media Library does not securely parse XML content when running on PHP 8. By uploading a malicious .wav file, an authenticated attacker can trigger a XXE vulnerability which enables to read secret system files, DoS the web server, perform SSRF, or aim at Remote Code Execution via Phar Deserialization.

## Steps To Reproduce:

Requirements:
* latest WordPress 5.6 installation
* running on PHP 8
* *author* user privileges in WordPress, or higher
* another web server that is controlled by the attacker to retrieve leaked data

The vulnerability can be exploited by uploading a crafted .wav file. The attached archive contains such a .wav file with a payload for extracting the content of */etc/passwd* by loading an external DTD. To reproduce:

1. Adapt the address in the 2 files in the attached PoC archive to point to a web server that you control (and that is reachable from the targeted WordPress installation).
2. For the .wav file, the address has to be adapted at `0x000338CD` (best use a hex editor for this, doing that with a text editor might corrupt the file).
3. Put the file *xxe.dtd* at the root of the webserver that you control.
4. Login to WordPress as author and upload *xxe.wav*  in the media library.
5. The content of */etc/passwd* will appear in the access logs of the web server base64 encoded (see attached screenshot).

## Vulnerable Code:

The vulnerable code commit is the following:
https://github.com/WordPress/WordPress/commit/03eba7beb2f5b96bd341255eaa30d6b612e62507

The vulnerable code is:
```
			if (PHP_VERSION_ID < 80000) {
				// http://websec.io/2012/08/27/Preventing-XEE-in-PHP.html
				// https://core.trac.wordpress.org/changeset/29378
				// This function has been deprecated in PHP 8.0 because in libxml 2.9.0, external entity loading is
				// disabled by default, so this function is no longer needed to protect against XXE attacks.
				$loader = libxml_disable_entity_loader(true);
			}
			$XMLobject = simplexml_load_string($XMLstring, 'SimpleXMLElement', LIBXML_NOENT);
```

It was recently modified to accommodate for the deprecation of the `libxml_disable_entity_loader()` function in PHP 8. The mistake here is to rely on the fact that XXE is no longer possible by default in PHP 8 (as it requires libxml version > 2.9). This is true, but using the `LIBXML_NOENT` flag is certainly not the default. The flag explicitly activates entity substitution (the name of the flag might be a little misleading). So if user input reaches that point as part of the `$XMLstring` variable, XXE is possible.

## Impact

An attacker can:
- read secret system files, such as *.htaccess* or *wp-config.php*
- DoS the web server via a malicious XML document, or by loading */dev/urandom* via XXE
- fingerprint and exploit services in the internal network by turning the XXE into SSRF
- trigger a Phar Deserialization by using the `phar://` stream wrapper within the XXE which can lead to further vulnerabilities, depending on the gadget chains available in the WordPress core and its plugins.

## Attachments
- xxe.zip
- screenshot.png
