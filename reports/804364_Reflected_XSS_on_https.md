# Reflected XSS on https://███████/

## Report Details
- **Report ID**: 804364
- **URL**: https://hackerone.com/reports/804364
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-02-25T10:49:54.642Z
- **Disclosed**: 2020-07-30T17:53:19.370Z

## Reporter
- **Username**: the_unlucky_guy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**

Hey Team,

There is reflected xss on https://█████/kinetic/ when certain action results in 404 error.

**Description:**

I am using some random strings paths after kinetic in https://███████/kinetic/ if that path is not exist then it says 404 not found. Strings is not sanitized after kinetic/ due to which any one can able to use Java Script code after kinetic/ and it executed successfully leads to reflected xss.

## Impact

The attacker can able to execute JS code.

## Step-by-step Reproduction Instructions

1. open this  https://████████/kinetic/1%3C!--%3E%3CSvg%20OnLoad=(confirm)(document.domain)--%3E/ in firefox
2. You will get alert pop up.

## Product, Version, and Configuration (If applicable)

## Suggested Mitigation/Remediation Actions

Sanitize string

## Impact

The attacker can able to execute JS code.

## Attachments
No attachments
