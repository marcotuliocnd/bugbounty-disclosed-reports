# Wordpress VIP leaks email of the test a/c

## Report Details
- **Report ID**: 540301
- **URL**: https://hackerone.com/reports/540301
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-04-16T16:33:23.606Z
- **Disclosed**: 2019-05-28T03:46:03.684Z

## Reporter
- **Username**: cryptordx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
i was testing learn.fb.com and i came to known that its wp-json is open and when i saw all the routes of the websites than i got to known that one end-point is leaking their internal email address 
the endpoint is as follow
https://learn.fb.com/wp-json/th/v1/user_generation
The issue has been fixed by fb but they told me to report the bug here for the bounty. So, i reported the issue here

==========================================
This is what facebook security engineer told me. So, am reporting this issue here and before this i have not tested wordpress VIP.
We've been in touch with the WordPress.com VIP team regarding this issue, and it looks like they consider this issue to have potentially affected a wider set of sites on their platform than just ours. Because of this, we ask that you submit the full details of this report to their HackerOne program so it can be reviewed and considered for a bounty from their end.
=====================================

## Impact

Email disclosure

## Attachments
No attachments
