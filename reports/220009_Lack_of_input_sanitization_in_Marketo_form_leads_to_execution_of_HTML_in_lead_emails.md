# Lack of input sanitization in Marketo form leads to execution of HTML in lead emails

## Report Details
- **Report ID**: 220009
- **URL**: https://hackerone.com/reports/220009
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-04-10T18:01:11.363Z
- **Disclosed**: 2017-10-03T17:35:47.477Z

## Reporter
- **Username**: encrypt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi,
There is SSRF vulnerability due to img tag injection in "Contact HackerOne Sales" form. Since vulnerability triggers after 18-20 minutes so I am not sure which site it affects. It might affect hackerone or marketo. So I thought it would be better to report it first on hackerone. 

**POC**

1. Navigate to https://www.hackerone.com/product/features.
2. Click on "Get Started".
3. Fill FirstName, LastName, Company and Message by <img src=https://yourserver.com/f onerror=alert(1)>, <img src=https://yourserver.com/l onerror=alert(1)>, <img src=https://yourserver.com/c onerror=alert(1)> and <img src=https://yourserver.com/m onerror=alert(1)>.
4. Fill the remaining details and submit the form.
5. Wait 18-20 minutes and check server logs.

In this case ssrf triggers many times. Please check the screenshots.

Thanks 


## Attachments
- first.png
- second.png
