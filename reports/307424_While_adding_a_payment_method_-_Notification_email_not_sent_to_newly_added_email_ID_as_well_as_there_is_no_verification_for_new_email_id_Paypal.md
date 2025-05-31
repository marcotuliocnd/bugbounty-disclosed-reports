# While adding a payment method - Notification email not sent to newly added email ID as well as there is no verification for new email id (Paypal)

## Report Details
- **Report ID**: 307424
- **URL**: https://hackerone.com/reports/307424
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-01-20T10:08:59.519Z
- **Disclosed**: 2018-01-23T19:32:54.459Z

## Reporter
- **Username**: us111
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Description:**
As you know hackerone allows us to add payout method. On selecting paypal we are asked to add paypal email id. On saving new email id. A hackerone account holder (i.e account from which payout method was changed) gets a notification email  saying that "The payout method was changed form current_user@testmail.com" to "New_user@testmail.com"

Note: This message comes when user has checked the box for making this email id as default else a simple notification email is triggered saying a new payment method has recently added to your account.

This is the expected behavior and very correct.

But the issue is a user whose email id has been added is not notified, according to me this is not the correct flow. Even a user should be notified that this email id has been added for paypal by xyz person. So all further payments will receive to this email id.

According to me the idle behaviour should be like whenever a user enters a new email address a verification code should be sent to that email address and after verifying only that email should be allowed. This is what i think and i believe.

Now a question arises why anyone will enter any other person email address because its all about money.

But the answer is you never know what an attacker might be thinking. There may be n number of reasons doing this below are few

1. On receiving bounty end user will be confused from where did this amount got deposited i never reported any vulnerability nor i have account on hackerone then y money got deposited to my account and may be he can lodge a complaint.

2. Purposely deposit money money to make him pay more tax (i don't know abt other countries but in country like INDIA if money is coming from additional resource then Accountants asks for all proofs from where did money came and we need to show all of them and based on that we pay yearly taxes)

### Steps To Reproduce

1. Login into your hackerone account
2. Goto Settings -> Payment Methods -> click on add payment method
3. Add another email id for which you have access ( so that you can check for any notification emails) 
4.Save

You will notice notification emails are only triggered to your registered hackerone account and no notification email is sent to newly added account.

### Optional: Your Environment (Browser version, Device, etc)
 Works in all browsers 

### Optional: Supporting Material/References (Screenshots)

 I have there is no need for any screenshots above steps are sufficient to reproduce it.

Note: This mentioned issue is not a hack but it is a good practise and adding a verification for new email id would be defence in depth.

## Impact

As mentioned above an attacker can use this in any way. We cannot guess what an attacker might think.

## Attachments
No attachments
