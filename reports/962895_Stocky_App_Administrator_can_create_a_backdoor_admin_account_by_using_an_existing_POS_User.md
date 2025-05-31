# Stocky App Administrator can create a backdoor admin account by using an existing POS User

## Report Details
- **Report ID**: 962895
- **URL**: https://hackerone.com/reports/962895
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-08-20T02:48:41.055Z
- **Disclosed**: 2020-08-24T21:58:39.568Z

## Reporter
- **Username**: imgnotfound
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Details
The Stocky App has POS Users that are being created once a POS Staff logs in into the application from the Point Of Sale application on a mobile device.

From the users management page located at https://stocky.shopifyapps.com/users there's no visible way to edit those POS users. Although, it is possible to edit them by inspecting their user id from the `delete` button and then opening `https://stocky.shopifyapps.com/users/{user_id}/edit` endpoint. Furthermore, you can even make that user an admin by adding `user[admin]` to the request being sent once you save their profile. As the UI doesn't show an admin column for POS users, it becomes a bit transparent to any other admins that a POS User does have an actual account and what roles he's assigned to.

The thing is that to access the Stocky APP, it requires an actual staff member with the App permission so this is reducing the impact here. Still, that flaw could be abused by a Staff Member whom was granted once the **Administrator** role within the app and took the opportunity to create a backdoor admin user from an already existing POS user and/or creating one for himself if he also had access to the Point Of Sale app. He could then be using that backdoor account at some point later if he does lose  its `Administrator` role from the app (assuming he still has the App permission).

## Steps to reproduce
1. From the Point Of Sale mobile application, open the Stocky Application with a POS User. (This is to create a POS User into the Stocky App - not sure if there's any other way)
2. As a Staff Member with Stocky App `Administrator` permission, open https://stocky.shopifyapps.com/preferences/users and inspect the user ID of that POS User by mouse hovering its delete button.
3. Open `https://stocky.shopifyapps.com/users/{user_id}/edit` by taking care of replacing the `{user_id}` placeholder with the one from previous step
4. Set an email address field to an email that you own, so you can actually use it to set the account password. To make it real the attacker user could be creating one with the actual POS User Firstname/LastName so it looks more real.
5. Intercept the request once you save the profile and add `user[admin]=1` to the payload

The POS user now has an actual account he can use to login as an admin (Still requires Stocky App permission).

## Demo (Step 1 excluded)
{F956014}

## Impact

Create a backdoor admin user from a POS user account

## Attachments
- Stocky_App_-_POS_User_as_admin.mp4
