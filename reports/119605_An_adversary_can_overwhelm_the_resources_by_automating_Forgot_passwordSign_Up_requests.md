# An adversary can overwhelm the resources by automating Forgot password/Sign Up requests

## Report Details
- **Report ID**: 119605
- **URL**: https://hackerone.com/reports/119605
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-03-01T01:27:39.001Z
- **Disclosed**: 2016-07-24T03:40:20.949Z

## Reporter
- **Username**: roshanpty
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: coinbase

## Vulnerability Information
As Coinbase doesn't use CAPTCHA on publicly available forms such as 'Forgot Password' & 'Sign Up' , the requests can be automated to overwhelm the resources to result in denial of service for CoinBase or mail flooding of customers.

The steps to reproduce the issue are as follows.

Step 1: Browse to https://www.coinbase.com/password_resets/new
Step 2: Enter a valid user email ID and click on Reset Password
Step 3: Capture the request in burp and send the request to repeater. Repeat the request several times.
Step 4: Open the mail client and check the inbox. It can be observed that the several password reset emails are present in the inbox.

## Attachments
- CB2.png
- CB1.png
