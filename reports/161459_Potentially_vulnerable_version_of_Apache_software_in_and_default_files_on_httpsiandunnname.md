# Potentially vulnerable version of Apache software in and default files on https://iandunn.name/

## Report Details
- **Report ID**: 161459
- **URL**: https://hackerone.com/reports/161459
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-19T21:10:32.615Z
- **Disclosed**: 2016-09-27T21:46:08.780Z

## Reporter
- **Username**: ethnicalhacker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: iandunn-projects

## Vulnerability Information
Hi,

The underlying web server for https://iandunn.name/ is not configured to hide the version of Apache in place. As a result, when attempts are made for the following files, a verbose response is received revealing the underlying Apache version. 

It should be noted that the underlying software could be back-ported and a newer version could be in place and should be investigated further. However, since the version reported is publicly known to contain vulnerabilities, a malicious attacker may be convinced to investigate further more malicious vulnerabilities.

Potentially Vulnerable version of Apache in place:

https://iandunn.name/wordpress/wp-admin.php
https://iandunn.name/wordpress/wp-config.php

Additionally, the following default WordPress file was identified revealing the version of WordPress in place: and should be removed:

https://iandunn.name/wordpress/readme.html

Thanks

## Attachments
- vulnerable_apache_version.PNG
- default_wordpress_file.PNG
