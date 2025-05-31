# password token validation

## Report Details
- **Report ID**: 275242
- **URL**: https://hackerone.com/reports/275242
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-10-06T21:03:00.040Z
- **Disclosed**: 2017-10-07T10:10:00.429Z

## Reporter
- **Username**: flex0geek
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
Hello,
when I reset password all tokens are valid can be used, should keep valid only token in the last request or you can invalidate all reset links after using one of the requests successfully.

Steps:
1) go to the password reset page and request more than one request.
2) go to your email and use the first reset link.
3) you can change password successfully.

Please check it,
Thanks.

## Attachments
No attachments
