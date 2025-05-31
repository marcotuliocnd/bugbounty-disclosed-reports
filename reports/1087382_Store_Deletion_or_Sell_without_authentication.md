# Store Deletion or Sell without authentication

## Report Details
- **Report ID**: 1087382
- **URL**: https://hackerone.com/reports/1087382
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-01-26T09:46:38.947Z
- **Disclosed**: 2021-10-21T18:57:07.762Z

## Reporter
- **Username**: fr4via
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
In order for an owner to "close or sell" the store,  a password is required in order to confirm the decision, when the action is applied in the web application.  
It was identified that  the mobile application doesn't require credentials in order to perform the same action, thus by navigating to the Settings->Plan and Permissions -> Sell or Close [bottom of the page] , the user may 'close' the shop without issuing a password.
- The flow in the first case is shown in the screenshots  close1.png, close2.png, close3.png (see attachments)
- The flow in the second case is shown in the screenshot cloceAccountMobile1.png

## Impact

By the time that the physical access requirement is satisfied and since the application is not protected by any kind of user verification (e.g. login pin), as a first place, an unauthorised entity may access the options mentioned above add Sell or Delete a shop without providing any authentication.

## Attachments
- close1.png
- close2.png
- close3.png
- closeAccountMobile1.png
