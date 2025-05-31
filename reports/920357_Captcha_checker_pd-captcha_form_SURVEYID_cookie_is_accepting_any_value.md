# Captcha checker "pd-captcha_form_SURVEYID" cookie is accepting any value

## Report Details
- **Report ID**: 920357
- **URL**: https://hackerone.com/reports/920357
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-07-09T22:18:21.401Z
- **Disclosed**: 2020-11-18T14:21:27.551Z

## Reporter
- **Username**: bugra
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
Hi team,
There is a `Captcha protection` feature on surveys and polls. If you captcha protection enabled survey, you will see this :
{F901789}

When you solve captcha and click `Submit Captcha`, website sets a cookie like this :
{F901799}

And if you delete this cookie and try access to survey, you will see captcha again. But if you change value of this cookie, you can access still. 
So any attacker can bypass this restriction via typing random value to cookie.

## Steps To Reproduce:

  1. Go to a captcha protected survey or poll
  1. Solve the captcha and click `Submit Captcha`
  1. Now change the value of `pd-captcha_form_SURVEYID` cookie to random value from browser's console.
  1. Refresh the page and you will see you can access to survey and submit the survey.

## Impact

Bypassing captcha protection on surveys and polls

Thanks,
Bugra

## Attachments
- captcha.PNG
- cookie.PNG
