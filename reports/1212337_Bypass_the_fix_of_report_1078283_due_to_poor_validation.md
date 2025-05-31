# Bypass the fix of report #1078283 due to poor validation

## Report Details
- **Report ID**: 1212337
- **URL**: https://hackerone.com/reports/1212337
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-05-29T02:29:33.525Z
- **Disclosed**: 2021-07-08T19:25:27.515Z

## Reporter
- **Username**: wlucenasec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: khanacademy

## Vulnerability Information
Hi Khan Academy Team,

I was able to bypass the fix you implemented for report #1078283. 

The URL validation you implemented on the endpoint `continue` checks the presence of `khanacademy.org` however it doesn't have any boundary checking to ignore domains starting with `.org`, so if an attacker register a domain starting with `org` like this one `orghacker.com.br` and have a subdomain entry of `khanacademy` the attacker is able to bypass the current implementation and lead the victim to his controlled page.

# Steps to reproduce the issue

* Go to this page https://www.khanacademy.org/signup?isteacher=1&referral=LearnStorm&continue=https://khanacademy.orghacker.com.br
* You'll be redirected to `orghacker.com.br` which is not a domain that Khan Academy owns

## Impact

Bypass of current URL validation. Attacker can send a phishing campaign and redirect the request to a server of his control. An attacker might chain the attack to other types of attack too.

## Attachments
No attachments
