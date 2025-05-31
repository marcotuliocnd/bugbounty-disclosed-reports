# [Bypass #645264] Report title disclosure despite the program settings for email notification is set to "No Content"

## Report Details
- **Report ID**: 669438
- **URL**: https://hackerone.com/reports/669438
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-08-08T02:35:48.109Z
- **Disclosed**: 2019-09-09T01:30:46.991Z

## Reporter
- **Username**: japz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi Team,

**Summary:**

There is newly disclosed resolved report [Program Email Nofication settings ignored when being added as an external contributor](https://hackerone.com/reports/645264), However i found that the fix is incomplete.

I have found that email invitation for a collaborator (bounty splitting) still disclosing the __Report title__ in email when the notification comes from `Manage Collaborator` invitation.

### Steps To Reproduce

Assumes that __Manage Collaborator__ (bounty splitting) is enabled to the program

  1. As a program admin, navigate to *Program Settings > Click Program >Click Email Notifications*
  2. In email notification settings, select __No Content__
  3. Go to any report in your program and invite any hacker to the report to become a __Collaborator__.
  4. Hacker can also invite __Collaborator__.
  5. Check the invited hackers email, they will see the report title in the collaboration invitation email.


## PoC screenshot below:

{F549793}

{F549792}

## Impact

Sensitive information disclosing bypassing the program settings.

Regards
Japz

## Attachments
- poc_title_leaked.png
- program_settings.PNG
