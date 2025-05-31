# Verification of E-Mail address possible on https://biz.yelp.com/login and https://biz.yelp.com/forgot

## Report Details
- **Report ID**: 166265
- **URL**: https://hackerone.com/reports/166265
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-06T20:29:41.312Z
- **Disclosed**: 2016-10-27T17:39:43.075Z

## Reporter
- **Username**: badagent
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
On pages https://biz.yelp.com/login and https://biz.yelp.com/forgot a malicious user can verify if a particular E-mail address is registered on biz.yelp.com.

Steps to reproduce for https://biz.yelp.com/login:
1. Open https://biz.yelp.com/login
2. Enter non existing E-Mail Address
3. Enter any password
4. Submit form
5. Result: The error message discloses, that the submitted E-Mail address is not known. 

Steps to reproduce for https://biz.yelp.com/forgot:
1. Open https://biz.yelp.com/forgot
2. Enter non existing E-Mail Address
4. Submit form
5. Result: The error message discloses, that the submitted E-Mail address is not known. 

An attacker can try different E-Mail addresses and can test if they are registered or not, helping him in a brute-force attack.

## Attachments
- cap1.png
- cap2.png
