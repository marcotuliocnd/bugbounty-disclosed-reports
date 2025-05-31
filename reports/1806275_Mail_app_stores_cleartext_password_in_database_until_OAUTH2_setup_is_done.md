# Mail app stores cleartext password in database until OAUTH2 setup is done

## Report Details
- **Report ID**: 1806275
- **URL**: https://hackerone.com/reports/1806275
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-12-15T10:21:14.550Z
- **Disclosed**: 2023-03-08T09:49:01.303Z

## Reporter
- **Username**: christophwurst
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:

The Mail app usually stores the user password encrypted. For XOAUTH2 the encrypted access token is stored in the same columns. However, during the time of the setup, XOAUTH2 accounts have the password in clear text in the database.

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  0. Configure Gmail Oauth client ID and secret as Nextcloud admin
  1. Open the Mail app
  2. Open the setup page
  3. Enter values for display name
  4. Enter a random value for the password
  5. Enter the gmail address

-> password field hides

  6. Continue the setup

Once the Gmail consent popup shows, look into oc_mail_accounts and the last entry.

inbound_password and outbound_password have the random value entered for the password.

## Supporting Material/References:

  * N/A

## Impact

A DBA could read the plaintext password

## Attachments
No attachments
