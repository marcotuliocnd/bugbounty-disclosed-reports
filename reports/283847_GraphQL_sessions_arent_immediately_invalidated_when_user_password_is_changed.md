# GraphQL sessions aren't immediately invalidated when user password is changed

## Report Details
- **Report ID**: 283847
- **URL**: https://hackerone.com/reports/283847
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-10-28T21:59:08.330Z
- **Disclosed**: 2017-11-30T22:28:39.938Z

## Reporter
- **Username**: bigbug
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

While changing password, once user clicks on "Change password" button after giving necessary values, on https://hackerone.com/settings/pass/edit, the session expires and the user is redirected to https://hackerone.com/users/sign_in for logging in again with the updated/changed password. A graphql mutation is used to change password. But, it is observed that the user can still change password with same graphql token and same session id, used in previous graphql request **even after signing out**. Inshort graphql token nor host session expires. 
 
**Description:**

Sorry if I categorized this into wrong weakness category. Also apologize for the complicated title.

When clicking on "change password" after supplying values for  current password, password and confirm password, user is directed to sign_in page to log in again with changed password. 

The password change takes place through graphql mutation request that contains graphql token and session id. 

It was observed that after capturing the above request with the help of a web debugging tool (charles proxy), the above request could be replayed with same graphql token  **x-auth-token** and host session **__Host-session**, with appropriate password values after sign out and the password is changed.

Inshort **A user can change password even after he/she is signed out or session expires, without having to login again, with the help of previously captured graphql request.**

**Impact**

An attacker could simply change the password again by capturing previous request. As the change can be done even after sign out or expired session, it is more severe.

**Remedy**

Must enforce graphql token expiration. Also check for host_sesssion cookie value.

### Steps To Reproduce

1. Login to the account and navigate to https://hackerone.com/settings/pass/edit to change password.
2. Input necessary values and click "Change password" button. Capture the request using a proxy.
    (User is now logged out and redirected to sign_in page)
3. Repeat the previous "graphql mutation" request using proxy with changed password. Password is
     changed again without having to login.  


## Attachments
No attachments
