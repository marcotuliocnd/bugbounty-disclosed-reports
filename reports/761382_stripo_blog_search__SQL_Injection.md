# stripo blog search  SQL Injection

## Report Details
- **Report ID**: 761382
- **URL**: https://hackerone.com/reports/761382
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-12-19T01:25:21.170Z
- **Disclosed**: 2020-01-30T11:50:16.629Z

## Reporter
- **Username**: bluebridsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripo

## Vulnerability Information
## Summary:

Sql injection of search parameters at blog search request

## Steps To Reproduce:

  1. request https://stripo.email/blog/search/
  2. input search `1' AND (SELECT 6268 FROM (SELECT(SLEEP(5)))ghXo) AND 'IKlK'='IKlK`
  3. See a very large response delay

## Supporting Material/References:
See attached screenshot

## Impact

Causes an attacker to obtain database information

## Attachments
- 2019-12-19_09-22-37______.png
- 2019-12-19_09-24-27______.png
