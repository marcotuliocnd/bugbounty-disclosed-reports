# No Rate Limit protection in user subscription form

## Report Details
- **Report ID**: 1195429
- **URL**: https://hackerone.com/reports/1195429
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-05-13T09:59:22.892Z
- **Disclosed**: 2021-05-14T16:58:48.279Z

## Reporter
- **Username**: aliyugombe
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
## Summary:
Hello
I found your form that user can subscribe for any update has no rate limit protection.

##Step to reproduce
1. Visit http://sifchain.finance and move to subscribe form and enter email
2. click on `sign-up` button.
3. use burpsuite to intercept the request and send to intruder.
4. Clear payload 
5. Select null payload and enter 10 in generate payload field.
6. Click on start attack.
7. You will see all the request have 200 response code (Means ok and send)
8. Check your email you will see 10 emails form sifchain asking you to confirm your subscription

 
## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

Attacker can use this vulnerability to do email bombing attack to any victim's email.
While if you are using third-party service to send this mail, you will be charge for sending those mails

## Attachments
- sifchain1.PNG
- sifchain2.PNG
