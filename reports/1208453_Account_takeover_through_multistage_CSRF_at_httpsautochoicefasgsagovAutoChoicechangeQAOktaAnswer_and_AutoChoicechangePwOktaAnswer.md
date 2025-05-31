# Account takeover through multistage CSRF at https://autochoice.fas.gsa.gov/AutoChoice/changeQAOktaAnswer and ../AutoChoice/changePwOktaAnswer

## Report Details
- **Report ID**: 1208453
- **URL**: https://hackerone.com/reports/1208453
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-05-25T12:08:45.284Z
- **Disclosed**: 2021-07-23T02:07:47.706Z

## Reporter
- **Username**: rptl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_vdp

## Vulnerability Information
Hi,

Account takeover is possible through CSRF vulnerability at 'Change Security Question/Answer'  & ' Change Password'.
The endpoints - https://autochoice.fas.gsa.gov/AutoChoice/changeQAOktaAnswer & https://autochoice.fas.gsa.gov/AutoChoice/changePwOktaAnswer both are vulnerable to CSRF attack .==The CSRF token/or its presence is not validated at server side.==

Since, the password update functionality requires 'Secret Answer' Value & 'New Password'. Therefore, in multistage CSRF Secret Answer was updated first & then using that new secret answer, new password was set for the account using second stage.

Both CSRF request are performed through the same html POC. Upon execution of POC html, changes will  be reflected after few seconds as timeout is set for the first request to complete.  Also, there is no need to know the security question either, which itself is updated in the first stage.

POC Video - {F1314428}

CSRF Html file -  {F1314439}

@Triage Team - Since, this report involves two CSRFs for different functionalities, should I have filed two different  reports ?  as I would be losing rep. points.

## Impact

Account takeover through CSRF

## Attachments
- recording-1621943105665.webm
- secret_answer_and_pwd_csrf.html
