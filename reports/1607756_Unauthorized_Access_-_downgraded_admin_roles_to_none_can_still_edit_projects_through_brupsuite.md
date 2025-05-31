# Unauthorized Access - downgraded admin roles to none can still edit projects through brupsuite

## Report Details
- **Report ID**: 1607756
- **URL**: https://hackerone.com/reports/1607756
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-06-20T16:03:43.388Z
- **Disclosed**: 2022-07-01T16:48:51.117Z

## Reporter
- **Username**: irwanjugabro
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: omise

## Vulnerability Information
hi team,
I found that your site is vulnerable to Unauthorized Access lead to  privilege escalation, where when the owner invites a user with admin roles, the user can still edit anything with admin access, via brupsuite, it should get an error message because the admin role has been removed.


production step:
1. The `owner `invites `user` with admin roles at https://dashboard.omise.co/team
2. Then the `user`, intercept any request using brupsuite, for example edit/add link at https://dashboard.omise.co/v2/links
3. then the `owner` lowers the role to `none`
4. then you will see, the user does not see the create link feature because the role is lost
5. but when the `user` repeats the request step#2 via brupstuite. then it will be valid.

PoC :
██████

## Impact

Unauthorized Access lead to  privilege escalation, downgraded admin roles to none can still edit projects through brupsuite

## Attachments
No attachments
