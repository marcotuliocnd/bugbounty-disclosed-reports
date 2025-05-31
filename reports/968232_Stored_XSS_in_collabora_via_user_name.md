# Stored XSS in collabora via user name

## Report Details
- **Report ID**: 968232
- **URL**: https://hackerone.com/reports/968232
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-08-27T03:14:13.196Z
- **Disclosed**: 2020-09-19T02:00:06.852Z

## Reporter
- **Username**: meliodas19
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Affected: collabora and nextcloud

Ubuntu 18.04.5 LTS
Nextcloud 19.0.1 snap version
collabora (CODE)

The name of the user is displayed when him joins to edit the document allowing the attacker trigger xss.

## Impact

* Set the name of the attacker account to <img src=a onerror=alert(window.parent.location)>
* Create a new document → share the document with admin or another victim → the document will appear automatically in the files of the victim as shared
* The attacker opens the document and waits until the victim also opens the document when opening it the payload is executed

{F965228}

## Attachments
- out.mp4
