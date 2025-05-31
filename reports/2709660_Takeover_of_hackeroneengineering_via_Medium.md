# Takeover of hackerone.engineering via Medium 

## Report Details
- **Report ID**: 2709660
- **URL**: https://hackerone.com/reports/2709660
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-09-10T01:25:12.032Z
- **Disclosed**: 2024-11-14T15:54:25.476Z

## Reporter
- **Username**: raditz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi HackerOne Team!

==**NOTE: I'm redoing the report because the last one wasn't looked at correctly #2705602 and the report was closed, so don't close it as duplicate, just see that the takeover on the hackerone page happened. **==

**Just click on the link: https://hackerone.engineering and see the Takeover. (We made the PoC)**

## Summary

During a Recon at HackerOne it was possible to identify a **Broken Link Hijacking** vulnerability, in which the [hackerone.engineering](https://hackerone.engineering) domain that belongs to HackerOne pointed to a non-existent page on Medium returning a 404 status code, and due to this ==it was possible to do the HackerOne Takeover==.

{F3588031}

## Description

During a Recon I discovered that HackerOne has a domain `hackerone.engineering` that belongs to HackerOne itself that was not mentioned within the scope, ==but at the same time it was not mentioned outside the scope==.

I discovered that the domain [hackerone.engineering](https://hackerone.engineering) was used by HackerOne as a company blog through evidence on the [Wayback Machine](https://web.archive.org/). Below I will leave screenshots and URL to prove that it really belongs to HackerOne.

### Whois

{F3588038}

### Wayback Machine

{F3588045}
{F3588046}

URL: https://web.archive.org/web/20220126180109/https://hackerone.engineering/

### HackerOne's own report

#2085260 - Report on [hackerone.engineering](https://hackerone.engineering ) 

{F3588052}

Based on this information, it was possible to deduce that the domain actually belongs to HackerOne. When I accessed the [hackerone.engineering](https://hackerone.engineering) domain, I was redirected to a page on medium that didn't exist.

**[https://hackerone.engineering](https://hackerone.engineering) ===> [https://medium.com/hackerone-engineering](https://medium.com/hackerone-engineering) (404 Not Found)**

{F3588058}

Since the Medium page doesn't exist, I was able to create the page with the same Medium news reference, ==Successfully Hijacking the Broken Link!==

## Broken Link Hijacking

{F3588031}

{F3588067}

## Steps to Reproduce

1. Just click on the link: https://hackerone.engineering
2. See what happened at the Takeover on the HackerOne Page.

{F3588031}

## Impact

The attacker can control the new content of the broken link and create a page that looks legitimate. This allows them to carry out phishing attacks or promote fake job openings, which also damages HackerOne's reputation.

Kind Regards.

## Attachments
- image.png
- image_(1).png
- image_(2).png
- image_(3).png
- image.png
- image_(4).png
- hijacked.mp4
