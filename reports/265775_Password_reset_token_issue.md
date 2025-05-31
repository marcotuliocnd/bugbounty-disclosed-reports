# Password reset token issue

## Report Details
- **Report ID**: 265775
- **URL**: https://hackerone.com/reports/265775
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-09-04T12:02:42.475Z
- **Disclosed**: 2017-09-05T00:23:31.684Z

## Reporter
- **Username**: ghoibsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
##Summary
Can still change password without token

##Step to Reproduce

- Request for password reset link.
- Go to email and click on password reset link https://app.legalrobot.com/password-reset/token?v=uWe_yFJS0-N9fIk0nG0b0NZ70lkwNNi7RdUZu0KhiaX
- Now remove the token and use the link https://app.legalrobot.com/password-reset

Observe that able to reset the password without the token.

##Fix :
Always password reset link should work with a valid token.

##Reference :
https://hackerone.com/reports/253934

Thanks,
tell me if you need video. i'll create one.

## Attachments
No attachments
