# Email Verification Bypass by bruteforcing when setting up 2FA

## Report Details
- **Report ID**: 1394984
- **URL**: https://hackerone.com/reports/1394984
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-11-09T00:55:37.395Z
- **Disclosed**: 2022-05-22T21:41:10.572Z

## Reporter
- **Username**: cyberworlcload
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: evernote

## Vulnerability Information
## Summary:
Hello team, I hope you are fine and doing well

when a user set ups his 2 Factor Authentication in his account  and verify his email ,i was able to bruteforce the email verification process . 

The confirmationCode is used for authentication of user's email and it can be brute forced. The code is only 6 digits long ,so it will not take much time to crack . (https://cloudnine.com/wp-content/uploads/2020/02/CrackPassword2.png)

After the victim's email confirmation code gets verified , the user can then set up his personal phone to victim's email and the victim will never be able to sign inside his account as he does not get the otp received in the attakers phone.(due to 2 fa)

## Steps To Reproduce:

  1. Request a confirmationCode in your email , enter any code
  2. Send this request to burpsuite intruder , and bruteforce the confirmationCode with any number of requests
  3. Out of all the response , one response will have a length around 373 (only response whose length is lesser than others), thus proving that was the correct confirmation code.

*Attackers Scenario*:

Attacker creates a account using victim's email ABC@gmail.com , Now attacker setups the 2FA  using brute force . Victim wants to join evernote , so he resets his password but he is unable to join since he does not have the 2FA codes . Thus he user is permanently unable to access evernote . It is a pre account takeover .

## Impact

The victim who wants to log inside or use forget password to recover his/her account in evernote will be locked out forever. Attacker did a pre account takeover.

## Attachments
- brute.png
