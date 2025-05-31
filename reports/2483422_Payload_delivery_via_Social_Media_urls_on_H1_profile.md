# Payload delivery via Social Media urls on H1 profile

## Report Details
- **Report ID**: 2483422
- **URL**: https://hackerone.com/reports/2483422
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-04-29T20:49:25.387Z
- **Disclosed**: 2024-07-23T12:28:09.277Z

## Reporter
- **Username**: tedix
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
HackerOne allows users to add social media profiles to their HackerOne profile via the [profile/edit](https://hackerone.com/settings/profile/edit) page. Users are allowed to provide their username. Due to improper sanitization, users are allowed to construct their own URLs (except Twitter, which is sanitized and shows inconsistency in security controls). This allows hackers to hide malicious payloads behind the social media buttons on their profile, such as malicious .zip files. 

Twitter is sanitized:
{F3232660}

The other Social media platforms are not:
{F3232662}

### Steps To Reproduce
1. Visit [profile/edit](https://hackerone.com/settings/profile/edit)
2. Construct your own payload using the handles.
3. Visit [Tedix](https://hackerone.com/tedix?type=user) profile, click the GitHub button. An .zip file will be downloaded immediately. 

{F3232688}

This violates HackerOne's protection which provides users with an alert prior to files being downloaded (e.g. files added to reports). 

In the POC on my profile, I have deployed a 'harmless' .zip file. However, this could be a [WinRAR zero day](https://www.bleepingcomputer.com/news/security/winrar-zero-day-exploited-since-april-to-hack-trading-accounts/) or other kind of malicious executable.

## Impact

Attackers are able to construct their own payloads, as long these are below 25 characters. These can be used for payload delivery, redirect, xss or abuse of other vulnerabilities/gadgets at the social platfoms.

## Attachments
- twitter.png
- github.png
- payload.png
