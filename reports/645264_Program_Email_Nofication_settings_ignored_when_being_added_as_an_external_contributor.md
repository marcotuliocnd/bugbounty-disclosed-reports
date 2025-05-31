# Program Email Nofication settings ignored when being added as an external contributor

## Report Details
- **Report ID**: 645264
- **URL**: https://hackerone.com/reports/645264
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-07-16T15:52:36.845Z
- **Disclosed**: 2019-08-07T23:01:26.824Z

## Reporter
- **Username**: archangel
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

When being added as an external contributor to a report, the report title are displayed in the email notification despite the program email notification settings being set to `No Content`

**Description:**

Hey team!

I noticed that programs have the ability to set their Email Notification settings, to `No Content`, which masks the report title:

{F530569}

This causes the hackers emails notifications to look like this:

███████

HOWEVER, if another hacker gets added as an external contributor to the report, the report title and activity are shown in the report:


{F530572}


### Steps To Reproduce

1. As a Program admin, navigate to `Program Settings`
2. Click `Program`
3. Click `Email Notifications`
4. Click `No Content`
5. Go to any report in your program and invite any hacker to the report.
6. Check the hackers email, they will see the report title in the invitation email


Hope that helps!

## Impact

Information Disclosure bypassing a program setting

## Attachments
- Screen_Shot_2019-07-16_at_8.47.29_AM.png
- Screen_Shot_2019-07-16_at_8.48.39_AM.png
