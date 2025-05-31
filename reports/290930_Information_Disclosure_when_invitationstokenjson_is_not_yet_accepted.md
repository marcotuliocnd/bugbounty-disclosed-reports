# Information Disclosure when /invitations/<token>.json is not yet accepted

## Report Details
- **Report ID**: 290930
- **URL**: https://hackerone.com/reports/290930
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-11-16T17:12:30.179Z
- **Disclosed**: 2019-12-06T18:21:46.537Z

## Reporter
- **Username**: japz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi Team,

**Summary:**

First, i just want to clarify that this finding seems a purely human mistake from one of the hackerone member team who created a summary of this report: #283309

---

I have found that you guys (HackerOne) was disclosing email address and private program as part of this report summary of previously disclosed report: https://hackerone.com/reports/283309

__Summary screenshot below:__

███████

You will observed that HackerOne team create a summary of the report, but the summary discloses the token of the report PoC of the researcher: https://hackerone.com/invitations/█████████.json , but since the token is still valid (means invitation note yet accepted) it discloses the email address of the researcher and the private program.

## PoC (Steps to reproduce)

  1. Load the invitation token that hackerone mentioned on the summary: https://hackerone.com/invitations/█████.json

  2. Response `{"token":"█████","type":"Invitations::ReportDraft","auth_option":"use-existing-account","email":"████","status":"never","expires_at":null,"team":{"name":"████","handle":"██████","state":"soft_launched","profile_picture":"https://profile-photos.hackerone-user-content.com/production/000/009/583/█████.png?1456279218","url":"https://hackerone.com/██████████"}}`

__Researcher email address:__ ███

__Private program handle name:__ █████████

█████

## Mitigation:

First, immediately remove the token on the summary, second it is good to not display the email address of the researcher on the json response.

Let me know if anything else is needed.

Regards
Japz



## Attachments
No attachments
