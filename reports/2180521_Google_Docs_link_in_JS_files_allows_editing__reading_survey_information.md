# Google Docs link in JS files allows editing & reading survey information

## Report Details
- **Report ID**: 2180521
- **URL**: https://hackerone.com/reports/2180521
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-09-25T19:08:17.403Z
- **Disclosed**: 2023-11-04T08:17:49.373Z

## Reporter
- **Username**: bebiks
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hello HackerOne security team,

I've been monitoring your JS files for a while now. I've just noticed that a new Google Docs link appeared.
https://docs.google.com/forms/d/1cwHTgNBd51ECJ3w-5Hy6LgioJWhJ2qFF_vdlmXb6zao/edit#responses
{F2725244}

This google docs link has been leaked in JS chunk file located at:
`https://hackerone.com/assets/static/js/5930.078b8e86.chunk.js`

It allows an attacker to edit anything & view some confidential data about users such as emails/survey responses.

Have a great day!

## Impact

The attacker is able to edit the survey & view some confidential data about some users.

## Attachments
- image.png
