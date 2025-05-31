# PII leakage due to caching of Order/Contract ID's on █████████

## Report Details
- **Report ID**: 374007
- **URL**: https://hackerone.com/reports/374007
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-06-29T19:49:16.494Z
- **Disclosed**: 2019-10-08T18:48:35.562Z

## Reporter
- **Username**: alyssa_herrera
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
I was able to discover contract numbers which leak out user names/emails/phone numbers nd other sensitive information. I took the time to assure that these contract id's wouldn't/shouldn't be easy guessable or known.
**Description:**
I discovered through google search query that I was able to access several Order/contract id's that revealed a trove of sensitive data that shouldn't of been easily accessible or cached by google search results.
## Impact
High
## Step-by-step Reproduction Instructions
https://███/CMT_View/CMT_View_List.cfm?StartRow=31&OrderBy=Email&OrderByCol=4&Sort=DESC&SearchType=CONTRACT&ContractNumber=███&Cage=

https://██████████/CMT_View/CMT_View_List.cfm?OrderBy=FormatedRoleCode&OrderByCol=2&StartRow=1&Sort=ASC&SearchType=CONTRACT&ContractNumber=██████&Cage=

███████, ██████ D.	ACO	1102	██████████.█████@█████████	█████████
████, ████ J.	CA	1102	███████.███@█████	█████
████, ███ M.	DRPM	0801	████.████████@██████	██████
██████,███████ R.	IS	1150	████.█████@████	██████
████, ███████ R.	PA	1103	████.████@█████████	████████
███████, ██████████ S.	PT	1106	████.████████@███	██████
████████, ███ E.	QAR	1910	██████████.████████@████████	█████████
██████████, ████ M.	SUP	0344	█████.█████@█████	██████
████████,███ R.	SUP	1150	██████████.███@███████	████
█████, ██████ D.	SUP	1150	██████.████@█████████	█████████

Additionally verified that these aren't test data entries by googling one of the emails and resulting found the owner's linkedin account.
## Product, Version, and Configuration (If applicable)
N/A
## Suggested Mitigation/Remediation Actions

## Impact

An attacker can gather high priority PII.

## Attachments
No attachments
