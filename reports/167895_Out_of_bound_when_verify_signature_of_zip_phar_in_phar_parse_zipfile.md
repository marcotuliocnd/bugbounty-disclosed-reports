# Out of bound when verify signature of zip phar in phar_parse_zipfile

## Report Details
- **Report ID**: 167895
- **URL**: https://hackerone.com/reports/167895
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-13T04:08:14.362Z
- **Disclosed**: 2019-11-12T09:31:59.768Z

## Reporter
- **Username**: hoangnguyen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
https://bugs.php.net/bug.php?id=72928

There was a security code in phar_parse_zipfile
```
sig = (char *) emalloc(entry.uncompressed_filesize);
read = php_stream_read(fp, sig, entry.uncompressed_filesize);
if (read != entry.uncompressed_filesize) {
	php_stream_close(sigfile);
	efree(sig);
	PHAR_ZIP_FAIL("signature cannot be read");
}
mydata->sig_flags = PHAR_GET_32(sig);
if (FAILURE == phar_verify_signature(sigfile,
	php_stream_tell(sigfile),
	mydata->sig_flags,
	sig + 8,
	entry.uncompressed_filesize - 8,
	fname,
	&mydata->signature,
	&mydata->sig_len,
	error)
	) {
```
There are no checking *entry.uncompressed_filesize* attacker can create a signature.bin with size less than 8 and then this value is passed to *phar_verify_signature* as sig_len as you can see `entry.uncompressed_filesize - 8` as result sig_len is overflow.
And the third param is sig buffer as you can see `sig + 8`, because *entry.uncompressed_filesize* is less than 8 by default emalloc will return 16 bytes this result may lead to heap out of bound.

phar zip file : https://drive.google.com/file/d/0B0D1DYQpkA9Ud3I2OFlfeFRqbEU/view?usp=sharing

Test script:
---------------
```
<?php
	$phar = new PharData('phars/signature.zip');
	var_dump($phar);
?>
```

## Attachments
No attachments
