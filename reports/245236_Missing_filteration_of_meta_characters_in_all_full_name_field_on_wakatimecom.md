# Missing filteration of meta characters in all full name field on wakatime.com

## Report Details
- **Report ID**: 245236
- **URL**: https://hackerone.com/reports/245236
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-07-02T02:13:23.768Z
- **Disclosed**: 2017-07-04T01:57:20.555Z

## Reporter
- **Username**: silv3rpoision
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
Hi there

Vulnerability Title:

Meta characters are not filtered into full name

Description

You haven't filtered control meta characters such as %00 etc in full name field which allows an attacker to impersonate or hide their real identity within the application.
This one is not rejected. It turns out that it is possible to register a user's full name with special sign %0a(appended in proxy).

Impact

Attacker can impersonate user by appending meta characters.

Mitigation

You should disallow nullbytes in the name(here full name field).

Happy to Help

Thanks
Piyush kumar

## Attachments
No attachments
