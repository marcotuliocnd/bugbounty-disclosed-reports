# IDOR + Account Takeover  [UNAUTHENTICATED]

## Report Details
- **Report ID**: 1004750
- **URL**: https://hackerone.com/reports/1004750
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-10-10T18:58:15.648Z
- **Disclosed**: 2020-11-09T18:28:19.706Z

## Reporter
- **Username**: silentbreach
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
1- Open the burp suite.
2- Switch the "Repeater" tab.
3- Paste the content of the attached request into the repeater.
4- Replace the "UID2 = 4820041" value in the cookie with the ID value of the user to be attacked. Also write the user's email in the "userName" input.
5- Replace the victim user's password

**Note: Follow the steps in the "1004745" report to get the user's email address.**

## Impact

You can change users' passwords and take over their account.

## Attachments
No attachments
