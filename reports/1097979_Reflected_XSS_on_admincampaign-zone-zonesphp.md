# Reflected XSS on /admin/campaign-zone-zones.php

## Report Details
- **Report ID**: 1097979
- **URL**: https://hackerone.com/reports/1097979
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-02-07T19:56:00.911Z
- **Disclosed**: 2021-03-16T15:08:11.755Z

## Reporter
- **Username**: solov9ev
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: revive_adserver

## Vulnerability Information
I found a reflected XSS attack on `/admin/campaign-zone-zones.php`.

Revive-Adserver version is `revive-adserver-5.1.1`.

- Go to `http://revive-adserver.loc/admin/campaign-zone-zones.php?_=&clientid=1&campaignid=1&status=available%22%3E%3Cimg%20src=1%20onerror=alert(document.domain)%3E&text=`

- Malicious code executed

{F1187355}

Rendered response from server:

{F1187356}

## Impact

With this vulnerability, an attacker can for example steal users cookies or redirect users on malicious website.

## Attachments
- _________________2021-02-07_22-49-17.png
- _________________2021-02-07_22-52-58.png
