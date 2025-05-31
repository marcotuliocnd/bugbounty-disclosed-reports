# my.stripo.emai email verification bypassed and also create email templates

## Report Details
- **Report ID**: 765318
- **URL**: https://hackerone.com/reports/765318
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-12-28T01:07:49.187Z
- **Disclosed**: 2020-02-04T07:38:48.495Z

## Reporter
- **Username**: h51ic0pt5r
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripo

## Vulnerability Information
Summary:
According to the Stripo.emai When the new user sign up Stripo.email allow to create  email templates after the verification of the email of Your stripo account.  Until your email get verified You are not able to create a email templates in your acc. User need to verified  their email successfully to create email templates. 
Steps To Reproduce:
  1.  Register on my.stripo.email via any fake email but it should be band new
  2. Email (fake email) isn't validated notification and don't allow to create basic templates and logoff from your account
  3.Login via fake email (registered email) and password but make sure burp intercept is on to intercept the response
  4. Modify prams in userInfo false to true and forward the response and You will see no any email validation notification appears and You can also 
     make email templates. 


Supporting Material/References:


below a poc video.

Suggestion:
Don't trust on user submit data, data like email verified via signature tokens if You can allow signature token in userInfo param that will be useful, token also set in the session match both token if valid then verified and having a functionality to delete accounts will be useful.

## Impact

I am sure security team know what are those services. And exposure of those services would bring a high security impact to my.stripo.email infrastructure.

## Attachments
No attachments
