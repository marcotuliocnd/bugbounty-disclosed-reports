# Use After Free/Double Free in Garbage Collection

## Report Details
- **Report ID**: 152281
- **URL**: https://hackerone.com/reports/152281
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-19T12:15:08.141Z
- **Disclosed**: 2019-10-13T11:08:45.357Z

## Reporter
- **Username**: ryat
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
https://bugs.php.net/bug.php?id=72605

I don't know if the bug is qualified.

I reported this bug since php some guys added this commit: https://github.com/php/php-src/commit/1c84b55adea936b065a20102202bea3d1d243225
Then they had reverted this commit before PHP updates release: https://github.com/php/php-src/commit/171c759d791f809ebc31711fd0b0b5bb632cd2cc
So I think this bug have been fixed. if I don't submit this bug until php updates release, then this bug will be tagged as `Type: Security` and fix in next PHP updates release.

## Attachments
No attachments
