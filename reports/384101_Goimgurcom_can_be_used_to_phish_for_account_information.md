# Go.imgur.com can be used to phish for account information

## Report Details
- **Report ID**: 384101
- **URL**: https://hackerone.com/reports/384101
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-07-19T10:17:46.443Z
- **Disclosed**: 2018-09-21T06:39:25.238Z

## Reporter
- **Username**: kiyell
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: imgur

## Vulnerability Information
Right now the **go.imgur.com** domain is pointing to `godoc.org/go.imgur.com` but there is nothing at this resource. It is possible with encoded double dots to redirect **go.imgur.com** URLs to pages that phish for imgur account information.

Proof of Concept
===

PoC 1:
###
`http://go.imgur.com/account-verification/%252e%252e%2f%252e%252e%2f%67%69%74%68%75%62%2e%63%6f%6d%2f%6b%69%79%65%6c%6c%2f%70%71`

In this example the URL is customized to appear more legitimate.
Resulting page: F322182



PoC 2: 
###
`http://go.imgur.com/account-verification/%252e%252e%2f%252e%252e%2f%67%69%74%68%75%62%2e%63%6f%6d%2f%6b%69%79%65%6c%6c%2f%70%71%23%68%64%72%2d%57%41%52%4e%49%4e%47%5f%5f%5f%49%4d%50%4f%52%54%41%4e%54%5f%41%43%43%4f%55%4e%54%5f%49%4e%46%4f%52%4d%41%54%49%4f%4e`

In this longer example, code was added that adds emphasis to the phishing message.
Resulting page: F322181

## Impact

An attacker could mass email users for their account information or could use this vulnerability as part of another type of social engineering campaign against Imgur partners and customers.

## Attachments
- imgur_phishing_long_url.JPG
- imgur_phishing_short_url.JPG
