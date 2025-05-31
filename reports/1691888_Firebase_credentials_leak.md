# Firebase credentials leak

## Report Details
- **Report ID**: 1691888
- **URL**: https://hackerone.com/reports/1691888
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2022-09-06T03:11:17.412Z
- **Disclosed**: 2022-12-15T13:28:25.003Z

## Reporter
- **Username**: jimmisimon
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
This report is regarding the fix of #1351329.
The fix is not patched fully, comments are visible to anyone and an attacker can utilize this for further attacks.

## Steps To Reproduce:
go to : view-source:https://mpulse.mtn.ng/
search for 'Initialize Firebase'

as you can see the firebase details are commented.

## Supporting Material/References:
POC attached

## Impact

Unauthorized access to firebase

## Attachments
No attachments
