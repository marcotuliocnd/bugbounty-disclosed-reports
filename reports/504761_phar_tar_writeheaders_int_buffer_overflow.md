# phar_tar_writeheaders_int() buffer overflow

## Report Details
- **Report ID**: 504761
- **URL**: https://hackerone.com/reports/504761
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-03-04T12:21:44.897Z
- **Disclosed**: 2020-11-09T01:46:01.959Z

## Reporter
- **Username**: jordyzomer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
A buffer overflow has been found in the phar_tar_writeheaders_int() function.

it does a strncpy to header->linkname from entry->link with the size of entry->link.

As you can see in https://github.com/php/php-src/blob/master/ext/phar/tar.h#L66 , header->linkname is a char of the size 100. Once entry->link contains a value that's bigger than 100 it will overflow the _tar_header structure.

This can be fixed by setting the size argument of strncpy to sizeof(header->linkname) for example:

strncpy(header.linkname, entry->link, strlen(header->linkname);

This has been fixed in the following references:

https://github.com/php/php-src/commit/071e18c6971c4cf64297378b30b945a1b85d682a
http://git.php.net/?p=php-src.git;a=commit;h=e0f5d62bd6690169998474b62f92a8c5ddf0e699
https://bugs.php.net/bug.php?id=77586&edit=2

Kind Regards,

Jordy Zomer

## Impact

An attacker could overflow the buffer resulting in either a crash (DoS), EOP or RCE.

## Attachments
No attachments
