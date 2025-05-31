# bypass forced password protection via circles app

## Report Details
- **Report ID**: 1406926
- **URL**: https://hackerone.com/reports/1406926
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-11-22T09:25:03.605Z
- **Disclosed**: 2022-06-19T08:10:12.075Z

## Reporter
- **Username**: michag86
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
A user can bypass password enforcement for link and email shares by using a circle

## Steps To Reproduce:
 1. enable forced passwords for link shares and email shares as administrator in the share settings
 2. as user create a circle and add an e-mail-address
 3. share some file to that circle

## Supporting Material/References:
Used version: Nextcloud Version 22.2.3 circles version 22.1.1

## Impact

A user can create an link that is not password protected even if this is forced by the administrator.

## Attachments
No attachments
