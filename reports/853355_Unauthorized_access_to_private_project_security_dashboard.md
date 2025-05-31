# Unauthorized access to private project security dashboard

## Report Details
- **Report ID**: 853355
- **URL**: https://hackerone.com/reports/853355
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-04-19T09:30:11.064Z
- **Disclosed**: 2020-11-21T02:22:48.276Z

## Reporter
- **Username**: vaib25vicky
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

User with guest permissions can't view security dashboard of the private project. However, this is not applied when user permission changes from maintainer to guest. 

As a result, if user was previously a maintainer in the project he/she can add the project to their security dashboard and when their access levels decreases to guest, they can still view new security vulnerabilities result found in the project through their security dashboard. New security issues found in the project are reflecting back to the guest user security dashboard.


### Steps to reproduce

*  User A create a private project and add user B with maintainer access
* User B will add the project in his security dashboard.
* User A reduced the user B access level to guest. Now, user B can't view any old and new security issues in the project directly
* User B access the project new as well as old security issues through his security dashboard and also the specific new files where the issues lies
* Done

### Impact

The impact of this vulnerability is actually very high. A malicious user can take advantage of the security issues found and can use it to exploit the owner application.  **More info** will also disclose newly added files, dependencies and new internal structure of the project/application to the unauthorized user.


### What is the current *bug* behavior?

Unauthorized user (guest) can view security dashboard of the private project

### What is the expected *correct* behavior?

Project should be removed from the user security dashboard when his/her permission changes to lower.

### Relevant logs and/or screenshots

When permission changes to guest, user can't view the security dashboard directly, they are treated with this message.

{F794811}

But user can access the private project security issues through his own security dashboard.

{F794812}

### Output of checks

This bug happens on GitLab.com

**NOTE** : I'm using one of the example project provided by Gitlab named "yarn-vulnerabilities" for security testing.  
If you want to quickly validate my report, please consider using it.  https://gitlab.com/gitlab-examples/security/yarn-vulnerabilities. 



Thanks,
Vaibhav Singh

## Impact

Unauthorized access to private project security dashboard which allows a malicious user to exploit the owner application and also disclose application newly added files/dependencies and internal structure.

## Attachments
- sec1.png
- sec2.png
