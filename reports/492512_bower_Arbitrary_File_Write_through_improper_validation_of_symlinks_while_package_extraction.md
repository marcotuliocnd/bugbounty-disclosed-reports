# [bower] Arbitrary File Write through improper validation of symlinks while package extraction

## Report Details
- **Report ID**: 492512
- **URL**: https://hackerone.com/reports/492512
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-02-07T16:09:07.914Z
- **Disclosed**: 2019-09-10T20:21:52.042Z

## Reporter
- **Username**: skyn3t
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Hi,

I want to submit my report https://hackerone.com/reports/473811 for the Internet Bug Bounty.
Snyk's writeup: https://snyk.io/blog/severe-security-vulnerability-in-bowers-zip-archive-extraction

**My assessment on why this report might be eligible:**
>To qualify, vulnerabilities must meet the following criteria:

- Be implementation agnostic: vulnerability is present in implementations from multiple vendors or a vendor with dominant market share. Do not send us vulnerabilities that only impact a single website, product, or project.

*Bower is one of the top package managers for nodejs ecosystem with many major companies dependent on it as cited by https://stackshare.io/stackups/bower-vs-npm-vs-yarn*

- Be open source: finding manifests itself in at least one popular open source project. **✔️**

>In addition, vulnerabilities should meet most of the following criteria:

- Be widespread: vulnerability manifests itself across a wide range of products, or impacts a large number of end users

*Bower has ~2 million monthly downloads according to [Snyk's report](https://snyk.io/blog/severe-security-vulnerability-in-bowers-zip-archive-extraction) with official npm stats showing 355k+ downloads the past week.*

{F419777}

- Have critical impact: vulnerability has extreme negative consequences for the general public.  **✔️**
- Be novel: vulnerability is new or unusual in an interesting way. **～**

What do you think?

Regards,
Skynet (skyn3t)

## Impact

Writing arbitrary files on the system

## Attachments
- bower-stats.png
