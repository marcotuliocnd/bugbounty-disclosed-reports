# Modify Host Header which is sent to email

## Report Details
- **Report ID**: 791293
- **URL**: https://hackerone.com/reports/791293
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-02-08T18:40:32.664Z
- **Disclosed**: 2020-02-12T12:24:39.537Z

## Reporter
- **Username**: codermak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: endless_group

## Vulnerability Information
## Summary:
Modify host header and include the fake website in password reset email.  Password reset mail is taking source domain from request header host, which can be modified using burp suite and the modified link is sent to the victims email

## Steps To Reproduce:

  1. Go to  https://da.theendlessweb.com:2222/
  2. Start burp suite
  3. Enter username and click on Send me a Link
  4. Intercep the request and modify the URL to some other custom url
  5. Forward the modified request
  6. Password reset email will be sent.
  7. Check your email and you will see the new url (which was configured in step 4) in the email.

## Supporting Material/References:

  * Snapshots in attachment

## Impact

With this, attacker can make any victim to visit their custom website and can affect the victim in many ways

## Attachments
- email-hosting.png
- Screen_Shot_2020-02-09_at_12.06.31_AM.png
