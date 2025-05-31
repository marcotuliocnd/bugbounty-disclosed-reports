# The user, who was deleted from Github Organization, still can access all functions of federalist, in case he didn't do logout

## Report Details
- **Report ID**: 245833
- **URL**: https://hackerone.com/reports/245833
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-07-04T13:48:23.900Z
- **Disclosed**: 2017-09-05T19:48:53.548Z

## Reporter
- **Username**: sp1d3rs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_bbp

## Vulnerability Information
##Description
Hi. I found a non-critical session management bug, which still can have serious impact in some scenarios.
When user perform login to the Federalist through Github, federalist checks his Organization ID (but only upon login).
When the user was deleted from organization for some reasons, but he was logged in the Federalist (or saved his session cookies), he can still do any action on behalf of organization (create sites, delete sites etc).

##Reproduction Steps & POC
1) Add a test user to your organization, which have access to the federalist.
2) Login to the Federalist.
3) Remove the user from organization, or leave organization
4) Try to create or delete the site. Federalist doesn't know that this user has no permissions, and will allow him to use functions.

##Suggested fix
You should implement Organization ID checking in the requests.
Upon login, the endpoint `/v0/me` is called (once). But it can be a good idea to call it in a random periods of time and check the organization ID, and in case it will return 403 - invalidate user session.


## Attachments
No attachments
