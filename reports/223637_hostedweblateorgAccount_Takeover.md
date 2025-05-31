# [hosted.weblate.org]Account Takeover

## Report Details
- **Report ID**: 223637
- **URL**: https://hackerone.com/reports/223637
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-25T03:23:39.968Z
- **Disclosed**: 2017-05-17T14:09:10.628Z

## Reporter
- **Username**: 0xspade
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hello Team,

**Steps to Reproduce:**

* Go to Login Page
* Reset Your Password by Clicking `Reset it`.
* Put your email and answer the captcha.
* Go to your email and click your reset Link.
* You dont need to Change Your Password because you'll be logged in.

**Scenario**
Victim forgot to logout his/her Email Account on a Cafe/Internet Renting Shops. The Attacker Click the Reset Password link and because that Improper InValidation of Session on Password Reset Links lies in there. Attacker can gain access to Victim's Account.

Let me know if you need more information.

Best Regards,




## Attachments
No attachments
