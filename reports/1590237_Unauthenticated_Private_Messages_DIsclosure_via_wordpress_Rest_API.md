# Unauthenticated Private Messages DIsclosure via wordpress Rest API

## Report Details
- **Report ID**: 1590237
- **URL**: https://hackerone.com/reports/1590237
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-06-03T04:28:27.921Z
- **Disclosed**: 2022-08-04T10:45:17.078Z

## Reporter
- **Username**: ghimire_veshraj
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
Vulnearble Plugin: Senei LMS

Hi there,
Hope you are doing well,
So, i noticed that their is an option to contact teacher on Sensei LMS which is meant to private.
By default, other user can't see the question I asked to the teacher.
But using the  `/wp-json/wp/v2/sensei-messages/<numericID>` where numeric ID can be bruteforced.
Those private questions asked to teacher is still visible to any Unauthenticated User.
{F1754958}

Steps to reproduce:
Create any course then as a student, ask question on that course.
Now, the message is visible through `/wp-json/wp/v2/sensei-messages/<numericID>` 
Sensei LMS lacks authentication in a REST API endpoint, allowing unauthenticated users to discover private questions sent between teacher and student on the site.

## Impact

Disclosure of Private Questions to Unauthenticated User.

## Attachments
- Screen_Shot_2022-06-03_at_10.08.45_AM.png
