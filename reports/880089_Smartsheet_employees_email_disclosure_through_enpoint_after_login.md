# Smartsheet employees email disclosure through enpoint after login.

## Report Details
- **Report ID**: 880089
- **URL**: https://hackerone.com/reports/880089
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-05-21T22:26:46.684Z
- **Disclosed**: 2020-09-09T22:15:47.207Z

## Reporter
- **Username**: soareswallace
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: smartsheet

## Vulnerability Information
## Summary:
[add summary of the vulnerability]
After login  - while validating this issue [#858974](https://hackerone.com/reports/858974) - I notice there is an endpoint call `/b/home?formName=webop&formAction=SheetLabLoadData&to=68000&ss_v=98.0.2` that is bringing emails from some employees.

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Login with your account
  2. While tracking traffic with your favorite traffic tracker capture the endpoint mentioned in the summary.
  3. Check the response

I honestly search in the dashboard where this information could be used and didn't founded it. Do we need this endpoint call?

## Bug Behavior
Expected: Do we need this information while loading the dashboard?
Actual: Employees email and name are being disclosed in the response

## Supporting Material/References:
[#858974](https://hackerone.com/reports/858974)

## Impact

Unnecessarily disclosing employee emails via endpoint call.

## Attachments
No attachments
