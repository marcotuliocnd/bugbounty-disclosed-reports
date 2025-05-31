# DOM-Based XSS in tumblr.com

## Report Details
- **Report ID**: 949382
- **URL**: https://hackerone.com/reports/949382
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-08-01T20:04:10.401Z
- **Disclosed**: 2021-02-02T21:38:45.747Z

## Reporter
- **Username**: keer0k
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
# Description

Hi, i would like to report DOM-Based XSS that it's exactly like this one #882546, this one work just because  the page /reblog/ID/OTHER_ID doesn't have a correct CSP rule.

# Steps to reproduce
1. go to `https://www.tumblr.com/reblog/620008931446652928/JBuEvzz5`
2. click in `click me`
3. click in open
4. XSS will be triggered

## Impact

it is possible to perform malicious actions on the victim's account

## Attachments
No attachments
