# Avoid "resend verification email" confusion

## Report Details
- **Report ID**: 156542
- **URL**: https://hackerone.com/reports/156542
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-08-04T17:04:33.865Z
- **Disclosed**: 2017-03-20T17:07:44.516Z

## Reporter
- **Username**: s_p_q_r
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Let's assume Alice has a Gratipay account https://gratipay.com/~alice and an alice@foo.com email

1. Mallory creates an a‎**1**‎ice@foo\.com email address, base64-encodes it, and sends Alice a link https://gratipay.com/~alice/emails/verify.html?email2=YTFpY2VAZm9vLmNvbQ~~&nonce=x
2. When Alice opens the link, she sees a notification "The verification code for a1ice@foo.com is bad. Resend verification email"
3. If she clicks the "Resend verification email" button, that fake a‎**1**‎ice@foo\.com email will be automatically associated with her account, and a valid verification link will be sent there.
4. Mallory opens her a‎**1**‎ice@foo\.com inbox, gets the verification link, and sends it to Alice.
5. After Alice opens it, the email will be successfully verified, so Mallory will receive all Alice's notifications.

**The way to fix:**

You shouldn't give Alice a chance to accidentally add any emails to her account, without knowing that: on step 3 a verification link should be sent only if the email is already associated with the Alice's account. If no, there should be just an error message with no "Resend verification email" button.

## Attachments
No attachments
