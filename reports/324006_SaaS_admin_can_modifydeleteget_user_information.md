# SaaS admin can modify/delete/get user information.

## Report Details
- **Report ID**: 324006
- **URL**: https://hackerone.com/reports/324006
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-03-09T22:01:02.670Z
- **Disclosed**: 2019-03-26T20:42:55.491Z

## Reporter
- **Username**: rijalrojan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: pingidentity

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

**Summary:** [add summary of the vulnerability]
Based on what is seen, SaaS admin should not have access to users info from this page: https://ort-admin.pingone.com/web-portal/usermanagement#/ however, it is still able to get the info on that page. 

**Description:** [add more details about this vulnerability]
When we go to https://ort-admin.pingone.com/web-portal/usermanagement#/, it returns an error that says: `You are not authorized to view that page.`. This means it is blocking certain user permissions like SaaS admin. 

But the Ajax link that retrieves user info on that page does not check for the permission and gives out detail info of the users. 


## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. Make sure you are the SaaS administrator on that page and not a Global Admin. If you do not have a SaaS admin account, you can create one at: https://ort-admin.pingone.com/web-portal/account/administratorsng
  2. Go to https://ort-admin.pingone.com/web-portal/ajax/user/directory/users/?advancedSearch=false&ascendingSort=true&count=100&searchString=&sortField=name.familyName&startIndex=1&statusFilter=

## Supporting Material/References:

  * List any additional material (e.g. screenshots, logs, etc.)

## Impact

Leaking user information for under privileged user.

## Attachments
No attachments
