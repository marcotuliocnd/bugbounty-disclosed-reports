# Disclosure of h1 challenges name through the calendar

## Report Details
- **Report ID**: 488643
- **URL**: https://hackerone.com/reports/488643
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-01-30T16:16:01.379Z
- **Disclosed**: 2019-01-30T21:53:55.135Z

## Reporter
- **Username**: rijalrojan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

It seems like the Calendar somehow grabs the name of the target for a h1 challenge even though the target name is not public. 

**Description:**

`h1challenges` do not disclose the name of the target until the time it starts. For example for this challenge: █████ the name of the target is not disclosed anywhere and the page looks something like this: 

█████

However, once we import the calendar on something like Google calendar, it shows the name of the target: 

█████████

This is super useful specially because sometimes program run multiple challenges in short period of time. For example, knowing more about this challenge (the name of the target), a hacker can hack and hodl bugs until the program starts. 

### Steps To Reproduce

1. Add yourself to challenge like the one linked above.
2. Link/update your Google Calendar with the hackerone events calendar.
3. Find the date in the calendar when the challenge is set to start and you can see the name there.

## Impact

Disclosure of h1c-* challenge targets.

## Attachments
No attachments
