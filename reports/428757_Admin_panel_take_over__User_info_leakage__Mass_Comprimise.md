# Admin panel take over | User info leakage | Mass Comprimise

## Report Details
- **Report ID**: 428757
- **URL**: https://hackerone.com/reports/428757
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-10-25T15:49:34.515Z
- **Disclosed**: 2019-10-08T18:44:27.421Z

## Reporter
- **Username**: bigchonk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

**Summary:** [add summary of the vulnerability]
I'm able to take over the admin panel, allowing me to viewing the entire ticket database's PII (DOD ID, email, name by changing the URL and bypassing authentication
**Description:** [add more details about this vulnerability]

## Steps To Reproduce:
1: Go to
████████?x-app=itsm&x-urlpath=/arsys/shared/login.jsp&x-redir=%2Farsys%2Fforms%2Fedgelb-itsm-ar%2FRKM%253AKnowledgeArticleManager%2FDisplay%2BView%2F%3Feid%3DKBA000000024701%26cacheid%3Ddf8e1567

2: Change URL to 
█████?x-app=itsm&x-urlpath=../../../../../../../../passwd
3) 
LFI fails, click login
4) Enjoy full admin panel access

5 (Leak PII)
In the left hand corner, applications -> quick links -> AR system report console
Bottom left, click run


## Supporting Material/References:

  * List any additional material (e.g. screenshots, logs, etc.)
Proof of PII:
██████████

Proof of admin panel:
█████████

## Impact

I can steal users DOD IDs, pretty much anything I want because I'm the websites admin
Change tickets
Change user info
Change permission
Steal PII

## Attachments
No attachments
