# Reflected XSS on /admin/stats.php

## Report Details
- **Report ID**: 1187820
- **URL**: https://hackerone.com/reports/1187820
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-05-07T14:35:04.269Z
- **Disclosed**: 2021-06-03T12:38:57.290Z

## Reporter
- **Username**: solov9ev
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: revive_adserver

## Vulnerability Information
Hi, Security Team!

Linked to the reports:
- https://hackerone.com/reports/1083376
- https://hackerone.com/reports/1097217

In the past reports, we have corrected Reflected XSS. But recently it turned out that with the parameter `breakdown = affiliates`, this vulnerability still works. (Fixed when parameter `breakdown = history`).

- Go to `http://revive-adserver.loc/admin/stats.php?entity=global&breakdown=affiliates&statsBreakdown=day%27%20onclick=alert(document.domain)%20accesskey=X%20`
- For the payload to be executed, the user needs to press the access key combination for the hidden input field (for Firefox, Alt+Shift+X, see [this](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/accesskey) for other browsers).

{F1292520}

{F1292519}

## Impact

With this vulnerability, an attacker can for example steal users cookies or redirect users on malicious website.

## Attachments
- 2.png
- 1.png
