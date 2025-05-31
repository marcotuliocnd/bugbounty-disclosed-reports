# Validation of Password reset tokens

## Report Details
- **Report ID**: 273560
- **URL**: https://hackerone.com/reports/273560
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-10-01T07:59:47.492Z
- **Disclosed**: 2017-10-01T14:56:19.826Z

## Reporter
- **Username**: saikiran-10097
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
Dear sir,
At first, i am very happy to report an issue.  Before three months, i reported to wakatime and again i am reporting another issue now.

Note:-This report is similar to #244614 which was previously reported at the start of this bug bounty program.

Vulnerability:-
->If two password reset tokens are generated at a time, then the first reset token doesn't expire after the generation of second reset token.
->Similarly, if 100 password reset tokens are generated then only the last generated reset token should be valid, but here all 100 tokens are being valid until any one in it is used to change password.
->As per industrial standards, and also as a best security issue, only one token should be valid at a time but not all the tokens.

I hope that you will resolve this issue as i am reporting a valid issue.  Any issues, please let me know

Thank you

## Attachments
No attachments
