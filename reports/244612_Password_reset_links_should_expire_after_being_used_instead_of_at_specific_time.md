# Password reset links should expire after being used, instead of at specific time

## Report Details
- **Report ID**: 244612
- **URL**: https://hackerone.com/reports/244612
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-06-30T03:08:35.234Z
- **Disclosed**: 2017-07-23T16:37:40.454Z

## Reporter
- **Username**: silv3rpoision
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
Hi,

Hope you are good!

Steps to repro:
1) Create an account having any email address like "a@x.com".
2) Now Logout and ask for password reset link. Don't use the password reset link sent to your mail address.
3) Login using the same password back and update your email address to "b@x.com" and verify the same. Remove "a@x.com".
4) Now logout and use the password reset link which was mailed to "a@x.com" in step 2.
5) Password will be changed.

Fix:

All previous password reset links should automatically expire once a user changes his email address.

So below is the attack scenario:

1) My email account is compromised. Attacker asks for password reset link for my account.
2) I got to know, I change my email address on my account. I now assume i am safe.
3) But the hacker can still use the old password reset links (which he had never used for single time) which were sent to my old email address.

4) My account is now compromised again.

Please let me know if you need any other information and thanks again for looking into this.

Please fix this.

Best Regards
Piyush kumar

## Attachments
No attachments
