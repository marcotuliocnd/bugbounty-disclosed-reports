# User's who are banned from program can still be invited to the new reports as collaborators

## Report Details
- **Report ID**: 1131306
- **URL**: https://hackerone.com/reports/1131306
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-03-29T05:16:49.595Z
- **Disclosed**: 2021-09-22T19:36:01.370Z

## Reporter
- **Username**: muon4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
## Summary:
Hello team!

We have found out that the banned user's (who are banned from program) can be invited to the new reports as collaborator users. This is pretty weird because the hacker should be banned and no new reports shouldn't be allowed.  

If program bans the hacker the program can't invite s/he back to be part of program. That's why we see that this is real issue and should be mitigated.

## Steps To Reproduce:

- Login to the system as an user who has right to invite hackers to the program
- Invite two hacker let say hacker A and hacker B at `https://hackerone.com/<program name>/launch`
- Make sure you have bounty split on at `https://hackerone.com/██████████/submission_requirements`
- Login and submit new report as an hacker A
- As a program user navigate to  this new report, close report and ban the user
- As a hacker B login and submit new report to this program
- Invite banned hacker A to this report as a collaborator
- Login as hacker A, check your email inbox and accept the collaborator invitation
- Hacker A were able to participate the program as a banned hacker

## Recommendation:

After a hacker is banned from a program the hackerone should ensure that s/he can't be invited to the new reports as a collaborator

## References:

-

## Impact

Banned hackers can still participate the program as a collaborator user

## Attachments
No attachments
