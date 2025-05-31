# Gitlab.com is vulnerable to reverse tabnabbing via AsciiDoc links. (#3)

## Report Details
- **Report ID**: 213114
- **URL**: https://hackerone.com/reports/213114
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-03-13T16:17:14.804Z
- **Disclosed**: 2017-05-09T19:11:56.301Z

## Reporter
- **Username**: edoverflow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Dear GitLab bug bounty team,

# Summary
---
Gitlab.com is vulnerable to reverse tabnabbing in AsciiDoc files. 

# Why does this vulnerability exist?
---

In AsciiDoc the following `http://example.com[Reverse Tabnabbing^]` is equivalent to `<a href="http://example.com" target="_blank">Reverse Tabnabbing</a>`.

# How can this exploited?
---

Same scenario as https://hackerone.com/reports/211065. ;)

Best regards,
Ed



## Attachments
No attachments
