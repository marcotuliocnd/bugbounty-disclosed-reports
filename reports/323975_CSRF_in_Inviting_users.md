# CSRF in Inviting users

## Report Details
- **Report ID**: 323975
- **URL**: https://hackerone.com/reports/323975
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-03-09T19:33:21.827Z
- **Disclosed**: 2019-03-26T20:41:09.075Z

## Reporter
- **Username**: rijalrojan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: pingidentity

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

**Summary:** [add summary of the vulnerability]
When a user is invited, a GET request is made. This can be used with a CSRF attack. 

**Description:** [add more details about this vulnerability]
User invitations usually should be done through a POST request. In this case the app uses a GET request. For example: https://ort-admin.pingone.com/web-portal/ajax/user/directory/inviteuser/?alternate_email=rojan@netsecurity.tech&email=rojan@securifyinc.com
Which allows inviting another user easily. 

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. Download the attached html. 
  2. Open it in a logged in browser. 
  3. It should invite my email to the website. 
## Supporting Material/References:

  * List any additional material (e.g. screenshots, logs, etc.)

## Impact

Adding other users easily. Gives internal access.

The hacker selected the **Cross-Site Request Forgery (CSRF)** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**URL**
https://ort-admin.pingone.com/web-portal/usermanagement#/

**Verified**
Yes

**Can a victim be forced to perform a sensitive state-change operation unknowningly?**
Yes

**What state-change operation can be performed?**
Adding users.

## Attachments
- csrf.html
