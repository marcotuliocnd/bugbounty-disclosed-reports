# Information disclosure-Referer leak

## Report Details
- **Report ID**: 1337624
- **URL**: https://hackerone.com/reports/1337624
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-09-12T19:40:55.938Z
- **Disclosed**: 2022-02-01T19:32:16.611Z

## Reporter
- **Username**: kkarfalcon
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
Assigned to: Brave
Assigned by: Kirtikumar Anandrao Ramchandani
Assigned on: 13/09/2021
Browser information used to test (Up to date):
```
Brave	1.29.79 Chromium: 93.0.4577.63 (Official Build) (64-bit)
Revision	ff5c0da2ec0adeaed5550e6c7e98417dac77d98a-refs/branch-heads/4577@{#1135}
OS	Windows 10 OS Version 2009 (Build 19043.1165)
```

Vulnerability name: Information Disclosure
Vulnerability description: Brave browser has a function of    `New Private Window with Tor`. The browser when used with Tor shouldn't leak the referer.
Steps to reproduce:
1. Visit [exploit].
2. Click on `https://www.whatismybrowser.com/`.

Expected behavior: It should have shown a blank `referrer`
Actual behavior: It shows the referrer as: `kirtikumarar.com` which was the host from where we navigated

To know expected behavior, please refer to the below screenshot:
{F1445735}

Video POC showing the expected behavior can be found below:

{F1445736}

[exploit]: https://kirtikumarar.com/referrer/top-page.html

## Impact

1. This will leak users information
2. In the Tor network, we don't have common URLs as we have in the browsers. They usually are something like `dhxnafkaxlxdnackeudxdca.onion`, those can be leaked.

## Attachments
- referrer.PNG
- F-Secure_SAFE.mp4
