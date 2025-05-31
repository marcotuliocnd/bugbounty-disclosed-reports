# Able to log in with default ██████g creds at  https█████████████████████.mil 

## Report Details
- **Report ID**: 710813
- **URL**: https://hackerone.com/reports/710813
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-10-10T01:34:54.464Z
- **Disclosed**: 2021-01-12T21:38:03.946Z

## Reporter
- **Username**: pirateducky
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary████**
was able to use ████████████████████████ to log into this instance of Adobe Experience Manager, though it does not seem to be in used at the moment 
**Description███████**
while navigating to https█████████████████████████.mil, I performed some fuzzing and found that `/repository` was available which asked for authentication using `███████████████████` worked and I could then access another path found by fuzing `lc` [link](https█████████████.mil/lc) which then showed me the ██████ panel. 

## Impact
Medium since it is not being used
## Step-by-step Reproduction Instructions

1. Navigate to  https████████████████.mil/repository 
2. use ████████████████ (username██████████password)
3. navigate to  https██████████████████████.mil/lc 

## Product, Version, and Configuration (If applicable)

Adobe Experience Manager

## Suggested Mitigation/Remediation Actions

Remove this application if it is not being used

## Impact

Medium - I was able to use █████████████ to log in 

Thanks

## Attachments
No attachments
