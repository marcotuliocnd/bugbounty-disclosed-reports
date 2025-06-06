# Week Passwords generated by password reset function

## Report Details
- **Report ID**: 765031
- **URL**: https://hackerone.com/reports/765031
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-12-27T09:24:25.869Z
- **Disclosed**: 2020-05-09T13:54:35.927Z

## Reporter
- **Username**: tp9222
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
 Assessor observed that password reset function generates only alphanumeric passwords that is passwords don't contain any special characters 
Also User can set old password as new password.

## Steps To Reproduce:

Goto https://mycontract.mtn.co.za/landing/landing.htm
Click forget password link
select email radio button and enter user ID
press submit 

*Application will send email with week password*

upon entering temporary password application ask user to set new password
here user can enter his immediate used password


## Supporting Material/References:

https://www.owasp.org/index.php/Authentication_Cheat_Sheet
https://www.owasp.org/index.php/Top_10-2017_A3-Sensitive_Data_Exposure

Remediation:
Application should generate secure passwords thats password should contain alphanumeric characters as well as special characters 
Application should not allow user to set previously used 5 password as new password

## Impact

## Impact 
Brute force attack can be carried out on the password based authentication mechanism

## Attachments
- password_reset_not_secure.jpg
