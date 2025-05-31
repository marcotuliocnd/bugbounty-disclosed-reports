# Can see phone numbers of others by providing mail address

## Report Details
- **Report ID**: 2534458
- **URL**: https://hackerone.com/reports/2534458
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-06-03T17:42:45.253Z
- **Disclosed**: 2024-11-13T18:05:48.871Z

## Reporter
- **Username**: sevada797
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: linkedin

## Vulnerability Information
It is possible for an attacker to see anyone's phone numbers abusing bug in reset password functionality. Bug allows to see anyone's phone number via email address. I will provide video POC a bit later.

Steps to reproduce.
1) Go to `Forget password` page ███
2) Type your email press enter
3) After verification code is sent to your mail, Press can't access this email
4) You will see half of the phone number with that account,  select the checkbox with phone number and press `Send code`
5) You will be surprised seeing the phone number in the input tag visible to eye even without inspecting the page further
Saying  `Your phone is not set up for password recovery. Please use one of the confirmed emails or eligible phone linked to your account.`

## Impact

The exposure of users' phone numbers presents several security and privacy risks:

Privacy Violation: Users' private information is exposed without their consent.
Phishing Attacks: Attackers can use the obtained phone numbers to launch targeted phishing attacks.
Social Engineering: Attackers may exploit the information to impersonate users or gather more personal details through social engineering tactics.
Further Compromise: Knowledge of the phone number could potentially aid in other forms of attacks, such as SIM swapping or bypassing two-factor authentication (2FA).

## Attachments
No attachments
