# unchecked unserialize usages in audit-trail-extension/audit-trail-extension.php

## Report Details
- **Report ID**: 185909
- **URL**: https://hackerone.com/reports/185909
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-11-28T01:20:42.688Z
- **Disclosed**: 2016-12-30T07:08:31.322Z

## Reporter
- **Username**: e3amn2l
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: iandunn-projects

## Vulnerability Information
in:
	https://github.com/iandunn/audit-trail-extension/blob/master/audit-trail-extension.php#L106
	https://github.com/iandunn/audit-trail-extension/blob/master/audit-trail-extension.php#L112
	https://github.com/iandunn/audit-trail-extension/blob/master/audit-trail-extension.php#L133
	https://github.com/iandunn/audit-trail-extension/blob/master/audit-trail-extension.php#L139
	
there is usages of unserialize function		
```
					$option = unserialize( $item->data );
					$details = unserialize( $item->data );
```

without disallowing unneeded classes.
thus, if attacker managed to control the value of $item->data he will be able to:

1\. conduct PHP POP exploitation, more information:

http://www.slideshare.net/_s_n_t/php-unserialization-vulnerabilities-what-are-we-missing
http://www.slideshare.net/MailRuGroup/security-meetup-22-php-unserialize-exploiting

2\. unserialize itself has many security bugs in previous PHP versions which can be exploited, more information:

https://www.evonide.com/fuzzing-unserialize/
https://blog.checkpoint.com/wp-content/uploads/2016/08/Exploiting-PHP-7-unserialize-Report-160829.pdf

fix:

1\. don't use serialize/unserialize if json_encode/json_decode can be used instead. (fix both 1 & 2 attack vectors)
2\. if 1 isn't possible, use safe unserialize invocation, such as:
```
        if (version_compare(PHP_VERSION, '7.0', 'lt')) {
            return safeUnserialize($data);
        } else {
            return safeUnserialize($data, false);
        }
```

Implement safeUnserialize function that based on PMA_safeUnserialize:
https://github.com/phpmyadmin/phpmyadmin/blob/fb161a7bebe60d902f743227158eca6a9889c472/libraries/core.lib.php#L1080
but with fix for the issue described in:
https://hackerone.com/reports/181315#activity-1322058

## Attachments
No attachments
