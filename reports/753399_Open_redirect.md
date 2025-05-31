# Open redirect

## Report Details
- **Report ID**: 753399
- **URL**: https://hackerone.com/reports/753399
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-12-06T22:02:41.711Z
- **Disclosed**: 2020-01-18T19:32:46.179Z

## Reporter
- **Username**: nickelheck
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nordsecurity

## Vulnerability Information
The following URL is vulnerable to an open redirect (it will redirect to google.com):
https://support.nordvpn.com/#/path///google.com
vulnerable code:
```
<script>
			if (window.location.href.indexOf('#/path') !== -1) {
				console.log("document.URL", document.URL)
				window.location.href = document.URL.slice(window.location.href.indexOf('#/path') + 6);
			}
		</script>
```

## Impact

Users could get redirected to malicious domain.

## Attachments
No attachments
