# Incorrect Functionality of Password reset links

## Report Details
- **Report ID**: 280529
- **URL**: https://hackerone.com/reports/280529
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-10-19T14:45:49.949Z
- **Disclosed**: 2017-10-30T09:23:39.528Z

## Reporter
- **Username**: saikiran-10099
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: infogram

## Vulnerability Information
Vulnerability:-
->Password reset links should work in such a way that "only the last generated password reset link should be valid" i.e; if two tokens are generated at a time, then 2nd token must work and 1st token must be invalid.
->If not, another case is that "if some number of reset links are generated at a time, if any one link is used in that links, then all remaining links should get invalid".

This is the standard practice followed and implemented by all secured websites that are running bug bounty programs on hackerone.

Any issues, please let me know...

Thank you 

## Attachments
No attachments
