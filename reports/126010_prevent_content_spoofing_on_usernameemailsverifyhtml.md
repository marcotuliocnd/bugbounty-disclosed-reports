# prevent content spoofing on /~username/emails/verify.html

## Report Details
- **Report ID**: 126010
- **URL**: https://hackerone.com/reports/126010
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-03-25T18:29:48.055Z
- **Disclosed**: 2017-07-10T09:59:30.350Z

## Reporter
- **Username**: a5tronaut
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
**Steps to Verify:**
1. Login to your Gratipay account.
2. Now navigate to the following url 

``````
https://gratipay.com/~your_username/emails/verify.html?email=your%20account%20has%20expired.%20You%20must%20renew%20it%20to%20use%20your%20account.%20To%20continue%20you%20have%20to%20send%20your%20login%20credentials%20to%20attacker@mail.com.%20A%20Gratipay%20executive%20will%20contact%20you%20after%20that.%20Sorry%20for%20this%20intereption,%20we%20know%20this&nonce=x
``````
 POC screenshot attached.

Regards
Uttam

## Attachments
- gratipay_content_spoofing.png
