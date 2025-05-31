# Sensitive information disclosure to shared access user via streamlabs platform api

## Report Details
- **Report ID**: 1072893
- **URL**: https://hackerone.com/reports/1072893
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-06T17:26:32.610Z
- **Disclosed**: 2021-01-20T23:50:04.598Z

## Reporter
- **Username**: pspspsp
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: logitech

## Vulnerability Information
## Summary:

Hi there, 

Hope you are doing well and stay safe.

Streamlab allows us to invite other users to manage our dashboard and cloudbot functions via following setting which named "Shared Access".

    https://streamlabs.com/dashboard#/settings/shared-access

If we invite other users with **Moderator** role, they only have access to our dashboard and cloudbot function.
But streamlab platform api doesn't have proper access control on the following api endpoint which discloses sensitive information like parent user email, jwt token to shared access users.

    https://platform.streamlabs.com/api/v1/s/user/me

## Steps To Reproduce:

Let's suppose there are User A and User B.

1)  Login to User A account and browse to https://streamlabs.com/dashboard#/settings/shared-access 

2)  Create invitation link with **Moderator** access and copy link and Logout.

3)  Login to User B account and accept the invitation by pasting copied link.

4) Go to https://streamlabs.com/dashboard#/settings/shared-access and click to access  User A account.

5) Try to access the following endpoint which response current user info including user id, username,  email, etc...
     
    https://streamlabs.com/api/v5/user/

6) You'll end up getting response saying "Request Unauthorized" because you don't have access to view User A information.

7)  Now if you try to access the following api endpoint, you should get response with User id, Email, Jwt token of User A.

     https://platform.streamlabs.com/api/v1/s/user/me

Video POC

{F1146950}

## Impact

Disclosure of parent user's  sensitive information like email, jwt token which is used to access developer api.

Thanks

Best Regards
@hein_thant

## Attachments
- Screen_Recording_2021-01-06_at_23.51.58.mov
