# Reset the 2FA of the user which can lead to Account Takeover

## Report Details
- **Report ID**: 2492631
- **URL**: https://hackerone.com/reports/2492631
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-05-07T07:36:44.891Z
- **Disclosed**: 2024-07-11T15:09:54.991Z

## Reporter
- **Username**: 5zdob13
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

  Dear H1 Security Team,
   This report details a vulnerability that allows attacker to reset the 2FA of the victim and takeover their account within a day.

**Description:**

 The 2FA is extra layer of protection from getting your account compromised and that means even if the attacker knows your email and password still they can't access to your account but when you sign-in to "https:hackerone.com" with 2FA enable there's a  **Reset option** :
F3250375
   And then you'll got an email to **cancel the request** :
██████████
  If you don't Interact with this email within a day your 2FA will be disabled.
So Attacker can request to disabled the 2FA of the victim and If the victim don't cancel this request after a one day  attacker can takeover the victim's account and have a full access to it.
  On my opinion, Requesting something like this is a too serious so even If the attacker can request to disable the 2FA the email should be to **Confirm this action** not to stop it. "I mean after user request to reset their 2FA,  they have to check their email and confirm that they want to reset the 2FA and then the process can start and  maybe after that HackerOne email them If they want to cancel the request like this one:
 ████

I hope I was helpful and sorry If there anything not clear enough.
Kind regards,
5zdob13
 
### Steps To Reproduce

1. Enable the 2FA one your account and sign-out.
2. Sign-in and don't enter your Time-based One-Time Password (TOTP) and click on "Reset two-factor authentication" and press ok like this below:
█████
3. don't Interact with the email that you received.
4. After one day, try to sign-in and you’ll be able to sign in successfully.

### Optional: Supporting Material/References (Screenshots)
  
On my PoC I just showed you what happened after one day from requesting to reset the 2FA

████████

## Impact

Attacker can request to reset victim's 2FA and takeover victim's HackerOne account and also exploiting this vulnerability requires minimal technical skill too.

## Attachments
- reset-2FA.png
