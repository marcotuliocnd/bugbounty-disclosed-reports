# Link poisoning on https://secure.login.gov/ login page

## Report Details
- **Report ID**: 299835
- **URL**: https://hackerone.com/reports/299835
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-12-21T15:13:50.828Z
- **Disclosed**: 2019-03-25T18:06:44.434Z

## Reporter
- **Username**: albinowax
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_bbp

## Vulnerability Information
This link leads to the genuine secure.login.gov login page, in French: 
https://secure.login.gov/fr?host=portswigger.net

However, if you try to change the language to English using the bar at the bottom you'll end up an external website of my choice. As users won't expect changing their language to place them on an external website, the attacker could launch a highly effective phishing attack from there by impersonating secure.login.gov

## Impact

This vulnerability makes it possible to launch phishing attacks originating from secure.login.gov

## Attachments
No attachments
