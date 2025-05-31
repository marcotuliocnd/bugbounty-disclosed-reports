# Cache poisoning for okhttp 

## Report Details
- **Report ID**: 137756
- **URL**: https://hackerone.com/reports/137756
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-11T06:54:13.587Z
- **Disclosed**: 2016-08-31T04:05:23.772Z

## Reporter
- **Username**: nvolcz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: square-open-source

## Vulnerability Information
If an attacker can control the Host header this can be used to poison the cache. This becomes extra dangerous if the library were to be used to build a caching proxy.

## Attachments
- Cache_poisoning_for_okhttp.pdf
