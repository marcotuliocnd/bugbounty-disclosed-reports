# Stored XSS in unifi.ubnt.com

## Report Details
- **Report ID**: 142084
- **URL**: https://hackerone.com/reports/142084
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-30T16:37:07.967Z
- **Disclosed**: 2016-11-26T19:37:56.762Z

## Reporter
- **Username**: b7882330c6060c6b277c5a1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ui

## Vulnerability Information
Dear @ubnt-matt,

I've found a stored xss in unifi.ubnt.com

##Step to reproduce :##
```
Step 1: Login to unifi.ubnt.com
Step 2: Connect latest unifi controller with unifi.ubnt.com via cloud access.
Step 3: Create site with any name in that controller.
Step 4: Click on launch site in unifi.ubnt.com then you will again redirect to unifi.ubnt.com with controls.
Step 5: Create Network with xss payload "><img src=x onerror=prompt(document.cookie)>
Step 6: XSS will execute.
```

**Note : ** force WebRTC should we enable.

I've attached screenshot of the same.
let me know if you need more info.

Best Regard
Shubham

## Attachments
- xss_in_unifi.ubnt.com.png
