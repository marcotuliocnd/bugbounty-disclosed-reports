# Captcha bypass at registration

## Report Details
- **Report ID**: 229584
- **URL**: https://hackerone.com/reports/229584
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-05-18T10:26:39.869Z
- **Disclosed**: 2017-06-28T02:12:30.956Z

## Reporter
- **Username**: proabiral
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
### Affected URL:
https://demo.weblate.org/accounts/register/

### Issue:
The captchas are implement so that the site can differentiate between the legitimate user and the bot. The captcha challenge should be something that a bot cannot solve easily and a human could easily solve. However, in the above URL captcha is simple enough that can be read by any script. 
An attacker can write a simple script to get value of those captcha ( as simple as `document.getElementById("div_id_captcha")` in JS ) and solve them.

### Solution:
Image captcha should be implemented whose value cannot be read by script.
Google captcha can be an effective solution.

## Attachments
No attachments
