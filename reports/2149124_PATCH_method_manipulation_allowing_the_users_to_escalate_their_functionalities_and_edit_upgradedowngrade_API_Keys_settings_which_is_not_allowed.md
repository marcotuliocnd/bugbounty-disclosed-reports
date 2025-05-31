# PATCH method manipulation allowing the users to escalate their functionalities and edit (upgrade/downgrade) API Keys settings which is not allowed

## Report Details
- **Report ID**: 2149124
- **URL**: https://hackerone.com/reports/2149124
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-09-15T05:35:17.570Z
- **Disclosed**: 2024-03-20T13:13:36.011Z

## Reporter
- **Username**: bugsv2
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: frontegg

## Vulnerability Information
## Summary:

Hey sup, Hope you are doing well today Inshaallah <3

I found a misonfiguration today would allow the users to edit the API Keys `Info`, `description`, `createdAT`, `roleIds` and manipulate all of them

Let me show you something first ..

It’s only allowed for all the users, Owners or Admins → Just to create new API Key and remove API Key

██████

Like this screen, There’s no area to edit your API Key, But the users actually still has the access to edit it, By using `PATCH` method

What the PATCH method means?

After some searching .. I found out that the delete request is: `DELETE /frontegg/identity/resources/tenants/api-tokens/v1/<API_KEY_ID>`

and here is the Idea !! The group actually can be edited by sending `PATCH` and can be deleted with `DELETE`, So could the API be the same?

I tried actually and It worked with me !!

█████

## Steps to reproduce:

1. Create Account A and Account B
2. Invite Account B with role `Admin` to ⇒ Account’s A Panel
3. Now From Account A, “██████████████The owner”.█████████ Create an API Key with role `Owner`
    
    ████
    
4. Now go the Account B (█████████████The Admin████████████████) and try to delete the Key, But don’t delete it !! Just ███████████Intercept████████████ and move it to repeater, and ███████████████drop it█████████████████ !!
5. Now change `DELETE` to `PATCH` as method ..
6. Now You have those fields to control, 
7. Let’s send something like: `{"description":"desc111111","roleIds":["c22321ba-8ece-426d-b418-ece2a6d72009"]}`
and `c22321ba-8ece-426d-b418-ece2a6d72009` refers to role: `Impersonator`
8. Now It’s successfully changed ^_^
    
    ███
    
9. Thank You <3

## Possible Scenarios:

- Let’s say the Owner has 2 admins with him, and he created some API Keys with the “`Owner`” Permission, Which he would use by himself, The Admins now can edit this API key with our bug and downgrade the API token permissions or remove it at all, Now the API Key is bad one, The admin would have to remove it and create new one and configure his settings again and again and again
██████████████████and who did this? ::█████████████ No body knows man !! It’s not even allowed !!
- Admins can too downgrade and upgrade the API key which is “under the admin”

## Applying a Fix:

- remove the PATCH method from endpoint: `/frontegg/identity/resources/tenants/api-tokens/v1/<API_KEY_ID>`

## Impact

- PATCH method manipulation allowing the users to escalate their functionalities and edit (upgrade/downgrade) API Keys settings which is not allowed
- broken access control to not allowed functionalities
- Users can edit the API Key’s info which is not allowed

## Attachments
No attachments
