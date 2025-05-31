# Affiliates - Session Fixation

## Report Details
- **Report ID**: 737058
- **URL**: https://hackerone.com/reports/737058
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-11-13T19:48:42.782Z
- **Disclosed**: 2020-06-14T06:49:20.454Z

## Reporter
- **Username**: jair
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: clario

## Vulnerability Information
SEVERITY: Medium

LOCATION:
● https://affiliates.kromtech.com

ISSUE DESCRIPTION:
User can use the same session token after logout. Attacker can repeat request with token that should be marked as invalidated.

PROOF OF VULNERABILITY:
Request made after Logout with the same cookie value.

curl -i -s -k -X $'GET' \
-H $'Host: affiliates.kromtech.com' -H $'Cookie: sid=91iqik6qtblp0vsu9b5j7fgal0;' \
-b $'sid=91iqik6qtblp0vsu9b5j7fgal0' \
$'https://affiliates.kromtech.com/account'

RECOMMENDATIONS:
The logout function should be prominently visible to the user, explicitly invalidate a user’s session and disallow reuse of the session token. Server should provide new session id to user browser after logout.

## Impact

A remote attacker can gain access to victim’s session and perform arbitrary actions with privileges of the user within the compromised session.

## Attachments
No attachments
