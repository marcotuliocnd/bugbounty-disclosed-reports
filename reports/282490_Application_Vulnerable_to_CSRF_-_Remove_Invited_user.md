# Application Vulnerable to CSRF - Remove Invited user

## Report Details
- **Report ID**: 282490
- **URL**: https://hackerone.com/reports/282490
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-10-24T13:48:00.594Z
- **Disclosed**: 2018-05-08T09:29:30.229Z

## Reporter
- **Username**: ramakanthk35
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: infogram

## Vulnerability Information
POC:

1. Login to the application with a business account.
2. Go to Manage teams, where we can send invites to a team member. Send a Invite to a team member
3. After the invite is sent to a user, the admin has option to Remove User.
4. While trying to remove the user, capture the request in burp , do not forward the request, send to repeater and drop the request
5. Now, from repeater , copy the url and put it in a new tab of authenticated admin browser, the user removal is successful

The user removal URL would look like https://infogram.com/api/team/cancel-invitation/c535cc62-9586-4f4b-8306-9381dcdbc815?teamId=16537204&_=1508852073697

## Attachments
No attachments
