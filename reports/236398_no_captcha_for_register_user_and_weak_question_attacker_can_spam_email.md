# no captcha for register user and weak question attacker can spam email

## Report Details
- **Report ID**: 236398
- **URL**: https://hackerone.com/reports/236398
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-06-04T10:01:49.028Z
- **Disclosed**: 2019-10-26T07:37:59.257Z

## Reporter
- **Username**: fr0nk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
hi
in https://demo.weblate.org/accounts/register/ attacker can register with same email and if didnt click on confirm link attacker can make request with infinite loop

so attacker can spam another email with your service

question is so simple any bot that can read source can generate answer for it

you can make fix with if email register in database user cant make register request within 24 hour

good luck


## Attachments
No attachments
