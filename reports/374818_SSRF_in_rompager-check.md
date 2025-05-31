# SSRF in rompager-check

## Report Details
- **Report ID**: 374818
- **URL**: https://hackerone.com/reports/374818
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-06-30T19:40:10.517Z
- **Disclosed**: 2018-11-09T14:54:12.318Z

## Reporter
- **Username**: bb9866f3f743d6bf69b6836
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: hannob

## Vulnerability Information
## Summary

The script `rompager.php` does not restrict which hosts can be requested. Thereby, an attacker can send HTTP requests to localhost and other servers of the same local network segment, on port 80 and 7547. 

## Description

In `rompager.php`, the value of `CURLOPT_URL` is fully controlled:

```php
<?php
// [...]
function checkHost($ip, $port) {
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, "http://".$ip);
	curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 1);
	curl_setopt($ch, CURLOPT_TIMEOUT, 1);
	curl_setopt($ch, CURLOPT_HEADER, TRUE);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
	curl_setopt($ch, CURLOPT_PORT, $port);
	$data = curl_exec($ch);
// [...]
	} else {
		$ip = $_GET['ip'];
	}
	output("<h4>Port 80</h4>\n");
	checkHost($ip, 80);
	output("<h4>Port 7547</h4>\n");
	checkHost($ip, 7547);
```

## Steps To Reproduce

  1. Access https://rompager.hboeck.de/?ip=localhost;
  1. Notice that *No RomPager found* is shown under *Port 80*.

## Impact

An attacker could force `rompager.hboeck.de` to perform HTTP requests to localhost or servers of the same local network segment.

## Attachments
No attachments
