# Khan Academy ClickJacking to Steal Users's Credintials

## Report Details
- **Report ID**: 639682
- **URL**: https://hackerone.com/reports/639682
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-07-10T17:57:58.666Z
- **Disclosed**: 2021-03-31T22:26:23.642Z

## Reporter
- **Username**: hack_im
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: khanacademy

## Vulnerability Information
#DESCRIPTION

1. It ask to login to https://alerta.khanacademy.org  with google account.
2. It doesn't give access to any normal user.
3. That's why after trying to login with GOOGLE account it shows a error message prompt with user's sensitive information including [email, code/access token and client id etc.]
4. Let's steal it via Click Jacking!

Note: If victim is already logged into his google account, attacker can easily steal victim's credintials including [email, code/access token and client id etc.]

#Usually we always logged into our google account, so it's quite easy to steal victim's credintials.

#Step to Re-Produce:

Step 1. Let's make [ Script+PoC ] via BurpSuite! {F526049}

Step 2. Login to your google account.

Step 3. Exploition!

Watch my proof of concept video carefully!

████

Cheers!

## Impact

Attacker can easily steal victim's credintials including [email, code/access token and client id etc.]

## Attachments
- clickjacked.html
