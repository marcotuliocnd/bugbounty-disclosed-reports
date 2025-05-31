# Reflected XSS on vimeo.com/musicstore

## Report Details
- **Report ID**: 85615
- **URL**: https://hackerone.com/reports/85615
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-08-30T03:49:15.449Z
- **Disclosed**: 2017-08-31T10:29:49.014Z

## Reporter
- **Username**: stefanovettorazzi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: vimeo

## Vulnerability Information
__Description__

The value of the parameter _section_ is reflected in the Javascript function `MusicStoreCommon.initialize()` without escaping, which allows to insert Javascript code.

__Proof of concept__
1. Go to https://vimeo.com/musicstore?section=%27-alert(document.domain)-%27.
2. `alert(document.domain)` is executed.

This reflected XSS is reproducible on Chrome, Safari and Firefox.

## Attachments
No attachments
