# Adding Used Primary Email Address to attacker account and Account takeover

## Report Details
- **Report ID**: 273647
- **URL**: https://hackerone.com/reports/273647
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-10-01T19:24:07.343Z
- **Disclosed**: 2017-10-05T14:38:00.608Z

## Reporter
- **Username**: sandeepl337
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
# Summary

I just found that the Gratipay is vulnerable for adding used Primary Email Address to attacker account and Account takeover of the Gratipay. 

# Description

I was looking at the source code of the application and I found that, "If the email address `test@test.com` is already added in the `X` Gratipay account as primary email address, then the attacker can also add the `test@test.com` in the `Y` Gratipay account". 

The above attack can be achieved by using the `add-email` action and updating the `address` parameter with payload once you login to the account. 

# Steps To Reproduce

As you can see the line number 123 which is looking for the email address if it exists in the database.

https://github.com/gratipay/gratipay.com/blob/04b85c20c681eab433e021fb9ce7d7a4258c7202/gratipay/models/participant/email.py#L123

Normal behavior - When user will use the sandeepk.l337@gmail.com it is exists in the database it will not allow you add the email address in the different account, according the Line number 123.  

Attack  - When the attacker try to add the sandeepk.1337@gmail.com which is already added into the other user's Gratipay account, however he can still add the other account's primary email into the attacker's  Gratipay account as primary email.

`Payload:  action=add-email&address=sandeepk.l337@gmail.com%20` all you need to append the %20 (%20 is treated as the space but below line 123 is considering as new email address)
https://github.com/gratipay/gratipay.com/blob/04b85c20c681eab433e021fb9ce7d7a4258c7202/gratipay/models/participant/email.py#L123

Once the above line executed then line number 131 and the application will send verification link to the email address. 

https://github.com/gratipay/gratipay.com/blob/04b85c20c681eab433e021fb9ce7d7a4258c7202/gratipay/models/participant/email.py#L131

If the Victim's email address is stolen or the attacker have temporary access to the email, then attacker can create new account on the Gratipay and add the Victim's email address into this Gratipay account. The attacker will receive all the Payment related emails and using forgot my password attacker can takeover the account. 

# PoC 
Kindly find the attached screen shot. 

# Patch
On the line number 314 the application updating the table without verifying that, "the requested email address is already exists in the database and assigned to other account".  

https://github.com/gratipay/gratipay.com/blob/04b85c20c681eab433e021fb9ce7d7a4258c7202/gratipay/models/participant/email.py#L314

The simple patch would be verifying the space encoding characters and also verifying the account is already exists in the database and assigned to the other account. 

If you have any question or you need video PoC then let me know I'll prepare it separately. 


Cheers. 

## Attachments
- Same_Email_address_into_two_different_account_as_primary_email.png
- Payload.png
