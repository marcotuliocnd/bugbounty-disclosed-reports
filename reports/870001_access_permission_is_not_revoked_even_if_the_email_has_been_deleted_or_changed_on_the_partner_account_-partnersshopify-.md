# access permission is not revoked even if the email has been deleted or changed on the partner account -partners.shopify-

## Report Details
- **Report ID**: 870001
- **URL**: https://hackerone.com/reports/870001
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-10T12:56:32.714Z
- **Disclosed**: 2020-08-18T19:44:19.392Z

## Reporter
- **Username**: jaka-tingkir
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
I can get increased privileges from accounts that have been deleted from shopify partners.

a partner uses another business email account and when the business email has been replaced or deleted from a partner, it turns out that the account still has full access as a collaborator account or still has permission as a partner account.

## Steps For Reproductions
1. create a partner account and use another business account email, and confirm
2. Add the store as a collaboration, and receive permission from the shop owner
3. Open a shop that has given permission
4. Return to partners, change business email to your email, and confirm
5. open an account from the email that has been used in a business email (step 1), try logging in to the added store (step 2). You can not enter and look email is not registered at the store
6. try logging in to `accounts.shopify.com` and successfully entering the shopify account
7. entered the store that was added, after successfully logging in it turns out that this account entered using the name of the partner account ██████████

## Impact

The account can enter the collaboration store using the permission as a collaboration account even though it has been deleted from the partner account and is not part of the partner

## Attachments
No attachments
