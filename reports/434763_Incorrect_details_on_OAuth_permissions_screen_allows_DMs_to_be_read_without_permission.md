# Incorrect details on OAuth permissions screen allows DMs to be read without permission

## Report Details
- **Report ID**: 434763
- **URL**: https://hackerone.com/reports/434763
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-11-06T10:04:29.257Z
- **Disclosed**: 2018-12-14T00:01:16.066Z

## Reporter
- **Username**: edent
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

**Summary:** 
The OAuth screen can be tricked into saying that an app cannot read Direct Messages. Despite that, DMs can be read.

**Description:** 
The official Twitter API keys have been leaked and are in use in several popular apps.
The iPhone keys and Google TV keys (as seen on https://gist.github.com/shobotch/5160017) present an OAuth screen which says the app "Will not be able to:   Access your direct messages."
This is false.  The apps *can* read DMs.

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. Ask the user to do the OAuth dance with a token generated from the official keys.
  1. User sees that the app cannot read DMs.
  1. User authorises.
  1. App now has unauthorised access to DMs.
  1. User is sad that their privacy has been violated.

## Impact: [add why this issue matters]
A user may not want a 3rd party app to have access to their DMs.

They rely on the OAuth screen to adequately inform them of the permissions they are granting.

Is this a GDPR violation? I'm not sure. You are telling users that the 3rd party app can't read their private information - but that is false. These API keys do allow access from *any* app which integrates them.

## Supporting Material/References:

  * Screenshot of the OAuth screen for Google TV
  * Screenshot of the OAuth screen for iPhone

## Impact

Unauthorised access to Direct Messages.

## Attachments
- Google_TV_Twitter_DMs.png
- iphone_dm.png
