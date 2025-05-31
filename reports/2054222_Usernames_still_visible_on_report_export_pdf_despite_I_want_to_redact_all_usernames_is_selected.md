# Usernames still visible on report export pdf despite "I want to redact all usernames" is selected

## Report Details
- **Report ID**: 2054222
- **URL**: https://hackerone.com/reports/2054222
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-07-06T22:57:40.427Z
- **Disclosed**: 2023-08-08T08:24:05.630Z

## Reporter
- **Username**: japz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

Hi Team,

Export report via .pdf still disclosing the reporter username despite I exported it with __"I want to redact all usernames"__ being selected to redact all the usernames.

{F2475645}

### Steps To Reproduce

1. Login and try to export any report using export as .pdf
2. Select "I want to redact all usernames"
3. Check the exported .pdf report is still disclosing the username of researcher

https://hackerone.com/reports/<REPORT-ID>.pdf?redact_usernames=true&pdf_type=reporter

PoC screenshot below:

█████

The .pdf looks messy (maybe design issue) but if you will take a look at __Reported by:__ section at the report header, you will see: `<REDACTED> (<REDACTED>j<REDACTED>a<REDACTED>p<REDACTED>z<REDACTED>)` If you removed the `<REDACTED>` it will show the username `japz`.

If you removed all `<REDACTED>`, you will see something like the screenshot below:

█████

## Impact

Information Disclosure

## Attachments
- poc0.PNG
