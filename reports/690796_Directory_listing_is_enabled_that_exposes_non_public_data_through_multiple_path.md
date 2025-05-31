# Directory listing is enabled that exposes non public data through multiple path 

## Report Details
- **Report ID**: 690796
- **URL**: https://hackerone.com/reports/690796
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-09-09T08:59:58.285Z
- **Disclosed**: 2020-02-01T04:39:52.072Z

## Reporter
- **Username**: tibin_sunny
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Directory Listing is enabled on https://try.nextcloud.com and it shows out a few files on the server + The server version.

POC: https://try.nextcloud.com/assets/
        https://try.nextcloud.com/css/
        https://try.nextcloud.com/js/

## Impact

This could leak sensitive information on the server and it also allows an attacker to gain knowledge about the web-technology used by the website

## Attachments
- nextcloud.PNG
