# Hyperlink Injection in Friend Invitation Emails

## Report Details
- **Report ID**: 158554
- **URL**: https://hackerone.com/reports/158554
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-11T19:23:55.377Z
- **Disclosed**: 2016-09-12T19:59:24.395Z

## Reporter
- **Username**: corb3nik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: instacart

## Vulnerability Information
## Description

A user can change their name to a URL in order to send email invitations containing malicious hyperlinks.

# Steps to Reproduce

1. Create a new Instacart account with the first name `http://example.com`
2. Navigate to [https://www.instacart.com/store/referrals](https://www.instacart.com/store/referrals)
3. Send an email invitation to an email address that you control

You will receive a new email with the first word being a link to a potentially malicious site.

# Consequences

This permits users to send malicious/phishing links to potential clients. It could also have an effect on how spam filters treat `instacart.com` emails.

## Attachments
- proof.png
