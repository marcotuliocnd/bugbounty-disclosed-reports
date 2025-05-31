# Stored xss in address field in billing activity at https://shop.aaf.com/Order/step1/index.cfm

## Report Details
- **Report ID**: 411690
- **URL**: https://hackerone.com/reports/411690
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-09-20T09:00:49.170Z
- **Disclosed**: 2019-05-25T09:08:06.032Z

## Reporter
- **Username**: gujjuboy10x00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: aaf

## Vulnerability Information
Dear Team,

**Summary:** [add summary of the vulnerability]
After looking into https://shop.aaf.com/Order/step1/index.cfm i get to know that there is address field is vulnerable to stored xss which can lead to steal any user's cookie and can lead to complete account takeover

**Description:** [add more details about this vulnerability]

## Steps To Reproduce:

  1. go to https://shop.aaf.com and click on any products , tshirt
  2. add that in cart and click on proceed
  3. enter xss payload (a"><svg/onload=prompt(1)> ) in every address field and click on OK proceed
  4. xss will popup 

## Supporting Material/References:

XSS OWASP

Thanks,
Vishal

## Impact

Stored xss in address field in billing activity at https://shop.aaf.com/Order/step1/index.cfm

## Attachments
- xss_aaf.PNG
