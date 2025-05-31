# constant cache_page_secret in regolith

## Report Details
- **Report ID**: 185914
- **URL**: https://hackerone.com/reports/185914
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-11-28T02:07:28.040Z
- **Disclosed**: 2016-12-30T04:48:13.103Z

## Reporter
- **Username**: e3amn2l
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: iandunn-projects

## Vulnerability Information
in:
https://github.com/iandunn/regolith/blob/master/config/plugins/wp-super-cache.php#L28
```
$cache_page_secret             = 'ad270361c39c428c9465313363b02559';
```
there usage of static $cache_page_secret, as regolith is installation template. it's better to generate the secret for each installation instead of using static known value.
knowledge of $cache_page_secret value can be used to send requests which will not pass though the caching:
https://github.com/Automattic/wp-super-cache/blob/ea592c1d2796d0bc5c343322923c5f8bb40a0066/wp-cache-phase1.php#L32
thus enable more effective DOS (denial of service) attacks as the caching mechanism is disabled.

fix:
generate the $cache_page_secret in safe way once per installation & store the value in needed configuration file.

## Attachments
No attachments
