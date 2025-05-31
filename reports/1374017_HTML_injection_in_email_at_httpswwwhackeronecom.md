# HTML injection in email at https://www.hackerone.com/

## Report Details
- **Report ID**: 1374017
- **URL**: https://hackerone.com/reports/1374017
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-10-19T08:59:22.766Z
- **Disclosed**: 2023-05-12T10:24:53.039Z

## Reporter
- **Username**: iamr0000t
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
By filling the firstname and last name with html tags at this form 
https://www.hackerone.com/hackers/pentest-community-application

It is possible to send email via hackerone and add custom html :)


**Description:**

### Steps To Reproduce

1. visit https://www.hackerone.com/hackers/pentest-community-application
2. in first name and last name add html tags ie firstname "><h1>anything etc. 
3. in email section add email of victim . 
4. submit the form 
5. check the email and see the html injected there 

### additional information: 
1.) please check the screenshot to see both the emails ie 1 without payload and one with payload 


### Optional: Your Environment (Browser version, Device, etc)

 * 

### Optional: Supporting Material/References (Screenshots)

 *

## Impact

An attacker can send malicious emails from hackerone , inject html in the email :) 
we all know where it leads to .

## Attachments
No attachments
