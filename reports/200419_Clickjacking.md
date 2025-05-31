# Clickjacking

## Report Details
- **Report ID**: 200419
- **URL**: https://hackerone.com/reports/200419
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-01-22T21:28:26.362Z
- **Disclosed**: 2017-02-02T11:32:17.453Z

## Reporter
- **Username**: b1b62e8d81ce1e3993ad913
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: pushwoosh

## Vulnerability Information
Steps to reproduce:

create index.html file with following content:
<iframe sandbox="allow-scripts allow-forms" src="https://go.pushwoosh.com/register" width="1000" height="600"></iframe>

Open index.html in browser

Actual result: Pushwoosh viewed in iframe.
Expected result: do not allow clickjacking
Root cause:

```
var isInIFrame = (function () {
			try {
				return window.self !== window.top;
			} catch (e) {
				return true;
			}
		})();
```

## Attachments
- pw-clickjacking.png
