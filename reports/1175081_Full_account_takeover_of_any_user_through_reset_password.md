# Full account takeover of any user through reset password

## Report Details
- **Report ID**: 1175081
- **URL**: https://hackerone.com/reports/1175081
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-04-26T12:34:49.823Z
- **Disclosed**: 2021-05-14T21:28:47.200Z

## Reporter
- **Username**: saajanbhujel
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: upchieve

## Vulnerability Information
## Summary:
Hi Security team members,

Usually, If we reset our password on https://app.upchieve.org that time we got a password reset link on the email. And through that password reset link, we can reset our password.

But, I noticed that if we add another email in the request of forgot password through Burpsuite then both person will get the same password reset token in their email. So, an attacker can takeover any account without the user's interaction.

## Steps To Reproduce:
1. Navigate to: https://app.upchieve.org/resetpassword 

2. Then, enter the victim's email address 

3. Intercept this request

4. Now, add your email also in the JSON body. like this:
```
{"email":["victim@gmail.com","your@gmail.com"]}
```
5. Forward this request

6. Now victim and you will receive the same password reset link
{F1278871}

7. By using that link which you just received in your email

8.  You can fully takeover the victim's account by reset password.

##POC:
{F1278872}

## Impact

1. It is a critical issue because an attacker can change any user's password without any user interaction.
2. This attack does not require any interaction from the victim to perform any actions and yet the account can be taken over by the attacker.
3. An attacker can fully takeover any user's account

## Attachments
- sameEmail.png
- tko.mp4
