# Password reset token leakage via referer

## Report Details
- **Report ID**: 342693
- **URL**: https://hackerone.com/reports/342693
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-04-24T10:25:00.266Z
- **Disclosed**: 2018-08-14T13:25:02.602Z

## Reporter
- **Username**: mansishah
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semrush

## Vulnerability Information
Hi Team,
I have found that if user open the link of reset password and than click on any external links within the reset password page its leak password reset token in referer header.

Steps to reproduce:

1.Open Password reset page from email. 
2.Click on any social media link(on follow us section)
3.Intercept the request(I have used burp suite) 
4.You can see the link for reset password in referrer

## Impact

It allows the person who has control of particular site to change the user's password (CSRF attack), because this person knows reset password token of the user.

## Attachments
- Screenshot_11.png
