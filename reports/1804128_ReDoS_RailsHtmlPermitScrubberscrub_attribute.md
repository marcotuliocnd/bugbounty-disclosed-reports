# ReDoS (Rails::Html::PermitScrubber.scrub_attribute)

## Report Details
- **Report ID**: 1804128
- **URL**: https://hackerone.com/reports/1804128
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-12-14T10:10:23.563Z
- **Disclosed**: 2022-12-14T22:51:27.924Z

## Reporter
- **Username**: ooooooo_q
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
I reported at  https://hackerone.com/reports/1684163

https://github.com/rails/rails-html-sanitizer/security/advisories/GHSA-5x79-w82f-gw8w

> Certain configurations of rails-html-sanitizer < 1.4.4 use an inefficient regular expression that is susceptible to excessive backtracking when attempting to sanitize certain SVG attributes. This may lead to a denial of service through CPU resource consumption.

It seems that the same problem existed on the Loofah side, so it was fixed as well. That has been fixed as CVE-2022-23514(https://github.com/flavorjones/loofah/security/advisories/GHSA-486f-hjj9-9vhh)

## Impact

ReDoS may occur if scrub is executed in Rails::Html::PermitScrubber.

## Attachments
No attachments
