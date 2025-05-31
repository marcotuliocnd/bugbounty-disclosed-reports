# [Thirdparty] Stored XSS in chat module - nextcloud server 9.0.51 installed in ubuntu 14.0.4 LTS

## Report Details
- **Report ID**: 148897
- **URL**: https://hackerone.com/reports/148897
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-07-02T18:29:25.357Z
- **Disclosed**: 2016-11-02T16:08:07.264Z

## Reporter
- **Username**: egrep
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
I found stored XSS vulnerability in nextcloud server's chat module

Nextcloud Server version - 9.0.51
OS - Ubuntu 14.0.4
Browser - Internet Explorer 11

Steps:
1) Login as non-admin user(attacker) and change full name containing XSS payload - elamaran\'>\"><script>alert(document.domain)</script>
2) Login as admin/non-admin(victim) and go to chat module
3) Click "Show information" of the attacker
4) Then the stored XSS payload in attacker's name will get execute in nextcloud domain

POC Video URL - https://youtu.be/UU60IthJWxI

## Attachments
No attachments
