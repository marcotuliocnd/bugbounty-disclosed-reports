# [Reflected XSS] In Request URL

## Report Details
- **Report ID**: 515484
- **URL**: https://hackerone.com/reports/515484
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-03-26T10:13:25.245Z
- **Disclosed**: 2020-03-01T13:18:48.738Z

## Reporter
- **Username**: nstikhomirov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
In [index.php file](https://github.com/nextcloud/updater/blob/master/index.php#L1765) on 1765 we can see XSS:
`<a class="button" href="<?php echo str_replace('/index.php', '/../', $updaterUrl); ?>">`
Because NextCloud allow links like: '/index.php/{ANY_CONTENT}'
If we will do request like: 
```
POST /updater/index.php/h"><script>alert(1);</script> HTTP/1.1
Host: vulns.local
Content-Type: application/x-www-form-urlencoded
Content-Length: 33

updater-secret-input={OUR_SECRET}
```
We will see Reflected XSS: F452129
To fix this vulnerability need to patch `<a class="button" href="<?php echo str_replace('/index.php', '/../', $updaterUrl); ?>">` to `<a class="button" href="<?php echo htmlspecialchars(str_replace('/index.php', '/../', $updaterUrl), ENT_QUOTES); ?>">`

## Impact

If the attacker knows the secret phrase, then they can implode illegitimate html code in page

## Attachments
- Screenshot_2.png
