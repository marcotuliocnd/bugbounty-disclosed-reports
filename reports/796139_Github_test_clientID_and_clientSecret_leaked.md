# Github test clientID and clientSecret leaked

## Report Details
- **Report ID**: 796139
- **URL**: https://hackerone.com/reports/796139
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-02-13T21:46:31.399Z
- **Disclosed**: 2020-07-24T00:27:51.310Z

## Reporter
- **Username**: rira12621
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Report Submission Form

## Summary:
A github clientID and clientSecret for an oauth app are being leaked on github

## Description
While looking for anything that is interesting on github I a clientID and clientSecret for a github oauth app hardcoded.
While they have been removed a long time ago, they are still valid and usable and easy to be found in the git history.

## Steps To Reproduce:
Check each branch and each commit from the past and keep looking for anything that looks like a token.
I did this automated using truffleHog (https://github.com/dxa4481/truffleHog)

`git clone git@github.com:kubernetes/test-infra.git`
`git checkout 70b274b10ed69dae95902cc3b5d1ead0ad4b6362`  
`git grep ClientSecret`

and in `mungegithub/mungers/bulk-lgtm.go` you will find the clientId and Client Secret

## Impact

While these credentials are not directly to be used to access they are bringing an attacker a lot closer.

This allows to build an app that uses github authentication.
As per the screenshot attached this will looks as if this was really approved and made by Brendan Burns.
I am not sure if this raises or lowers the risk this imposes as he is not directly the CNCF but indeed a pretty well known and trusted person inside the community.
If the user now clicks "authenticate" the attackers app follows the authentication flow further until https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/#2-users-are-redirected-back-to-your-site-by-github where it receives an access token.

This access token can now be used to impersonate any user that authenticated via our rogue app.

It should be assumed that the callbackURL is unknown but that is not true as github will give us a nice error message and we can rebuild it to `https://kubernetes.submit-queue.k8s.io/bulk-lgtm/bulkprs/callback?code=1e1db78bd7e2dfeb6b23` making the github flow complete.

even tho this subdomain doesn't exist anymore, we will still have the victims token.


This can easily be mitigated by revoking or rotating the clientSecret and ID

## Attachments
- Screenshot_2020-02-13_at_22.30.45.png
