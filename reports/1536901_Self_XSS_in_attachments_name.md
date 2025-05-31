# Self XSS in attachments name

## Report Details
- **Report ID**: 1536901
- **URL**: https://hackerone.com/reports/1536901
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-04-10T22:01:58.868Z
- **Disclosed**: 2022-05-31T09:10:35.148Z

## Reporter
- **Username**: mega7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Hello Gents,
> + While testing `account.acronis.com` I found that I could inject XSS payload in attachments name at  **"Support requests"** .

### Steps to Reproduce:
1. Please Login at `account.acronis.com`.
2. From support request, support a new case.
3. Expand Case ID,  Leave a comment for support professional, upload a file: `"><img src="x" onerror="alert(document.domain)">.png`.


### Proof of Concept:
{F1687467}

## Impact

XSS

## Attachments
- simplescreenrecorder-2022-04-10_23.54.05.mp4
