# Lack of Input sanitization leads to database Character encoding configuration Disclosure

## Report Details
- **Report ID**: 866271
- **URL**: https://hackerone.com/reports/866271
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-05-05T06:59:46.406Z
- **Disclosed**: 2020-08-07T08:48:39.733Z

## Reporter
- **Username**: l_user
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: unikrn

## Vulnerability Information
Summary:
Email Input field during Register is not properly sanitized leads to sql error 

 Steps To Reproduce:
   During Register use '💩' character in email field

## Impact

Information Exposure Through an Error Message
███████

## Attachments
No attachments
