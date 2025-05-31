# Subdomain Takeover at https://new.rubyonrails.org/

## Report Details
- **Report ID**: 1429148
- **URL**: https://hackerone.com/reports/1429148
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-12-16T21:21:48.610Z
- **Disclosed**: 2022-03-03T21:12:32.473Z

## Reporter
- **Username**: nagli
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
## Disclaimer

I know it's OOS but the issue is pretty serious because of the attractive domain name "new.rubyonrails.org" basically anyone could have put malware there.

## Summary
Hi!

I discovered that new.rubyonrails.org was pointing to an unclaimed Github Page, making it vulnerable to subdomain takeover.
I've managed to claim it in my Github-account and added a simple html file as POC:

{F1548667}

`https://new.rubyonrails.org`

## Mitigation
- Remove the DNS record

Best regards,
nagli

## Impact

Subdomain takeovers can be used for
- Cookies set to the root domain will be shared with this subdomain and can be obtained
- Stored XSS (arbitrary javascript code can be executed in a users browser)
- Phishing
- Hosting malicious content

## Attachments
- Screen_Shot_2021-12-16_at_23.12.09.png
