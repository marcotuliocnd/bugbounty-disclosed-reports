# Open redirect via redirect_to parameter in tumblr.com

## Report Details
- **Report ID**: 2812583
- **URL**: https://hackerone.com/reports/2812583
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-10-30T17:51:38.266Z
- **Disclosed**: 2024-11-05T07:16:14.971Z

## Reporter
- **Username**: shivangmauryaa
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
URL redirection is sometimes used as a part of phishing attacks that confuse visitors about which web site they are visiting.

## Platform(s) Affected:
Website 

## Steps To Reproduce:
1. open any browser 
2. enter https://www.tumblr.com/logout?redirect_to=https://evil.com%5C%40www.tumblr.com

## Supporting Material/References:
video attached

## Impact

A remote attacker can redirect users from your website to a specified URL. This problem may assist an attacker to conduct phishing attacks, trojan distribution, spammers.

## Attachments
- recording-1730310637082.webm
