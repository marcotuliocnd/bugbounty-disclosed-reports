# No rate limiting for confirmation email, can spam anyone with confirmation emails

## Report Details
- **Report ID**: 245147
- **URL**: https://hackerone.com/reports/245147
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-07-01T16:34:22.548Z
- **Disclosed**: 2017-07-03T16:51:02.039Z

## Reporter
- **Username**: pratyushjanghel
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
Hello, there is no rate limiting implemented in sending the confirmation email. Thus, attacker can use this vulnerability to bomb out the email inbox of the victim.

Proof of Concept :

1. Register a account  in wakatime.com
2. Login to account and go to https://wakatime.com/settings/account
3.  Under that click on send confirmation email to any email you want and capture that request with burp.
4. Now you can use the intruder and repeat the request by using different payloads under User Agent.
5. Check the email inbox, it will be bombed with lots of email.

{F199308}

Reference from : #87531

Hope, you fix this soon.

Best Regards,
Pratyush Janghel

## Attachments
- wakatime1.png
