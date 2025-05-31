# Content-Injection/XSS ████

## Report Details
- **Report ID**: 205360
- **URL**: https://hackerone.com/reports/205360
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-02-10T21:22:56.618Z
- **Disclosed**: 2019-12-02T18:39:38.310Z

## Reporter
- **Username**: c0rte
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**

Hi,

It is possible to inject content and vulnerable to reflected Cross Site Scripting.
Affected domain: https://██████████
Used browser: Mozilla.


## Impact

One of the most common XSS attack vectors is to hijack legitimate user accounts by stealing their session cookies. This allows attackers to impersonate victims and access any sensitive information or functionality on their behalf. Let's dissect how this can be achieved.

An attacker could inject fake login forms and ask for military credentials.

## Step-by-step Reproduction Instructions

1. XSS: https://██████/images.ashx?loc=%3C/div%3E%3Cimg%20src=%22youtube.com%22%20onerror=alert(%22TestingXSS%22)%3E

2. Content Injection: https://██████/images.ashx?loc=%3C/div%3E%3Cimg%20src=%22https://███.files.wordpress.com/2016/12/facebook-instagram-open-redirect.jpeg%22%3E

## Suggested Mitigation/Remediation Actions

Sanitize your input, by escaping HTML special characters.

Thanks,
Diogo Real

## Attachments
No attachments
