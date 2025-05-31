# Email Verification Bypass Allows Users to Add & verify Any Email  As Guardians Email 

## Report Details
- **Report ID**: 1636552
- **URL**: https://hackerone.com/reports/1636552
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-07-14T08:35:48.817Z
- **Disclosed**: 2022-12-17T02:33:28.678Z

## Reporter
- **Username**: shuvam321
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: khanacademy

## Vulnerability Information
1. Go to https://www.khanacademy.org/signup and signup as learner keeping date of birth below 13 years.
{F1821117}
2. Now keep victims email as parent's email for example here I am keeping info@khanacademy.org as parents email and click on signup.
████
3. Now you will see a following message "Your parent or guardian must approve your account or it will be deleted in 7 days".
██████
4. Now go to https://www.khanacademy.org/settings/account and update your email to temporary email or any email you have access to.
██████████
██████
5. Now, you will receive a verification email in your temporary email you have access to. But don't click on the email. Now again change the email to info@khanacademy.org.

{F1821137} ███████
6. Now open the verification email you received in your temporary email account in an incognito tab and refresh your child's account. We have successfully tied info@khanacademy.org as parent account with email verification.

This is the account that I created : Username : ██████ Password : ██████████ Email : ████

█████████

## Impact

Attacker is able to bypass email verification.

## Attachments
- Screenshot_at_2022-07-14_13-54-59.png
- Screenshot_at_2022-07-14_14-09-48.png
