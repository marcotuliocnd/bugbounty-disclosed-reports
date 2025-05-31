# HTML Injection in email via Name field

## Report Details
- **Report ID**: 1581499
- **URL**: https://hackerone.com/reports/1581499
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-05-26T00:34:30.261Z
- **Disclosed**: 2022-09-18T09:24:10.106Z

## Reporter
- **Username**: mega7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hello Gents,
I would like to report an issue where attackers are able to inject HTML into the `Name` field at `app.qualified.dev`.

### Steps to reproduce:
1. Please register at https://app.qualified.dev/signup
2. Inject the `Name`field with any HTML payload.
3. Open the victim's test email, HTML will be executed.

### Proof of concept:
+ {F1744498}

## Impact

HTML Injection

## Attachments
- simplescreenrecorder-2022-05-26_02.31.53.mp4
