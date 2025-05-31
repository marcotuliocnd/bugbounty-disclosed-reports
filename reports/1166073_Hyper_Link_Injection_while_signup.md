# Hyper Link Injection while signup 

## Report Details
- **Report ID**: 1166073
- **URL**: https://hackerone.com/reports/1166073
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-04-15T22:42:45.175Z
- **Disclosed**: 2022-06-15T10:04:14.051Z

## Reporter
- **Username**: 011alsanosi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: upchieve

## Vulnerability Information
## Summary:
Attacker can add their name to a URL in order to send email  containing malicious hyperlinks. while signup  

## Steps To Reproduce:
1-Go to https://app.upchieve.org and create account  with the first name ```http://attacker.com/ ``` and last name .
2-Now check  your email  and you notice there is malicious hyperlinks.
█████████

## Supporting Material/References:

█████

## Recommendations for Fixing/Mitigation
 Validate users input

## Impact

This permits users to send malicious/phishing links to potential clients. It could also have an effect on how spam filters treat ```app.upchieve.org``` emails.

## Attachments
No attachments
