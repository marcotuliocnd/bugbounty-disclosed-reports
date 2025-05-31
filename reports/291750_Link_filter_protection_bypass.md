# Link filter protection bypass

## Report Details
- **Report ID**: 291750
- **URL**: https://hackerone.com/reports/291750
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-11-19T21:27:22.907Z
- **Disclosed**: 2018-05-09T22:24:05.700Z

## Reporter
- **Username**: ramsexy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: valve

## Vulnerability Information
## Description
Hi, there is a protection bypass in the linkfilter function. By using the character 。 (%E3%80%82 url encoded) instead of a normal dot in urls, it is possible to bypass the blocking.

## PoC
Normal request : https://steamcommunity.com/linkfilter/?url=pornhub.com

{F240919}

Bypass : https://steamcommunity.com/linkfilter/?url=pornhub%E3%80%82com

{F240920}

## Attachments
- normal.png
- bypass.png
