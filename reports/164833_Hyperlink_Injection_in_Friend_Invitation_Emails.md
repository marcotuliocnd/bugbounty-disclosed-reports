# Hyperlink Injection in Friend Invitation Emails

## Report Details
- **Report ID**: 164833
- **URL**: https://hackerone.com/reports/164833
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-31T20:08:40.066Z
- **Disclosed**: 2016-10-07T11:35:54.715Z

## Reporter
- **Username**: corb3nik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: algolia

## Vulnerability Information
## Description 

A user can change their last name to a URL in order to send email invitations containing malicious hyperlinks.

## Steps to Reproduce
1. Create a new Algolia account with the last name `http://example.com`.
2. Navigate to `My Account > Referrral`
3. Send an invitation to an email address that you control

You will receive a new email with the last name being a link to a potentially malicious site.

## Consequences
This permits users to send malicious/phishing links to potential clients. It could also have an effect on how spam filters treat algolia.com emails.

## Attachments
- proof.png
