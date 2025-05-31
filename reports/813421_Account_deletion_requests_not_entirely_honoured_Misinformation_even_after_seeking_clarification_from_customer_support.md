# Account deletion requests not entirely honoured. Misinformation even after seeking clarification from customer support.

## Report Details
- **Report ID**: 813421
- **URL**: https://hackerone.com/reports/813421
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-03-09T05:14:23.183Z
- **Disclosed**: 2020-03-24T16:32:40.767Z

## Reporter
- **Username**: keshavkejriwal
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nordsecurity

## Vulnerability Information
Summary:
Requesting account deletion from NordVPN customer support that is supposed to have "removed your account from our database." does not truly remove account from database. Even after asking if critical information such a billing information is removed, which customer support confirms affirmatively, billing history is available on the website. Such a privacy hazard could be held against a NordVPN customer in a court of law, resulting in disastrous consequences for both the customer in question and NordVPN as an organisation.

Steps To Reproduce:
  1. Login into any NordVPN account at ucp.nordvpn.com (Original test ID was vainrunney30@protonmail.com)
  2. Contact customer support via live chat and request account deletion.
  3. Even after customer support confirms account has been deleted, account is still very much accessible using the following credentials:
     Email ID: vainrunney30@protonmail.com.deleted 
     Password: *same as the one used in step 1.*
     That is, simply appending ".deleted" to original e-mail address provides full access to falsely claimed "deleted" account.
  4. Even after support rep confirms billing history deleted, COMPLETE billing history very much available under billing history tab upon login with   xxx@xxx.com.deleted
                            

Supporting Material/References:
F741558: Logged in with test account.
F741554: Requested deletion from customer support on live chat.
F741556: Support rep falsely claims account (and billing history) deleted from NordVPN database.
F741559: Billing history very much visible.

## Impact

1. Critical information such as billing history is enough to convict a user in a court of law, and therefore, when claimed to be deleted, it must truly be deleted.

2. Customer feels a false sense of assurance.

3. Clearly, NordVPN support rep was propagating misinformation, inflicting damage on the image of NordVPN as an organisation.

## Attachments
- RequestedDeletion.PNG
- SupportRepConfirmsBillingHistoryDeleted.PNG
- OriginalAccountLogin.PNG
- DeletedBillingHistoryVisible.PNG
