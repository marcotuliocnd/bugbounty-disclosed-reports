# WordPress vulnerable to multiple attacks at https://nextcloud.com

## Report Details
- **Report ID**: 476526
- **URL**: https://hackerone.com/reports/476526
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-01-08T11:41:18.970Z
- **Disclosed**: 2020-03-01T13:39:43.150Z

## Reporter
- **Username**: br3ach
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
**summary:**
your current version of WordPress is available to multiple attacks check (INFO.php)

**available attacks:**
- Unauthenticated Arbitrary File Deletion
- lib/IPTraf.php User-Agent Header Stored XSS
- Password Creation Restriction Bypass
- wp-admin/admin.php whois Parameter Stored XSS
- XSS & IAA
- Banned IP Functionality Bypass
- XSS in Referer Header
- Username Enumeration

**POC**
I was able to enumerate some of your users check (POC.png)

## Impact

Attacker can use any of these attacks and steal a lot of information from your website
as I did with *Username Enumeration*

## Attachments
- INFO_1.png
- INFO.png
- POC.png
