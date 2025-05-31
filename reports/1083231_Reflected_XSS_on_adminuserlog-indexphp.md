# Reflected XSS on /admin/userlog-index.php

## Report Details
- **Report ID**: 1083231
- **URL**: https://hackerone.com/reports/1083231
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-21T16:36:57.233Z
- **Disclosed**: 2021-01-26T14:26:57.069Z

## Reporter
- **Username**: solov9ev
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: revive_adserver

## Vulnerability Information
I found a reflected XSS attack on `/admin/userlog-index.php`. 

Revive-Adserver  version is `revive-adserver-5.1.0`.

- Go to `http://revive-adserver.loc/admin/userlog-index.php?advertiserId=0&publisherId=0&period_preset=all_events%3C/script%3E%3Cscript%3Ealert(document.domain)%3C/script%3E%3Cscript%3E&period_start=&period_end=&setPerPage=10`
- Malicious code executed

{F1166698}

Rendered response from server:

{F1166701}

## Impact

With this vulnerability, an attacker can for example steal users cookies or redirect users on malicious website.

## Attachments
- _________________2021-01-21_19-31-55.png
- _________________2021-01-21_19-32-40.png
