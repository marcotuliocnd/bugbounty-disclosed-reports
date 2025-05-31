# Allowance of Meta/Null characters

## Report Details
- **Report ID**: 274013
- **URL**: https://hackerone.com/reports/274013
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-10-03T09:17:16.834Z
- **Disclosed**: 2017-10-04T01:34:50.283Z

## Reporter
- **Username**: saikiran-10097
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
Dear sir,

I am very happy to report a vulnerability to legalrobot.  Recently, the report #260468 is disclosed publicly and that report describes about the restriction lengths of profile fields "first name and last name".  Now, i am reporting an another vulnerability regarding those profile fields "first name and last name and also Bio field".

Vulnerability:-
->Meta characters are not being filtered in "First Name and Last Name" and "Bio" fields while creating a profile on app.legalrobot.com

Description:-
->You haven't filtered control meta characters such as %00 etc; in full name field and bio field, it allows an attacker to impersonate or hide their real identity within the application.
->It turns out that it is possible to register a user's full name and also bio field can be updated with special sign %0a(appended in proxy).

Impact:-
->An attacker can impersonate user by appending meta characters.

Steps to reproduce:-
->Go to app.legalrobot.com and create an account
->Now go to profile
->By using meta characters, fill the name fields and bio fields
->You profile will get updated.

Mitigation:-
->You should disallow null bytes in the "Name" and "Bio" fields.
->That is by filtering full_name to only unicode word characters and a limited set of special characters.

Any issues, please let me know.

Thank you

## Attachments
No attachments
