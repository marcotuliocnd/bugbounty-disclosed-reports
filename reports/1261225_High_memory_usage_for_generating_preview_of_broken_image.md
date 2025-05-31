# High memory usage for generating preview of broken image

## Report Details
- **Report ID**: 1261225
- **URL**: https://hackerone.com/reports/1261225
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-07-14T10:18:51.927Z
- **Disclosed**: 2022-03-09T07:22:46.512Z

## Reporter
- **Username**: fancycode
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
When the attached file is uploaded and a preview is generated (e.g. in the folder overview of the files app), the PHP process allocates a very large amount of memory (on my machine it was shortly around 5 GByte)  and CPU.

Tested with latest master (1366b35081f1d92429787696f4175c19a602858a)  on Ubuntu 20.04 (php7.4-fpm). Option "memory_limit" is set to 512M.

## Impact

An attacker can cause a denial of service by uploading lots of such files which will cause the server to allocate too much memory / CPU.

## Attachments
- bad-header.jpg
