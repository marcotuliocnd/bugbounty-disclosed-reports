# Misconfigured oauth leads to Pre account takeover 

## Report Details
- **Report ID**: 1074047
- **URL**: https://hackerone.com/reports/1074047
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-01-08T04:52:02.069Z
- **Disclosed**: 2021-03-18T12:19:29.210Z

## Reporter
- **Username**: dhakal_bibek
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bumble

## Vulnerability Information
##Summary

While testing badoo i have noticed that users can use SMAL (Google,MSN,VKontakte,Odnoklassniki,Yandex
Mail.Ru) to create and login to badoo accounts. Now there are two ways of registering into badoo

By email registration
Google,MSN,VKontakte,Odnoklassniki,Yandex,Mail.Ru  oauth login

Now here badoo has a weak auth verification which does not check if a previous account was created with the same email when we use Google,MSN,VKontakte,Odnoklassniki,Yandex,Mail.Ru to login to our accounts. SO basically what it means is that someone can register using the unregistered victims account. **after that victim will log in using the OAuth. in this case, the verification process is bypassed and the attacker can log in using the password after that.**

##Steps

1: Go to https://badoo.com/en/signup/ and signup using the unregistered victim's account.

2: Now, It will ask you to verify the email.
{F1148978}
3: After the sometime victim is going to signup using the OAuth method.

4: What happens here is, now the victim can easily log in using the victim's account which bypasses the verification methods.

{F1148983}

##Fix
Either don't let user enter with oauth when there's already another account created with the same email or let the user enter but let him know someone else has already created an account and if it was him or not then ask him to change the password.

## Impact

Only one thing we need here and that is email address. Just by knowing that we can takeover victim's account so the impact here is quite high. Imagine email address is something you can even get if you ask so its not a hard task. But since the oauth does not authenticates the real user attackers can easily takeover the account.

## Attachments
- Screenshot_from_2021-01-08_10-25-48.png
- recording-1610081305478.webm
