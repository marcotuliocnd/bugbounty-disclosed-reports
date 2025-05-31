# Change phone number OTP flaw leads to any phone number takeover

## Report Details
- **Report ID**: 2588329
- **URL**: https://hackerone.com/reports/2588329
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2024-07-07T03:16:49.461Z
- **Disclosed**: 2024-10-09T04:21:45.002Z

## Reporter
- **Username**: polem4rch
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: indrive

## Vulnerability Information
## Summary:

Dear Indrive,

Ive found another valid report, the app allows any user to change the app phone number, but a flaw within the otp allows any number to be added into the account!

When an user requests a phone number change inside the app, it will send a 4 digit code but if you place 0000, it will accept any number and update it into the app!!

## Steps To Reproduce:

  1. Click setting in the account
  2. Click into the phone number and change for a new one
  3. Input 0000 as the otp code

  Phone number added!!


VIDEO POC

████████

At the end you can see  i was trying to pick a number from my contacts but instead i  just use a random phone number and works!!



Remediation: Make sure the otp doesnt accept 0000 or other invalid codes

Let me know if anything,

Regards,

Polem4rch

## Impact

Any attacker can use the phone number for an account takeover or delete anyone account, or cancelling trips

## Attachments
No attachments
