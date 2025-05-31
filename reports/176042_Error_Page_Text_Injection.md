# Error Page Text Injection

## Report Details
- **Report ID**: 176042
- **URL**: https://hackerone.com/reports/176042
- **State**: Closed
- **Severity**: none
- **Submitted**: 2016-10-15T19:43:55.206Z
- **Disclosed**: 2017-11-09T20:11:37.669Z

## Reporter
- **Username**: r0h17
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
Hello Yelp team,

Description :

An attacker is able to inject his own text into error page and can fool the victim to visit his own malicious site.
Please take a look at attached document, it contains POC as well as attack scenario about how the attacker can exploit this vulnerability and mitigation.

POC URL: 

https://biz.yelp.com/%0A%0D*%20The%20web%20page%20you%20are%20trying%20to%20access%20has%20been%20moved%20to%20https://login.yelp.biz%20*/

OR

https://biz.yelp.com@goo.gl/LBwo5y

Regards,
Rohit

## Attachments
- Error_Page_Injection_biz_yelp.docx
