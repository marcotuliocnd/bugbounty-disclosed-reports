# Error Message When Changing Username

## Report Details
- **Report ID**: 243664
- **URL**: https://hackerone.com/reports/243664
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-06-27T16:46:38.944Z
- **Disclosed**: 2017-08-17T14:16:45.566Z

## Reporter
- **Username**: blake12356
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hello,

## Description:

I have found a bug in your fix other my other report, #243609. I reported this in a new report as this is an error in the error message.

When changing your username that starts with a `.` the error message is:
`Username may only contain letters, numbers or the following characters: @ . + - _`

A normal user would be confused as it does not state any reason for the `.` not being allowed at the beginning of their username.

## POC:

1. Change your username to a name that starts with a `.`.
2. You will receive an error message that does not explain why this is not excepted. 

## Mitigation:

I recommend you add a specific error message that states that your username cannot start with a `.`.

Thanks!

## Attachments
No attachments
