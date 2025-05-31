# User input validation can lead to DOS

## Report Details
- **Report ID**: 767458
- **URL**: https://hackerone.com/reports/767458
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-01-03T04:16:25.795Z
- **Disclosed**: 2020-03-26T23:00:35.357Z

## Reporter
- **Username**: meepmerp
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hi Security Team,

**Summary:** 
There is no limit to the number of characters on phone numbers and using this you can perform a DOS Attack

**Description:**
On the input form of phone number in ***https://twitter.com/account/complete*** there's no Input validation using this you can send more payload and may cause of Denial of service or **503 Service Temporarily Unavailable**

## Steps To Reproduce:

So this is the normal page 
█████████

Input this payload on the Phone number textbox ████ then submit as you can see the payload was encoded on backend so the payload may load more

████

After submitting this is the response on burp **503 Service Temporarily Unavailable**

█████████

And on the page this is the result .

████████

## Supporting Material/References:

+ payload.txt

Thank you! 
Regards

## Impact

Attacker can perform a DOS because of lack of input validation

## Attachments
No attachments
