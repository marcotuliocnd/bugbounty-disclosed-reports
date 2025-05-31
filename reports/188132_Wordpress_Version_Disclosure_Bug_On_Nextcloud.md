# Wordpress Version Disclosure Bug On Nextcloud

## Report Details
- **Report ID**: 188132
- **URL**: https://hackerone.com/reports/188132
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-12-04T06:31:39.344Z
- **Disclosed**: 2016-12-04T09:03:23.103Z

## Reporter
- **Username**: cr4zyrud
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi @nextcloud ,

#Description
Wordpress version disclosure.

#Affected items
https://nextcloud.com/readme.html
https://nextcloud.com/wp-admin/install.php
https://nextcloud.com/wp-login.php

#The impact of this vulnerability
Possible Wordpress Version information disclosure.You are using wordpress 4.6.1 version also you not delete **`https://nextcloud.com/wp-admin/install.php`** if you got any type of database problem in your site attacker try to install it for deface,And to be noted that you not protect your admin panel **`https://nextcloud.com/wp-login.php`** with captcha attacker can easily Bruteforce your admin panel.

#Web references
* http://www.hackingtutorials.org/web-application-hacking/hack-a-wordpress-website-with-wpscan/

#How to fix this vulnerability
1. Just Delete The **readme.html** from **`/`** root path
1. and also delete **install.php** from **`/wp-admin/`**

Please resolved as close if not acceptable.Because this is my first hunting ;) .
**Thanks**

## Attachments
No attachments
