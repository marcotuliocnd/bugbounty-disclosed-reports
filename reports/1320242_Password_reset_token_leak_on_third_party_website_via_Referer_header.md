# Password reset token leak on third party website via Referer header [██████████]

## Report Details
- **Report ID**: 1320242
- **URL**: https://hackerone.com/reports/1320242
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-08-26T13:18:36.314Z
- **Disclosed**: 2022-09-01T20:21:48.701Z

## Reporter
- **Username**: ibrahimatix0x01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:

██████████

It has been identified that the application is leaking referrer token to third party sites. In this case it was found that the password reset token is being leaked to third party sites which is a issue knowing the fact that it can allow any malicious users to use the token and reset the passwords of the victim.

##Steps To Reproduce:

1) Request a password reset link for a valid account on ████████
2) Click on the reset link from your link
3) Before resetting the password click on the Facebook link footer section
4) You will notice the following request in Burpsuite

## Supporting Material/References:

## Impact

As you can see in the referrer the reset token is getting leaked to third party sites. So, the person who has the complete control over that particular third party site can compromise the user accounts easily.

## Attachments
No attachments
