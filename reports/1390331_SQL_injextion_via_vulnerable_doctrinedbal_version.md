# SQL injextion via vulnerable doctrine/dbal version

## Report Details
- **Report ID**: 1390331
- **URL**: https://hackerone.com/reports/1390331
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-11-03T07:38:44.479Z
- **Disclosed**: 2022-05-11T14:08:04.479Z

## Reporter
- **Username**: nickvergessen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
SQL injection via limit parameter on user facing APIs

## Steps To Reproduce:
Run security scanner:

  1. REPORT /remote.php/dav/comments/files/1985
  1. XML input oc:filter-comments.oc:limit#text was set to 1'"
  1. You have an error in your SQL syntax

## Supporting Material/References:
For more details see:
https://github.com/nextcloud-gmbh/h1/issues/197

## Impact

Full flexed SQL injection via user provided input

## Attachments
No attachments
