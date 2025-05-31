# Missing Password Confirmation at a Critical Function (Payout Method)

## Report Details
- **Report ID**: 303299
- **URL**: https://hackerone.com/reports/303299
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-01-08T16:26:08.722Z
- **Disclosed**: 2018-01-10T18:45:57.286Z

## Reporter
- **Username**: hk755a
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hey Hackerone Team,

Payout being one the very important matter demands to be taken extra precaution. But at our lovable platform "Hackerone" there is no Password Confirmation at one of very critical functions i.e Payout Method/state Change.
All the other important functions like : 1.) Email Change 2.) Password Change 3.) Disable Account are additionally protected by demanding the user to enter his current password to make any changes in them. 

But to my dismay Payout Method requires no additional authorization to:
 1.) Change state of any payout method, 2.) Add new payout method or 3.) Delete any. 

Which is quite unexpected. Isn't it? 
Or shall we not consider this function critical enough (like email,password change etc.) to demand additional security practice?

Proof Of Concept:
STEP 1.) Visit the following link with a logged in researcher account:
              https://hackerone.com/settings/payment_preferences

STEP 2.) Make any changes there. Notice you won't be asked to re-enter your password.


Very keen to have your response
Himanshu Kumar

## Impact

All the critical functionalities are protected by issuing a password confirmation as an additional security practice so that even if some one gets access to some logged in session, they can't do much harm. This certainly is just a best practice to cover any unintended mistakes of some worthy users.

The issue is one the missing best practices like the following other reports:
https://hackerone.com/reports/242964
https://hackerone.com/reports/546
https://hackerone.com/reports/38343

## Attachments
No attachments
