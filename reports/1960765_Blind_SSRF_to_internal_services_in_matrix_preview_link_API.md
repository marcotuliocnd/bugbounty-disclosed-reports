# Blind SSRF to internal services in matrix preview_link API

## Report Details
- **Report ID**: 1960765
- **URL**: https://hackerone.com/reports/1960765
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-04-24T21:33:47.872Z
- **Disclosed**: 2023-04-26T15:42:47.191Z

## Reporter
- **Username**: la_revoltage
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
## Summary:
Reddit' new chat is based on Matrix software which has preview_link functionality which doesn't filter the URL before sending the request

## Impact:
Attacker can enumerate services by grabbing og:title and port scanning, also possible RCE escalation (Asking for permission on this one)

## Steps To Reproduce:


  1. Visit the https://matrix.redditspace.com/_matrix/media/r0/preview_url/?url=*
  2. Replace * with http://██████ to get og:title ███████
  3. Replace * with http://█████████ to get og:title ███████
 4. Replace * with http://██████████to get og:title ██████
 5. Replace * with ████████ to get og:title █████████

Note: If the request is stuck and not responding in 2 seconds reload the page until it does

## Permit for escalation attempt? 
Since the ███ URL is accessible it may be possible to run ███:
GET █████████

There are also possibilities to test ██████, but I thought that it would be incorrect to do such activity without permission and as such report vulnerability in this state. I also therefore request a permission to try to escalate this to Critical

## Impact

Attacker can enumerate services and launch attacks against them

## Attachments
No attachments
