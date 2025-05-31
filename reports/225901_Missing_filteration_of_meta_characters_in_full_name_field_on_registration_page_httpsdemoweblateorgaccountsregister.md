# Missing filteration of meta characters in full name field on registration page https://demo.weblate.org/accounts/register

## Report Details
- **Report ID**: 225901
- **URL**: https://hackerone.com/reports/225901
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-05-03T18:12:13.436Z
- **Disclosed**: 2017-05-22T12:38:16.209Z

## Reporter
- **Username**: sumit7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi there

#Vulnerability Title:
>Meta characters are not filtered into full name on registration page

#Description
>You haven't filtered control meta characters such as %00 etc in full name field on registration page which allows an attacker to impersonate or hide their real identity within the application.
This one is not rejected. It  turns out that it is possible to register a user's full name with special sign %0a(appended in proxy).

#Impact
>Attacker can impersonate user by appending meta characters.

#Mitigation
>You should disallow nullbytes in the name(here full name field).

Happy to Help

Thanks
@smit

## Attachments
No attachments
