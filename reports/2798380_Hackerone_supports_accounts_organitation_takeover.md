# Hackerone supports accounts organitation takeover

## Report Details
- **Report ID**: 2798380
- **URL**: https://hackerone.com/reports/2798380
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-10-23T04:48:38.492Z
- **Disclosed**: 2024-11-19T03:49:09.339Z

## Reporter
- **Username**: madara_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
## Description:
- I have discovered a vulnerability in HackerOne's email change process where the system automatically verifies the email address if the verification link is opened in any browser. This behavior differs from report #2128237, as it affects specific situations where email scanning bots automatically open links without human interaction.

- The issue arises because some email services, such as security bots that scan emails and analyze links, automatically open verification links. In certain cases, these bots do not validate whether the email originates from a "no-reply" address or another that should prevent verification. By exploiting this behavior, an attacker can verify email addresses without the legitimate owner’s interaction, allowing them to register email addresses as if they belong to a specific company.

## Reproduction Steps:
1. Register an account on HackerOne with any valid email address.
2. Change the email of the account to one belonging to a company that uses email scanning bots (e.g., certain security solutions). example ██████
3. If the email system of the target automatically scans the link without properly checking the email nature, the email address will be verified without any human action.
4. This allows the attacker to use a fake corporate email address without the legitimate owner’s consent.

- In this case, HackerOne attempts to request SAML authentication, but you bypass it, allowing you to log in to other services like PullRequest.com under the affected company’s identity.


## Attachments
No attachments
