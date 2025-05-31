# Possibility to force an admin to install recommended applications

## Report Details
- **Report ID**: 1403614
- **URL**: https://hackerone.com/reports/1403614
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-11-18T00:00:52.589Z
- **Disclosed**: 2022-04-29T11:50:18.775Z

## Reporter
- **Username**: igorpyan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
Endpoint /nextcloud/index.php/core/apps/recommended is accessible via GET http method and doesn't check anti-csrf token. If an admin visits this endpoint in a browser the process of installation of recommended applications begins immediately.

## Steps To Reproduce:
1. an attacker creates a malicious page on controlled domain
1. an attacker enforce an admin to visit this page
1. an admin visits this page
1. applications will be installed in a while

## Affected version:
nextcloud/server: 22.2.2 (at least)

## Recommendation:
require requesttoken for this GET query
or you can change behaviour so to initiate the installation process by manual click (POST query with checking of requesttoken)

## [attachment / reference]
{F1517676}

## Impact

Increasing of attack surface.
Any unused plugins should be disabled or removed. But this way allows to install them.

## Attachments
- _nextcloud__csrf_install_recommended_app-2021-11-18_00.35.16
