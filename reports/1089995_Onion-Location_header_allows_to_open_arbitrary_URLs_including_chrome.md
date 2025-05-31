# Onion-Location header allows to open arbitrary URLs including chrome:

## Report Details
- **Report ID**: 1089995
- **URL**: https://hackerone.com/reports/1089995
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-01-29T02:51:18.444Z
- **Disclosed**: 2023-06-22T05:52:04.648Z

## Reporter
- **Username**: nishimunea
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

This [PR](https://github.com/brave/brave-core/pull/6762) introduced "Open in Tor" feature that can open .onion URLs offered through `Onion-Location` response header, but `Onion-Location` header allows to open arbitrary URLs such as `javascript:` and `chrome:`.
This behavior can be exploited as a way to bypass SOP and gain access to privileged URLs.

## Products affected: 

* Brave Nightly for OSX (1.21.28 Chromium: 88.0.4324.96 (Official Build) nightly (x86_64))

## Steps To Reproduce:

* Open https://csrf.jp/brave/onion.php
* Click "Open in Tor" button shown in the Brave's address bar
* Privileged URL `chrome://restart/` is opened, and Brave is restarted.

If a user enabled "Automatically redirect .onion sites" in the settings, `chrome://restart/` is opened automatically and Brave continues to restart endlessly.

## Supporting Material/References:

PoC code in PHP is below

   ```
<?php
header("Onion-Location: chrome://restart/");
?>
   ```

## Impact

As written in the summary, attacker can bypass SOP restrictions and gain access to privileged URLs.

## Attachments
No attachments
