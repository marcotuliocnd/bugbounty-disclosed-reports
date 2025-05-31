# Stored XSS in plan name field (Acronis Cyber Protect)

## Report Details
- **Report ID**: 1940788
- **URL**: https://hackerone.com/reports/1940788
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-04-10T13:47:42.038Z
- **Disclosed**: 2023-10-09T09:49:10.984Z

## Reporter
- **Username**: und3sc0n0c1d0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary
It has been identified that a known and previously reported stored XSS vulnerability is still possible to be exploited and abused in the recent version of Acronis Cyber Protect (*15.0.31791*), released last March 7, 2023, (*evidence attached*).
This report is for no other purpose than to make it known that the vulnerability still persists.

## Steps To Reproduce
Be sure to follow the steps below to replicate this vulnerability:

  1. Create a new plan. Add a valid device.
  1. As plan name type the following payload: `<img src=x onerror=alert(/Stored_XSS/)>`
  1. Save the changes and wait for the plan to be created.
  1. Now stop the plan by pressing the "Stop" button.
  1. Before stopping it will ask for confirmation. Press the red "Confirm" button and the vulnerability will be triggered immediately.

Note that just below the browser window a bubble will appear with a temporary message trying to render our payload.

## Recommendations
You can avoid such vulnerabilities by escaping, validating data entries in fields and sanitizing suspicious and/or malicious entries. This text field is not supposed to contain/accept special characters or payloads.

## Impact

An XSS attack allows an attacker to execute arbitrary JavaScript in the context of the attacked website and the attacked user. This can be abused to steal session cookies, perform requests in the name of the victim or for phishing attacks.

## Attachments
- 2023-04-10_XSS_Acronis_2.png
- 2023-04-10_XSS_Acronis_1.png
- 2023-04-10_XSS_Acronis_3.png
