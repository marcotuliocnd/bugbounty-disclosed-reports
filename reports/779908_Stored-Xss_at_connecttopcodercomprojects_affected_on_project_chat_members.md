# Stored-Xss at connect.topcoder.com/projects/ affected on project chat members

## Report Details
- **Report ID**: 779908
- **URL**: https://hackerone.com/reports/779908
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-01-21T23:27:10.964Z
- **Disclosed**: 2020-09-22T19:41:55.290Z

## Reporter
- **Username**: sodium_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lab45

## Vulnerability Information
Hi team ,
I'm sorry for my bad report and english ,
but i wish you understand the impact of that bug here , if it well performed the sers may lose their access to their sso accounts 

## Summary:
While a developer at connect.topcoder.com can manage a messages about his/her project with someonelse ,
This conversation was not fully protected from XSS , if some user join in the same chat he'd be affected by that xss and his ==SSO== account possibly will be token over 

## Steps To Reproduce:
After you register to topcoder.com go to connect.topcoder.com and sign on with your sso account ,
After that Go to https://connect.topcoder.com/new-project/ and add new project

**NOTE** : The discussion will not be accessible publicult efore the administratirs manages it , So after the adiministrators accept it the bug will be accessible publiculy █████

  1. GO TO https://connect.topcoder.com/projects/<your_project_id>/messages
  2. Add message with random title and this `<script>alert()</script>` as content , then submit
  3. You'll get a fully JS code injected 

If an attacker inject a Javascript code that steal cookies/csrf-token... he'll be able to fully access to the victim account

## Supporting Material/References:
Tested on
* Chrome Browser .
* Windows 7_64x 
Note : That bug is affect to every machine/browser

## Impact

Xss

## Attachments
No attachments
