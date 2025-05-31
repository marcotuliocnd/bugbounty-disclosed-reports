# Brave: Admin Panel Access

## Report Details
- **Report ID**: 175366
- **URL**: https://hackerone.com/reports/175366
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-10-12T11:27:09.688Z
- **Disclosed**: 2017-08-10T05:11:23.792Z

## Reporter
- **Username**: ranjith16
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
** Steps to reproduce**

While browsing through the https://blog.brave.com/admin, it is getting redirected to a admin login panel https://brave.ghost.io/ghost/signin/.

**Consequence**
An attacker can easily enumerate this admin panel with the url such as https://blog.brave.com/admin
and with brute force attack this can be bypassed, but I didn't do that. If a known ghost.io vulnerability exists there can be chances of even taking over the sub domain.

**Remediation**

 It's recommended to give custom directory names instead of easily guessable names such as "admin" for such sensitive directories.

Please find the attached screenshots.

## Attachments
- 1.JPG
- 2.JPG
