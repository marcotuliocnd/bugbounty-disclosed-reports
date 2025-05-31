# XSS Reflected 

## Report Details
- **Report ID**: 484905
- **URL**: https://hackerone.com/reports/484905
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-01-24T01:37:55.408Z
- **Disclosed**: 2020-05-27T14:08:16.473Z

## Reporter
- **Username**: manshum12
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi Team ,

I found that https://████████/████/household/updateProfileInfo.action has vulnerability by XSS Reflected in household.householdID parameter .

I can verify it with following URL: https://█████████/██████/household/updateProfileInfo.action?household.householdID=%27;alert(document.domain)//

## Impact

XSS Reflected Attack

## Attachments
No attachments
