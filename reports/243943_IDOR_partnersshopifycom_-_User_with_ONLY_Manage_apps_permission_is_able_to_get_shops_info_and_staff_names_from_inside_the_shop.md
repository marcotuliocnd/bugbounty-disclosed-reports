# IDOR [partners.shopify.com] - User with ONLY Manage apps permission is able to get shops info and staff names from inside the shop

## Report Details
- **Report ID**: 243943
- **URL**: https://hackerone.com/reports/243943
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-06-28T08:58:20.090Z
- **Disclosed**: 2017-07-19T14:01:15.819Z

## Reporter
- **Username**: inhibitor181
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
SUMMARY
----------
Hello, I have found a permission problem in https://partners.shopify.com that allows a member with only "Manage apps" permission to get various show information and also list the staff account from inside that shop without having access the shop's admin area

REPLICATION STEPS
--------------
1. Create a new partner account and add a business
2. Invite a new member from https://partners.shopify.com/[YOUR_ID]/memberships and grant him only "Manage apps" permission
3. Create a new Development Store.
4. Create a new staff member for that store ( Go to https://partners.shopify.com/629528/development_stores -> click on your store -> click Transfer store to client -> click Add a staff account -> save him )
5. Now, open another browser / incognito tab and activate the member account
6. Directly call the shop's detail link ( has the form of https://partners.shopify.com/629528/stores/21360565, you can get it with the admin account ). Note here : because these are incremental ids, one can predict with a somewhat accuracy what should come next by correlating the business id and the store id, then making some math calculations. Then fine tune it by bruteforcing.
7. You will be able to access the store's info (even after the admin has transferred the ownership to another staff member and it is pending).
8. __Also, by clicking again the Transfer store to client link, you will see in the dropdown the staff members. This must be restricted as the member does not have access to the admin area !__

NOTES
-------
- I am mostly sure that there is a permission scheme problem. If the member doesn't have any access to anything, after calling the shop's direct URL, he receives the error "You’re missing the Manage apps permission required to view this page". Why manage apps instead of manage shops ??
- The member cannot actually transfer the shop's ownership as that endpoints seems to be covered.

I have also attached some screenshots.

## Attachments
- shopify_after_transfer.png
- shopify_access.png
