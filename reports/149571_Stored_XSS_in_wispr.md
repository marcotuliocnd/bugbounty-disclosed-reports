# Stored XSS in wis.pr

## Report Details
- **Report ID**: 149571
- **URL**: https://hackerone.com/reports/149571
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-06T15:10:27.616Z
- **Disclosed**: 2016-10-16T07:14:47.698Z

## Reporter
- **Username**: huntingforbugs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: whisper

## Vulnerability Information
Hi,

I detected a Stored XSS in wis.pr. These are the steps to reproduce the bug:

1. Create a new group named: Test>"<script>alert('test');</script>
2. Copy the sharing URL (http://wis.pr/*****).
3. Open this URL in a browser.

Please find the attached screenshots.

Fix: Sanitize the output in twitter:description meta. Please find attached the screenshot named "fix.jpg".

Don't hesitate to contact me if you need further details.



## Attachments
- step1.PNG
- step2.PNG
- step2_2.png
- fix.png
