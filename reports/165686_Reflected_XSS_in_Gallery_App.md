# Reflected XSS in Gallery App

## Report Details
- **Report ID**: 165686
- **URL**: https://hackerone.com/reports/165686
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-09-04T15:59:09.562Z
- **Disclosed**: 2016-12-03T22:01:12.670Z

## Reporter
- **Username**: soreks
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Go to: `nextcloud/index.php/apps/gallery/#%3E%3Cscript%3Ealert%28document.domain%29%3C/script%3Ejavascript:alert%280%29//%00`

Tested on: Firefox 43.0.1

If you need more information then write me.

## Attachments
- 1.JPG
