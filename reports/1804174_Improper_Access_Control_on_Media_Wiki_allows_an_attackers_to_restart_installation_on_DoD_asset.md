# Improper Access Control on Media Wiki allows an attackers to restart installation on DoD asset

## Report Details
- **Report ID**: 1804174
- **URL**: https://hackerone.com/reports/1804174
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-12-14T11:43:28.500Z
- **Disclosed**: 2023-03-24T17:33:54.173Z

## Reporter
- **Username**: miguel_santareno
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hello,

I notice that is possible to restart installation on this media wiki website due to the fact that /mw-config/index.php is available without authentication

Poc:
https://█████████/mw-config/index.php

Regards

## Impact

Attackers can restart the application.

## System Host(s)
███████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Go directly to https://██████████/mw-config/index.php and you should see the restart installation button.

## Suggested Mitigation/Remediation Actions
Block all access to your mw-config folder.

We fixed this by adding:

RedirectMatch 404 /\mw-config



## Attachments
No attachments
