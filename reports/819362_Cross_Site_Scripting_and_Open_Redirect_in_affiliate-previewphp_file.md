# Cross Site Scripting and Open Redirect in affiliate-preview.php file 

## Report Details
- **Report ID**: 819362
- **URL**: https://hackerone.com/reports/819362
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-03-14T18:49:20.091Z
- **Disclosed**: 2021-01-20T11:02:43.672Z

## Reporter
- **Username**: keyurvala
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: revive_adserver

## Vulnerability Information
### Summary:
Stored XSS can be submitted on the Website using Default Manager, and anyone who will check the report the XSS and Open Redirect will trigger.

### Description:
Stored XSS, also known as persistent XSS, is the more damaging than non-persistent XSS. It occurs when a malicious script is injected directly into a vulnerable web application.

### Steps To Reproduce:
1. Login with valid credentials of the user.
2. Go to inventory > Website > Website Properties
3. Fill the form and Enter Website URL as "http://Test"><img src=x onclick=window.location="http://google.com">". Click Save Changes.
4. Login with an administrator account.
4. Open http://localhost/hackerone/www/admin/affiliate-preview.php?codetype=invocationTags%3AoxInvocationTags%3Aspc&block=0&blockcampaign=0&target=&source=&withtext=0&charset=&noscript=1&ssl=0&comments=0&affiliateid=1&submitbutton=Generate
5. Click on Header Script Banner there is image click on that it will execute xss or open redirect.

## Impact

###Impact
Users can redirect the admin user or any normal user to any other website evil.com.

## Attachments
- XSS_on_Revive.mp4
