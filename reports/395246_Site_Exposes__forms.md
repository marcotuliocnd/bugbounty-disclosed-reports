# ███████ Site Exposes █████████ forms

## Report Details
- **Report ID**: 395246
- **URL**: https://hackerone.com/reports/395246
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-08-14T19:53:38.495Z
- **Disclosed**: 2019-04-05T19:45:03.914Z

## Reporter
- **Username**: cablej_dds
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
## Summary

The █████ site (https://██████.mil/) allows authenticated users to submit ██████ e-forms. Due to a vulnerability in this system, any authenticated user can access the full █████████ e-form of any other user.

## Steps to reproduce

1. Intercept an authenticated request on █████████ containing an Authorization header.
2. Replace the url with `█████████`. Observe that the id in the url can be incremented/decremented to view recently generated OMPFs.
3. Upon submitting the request, the user's full ███████ form JSON response will be sent.

## Impact

Access to ████ is possible through either a Department of Defense Self-Service logon, CAC card, or █████████password. Thus, a compromise of a single account on any of these systems would allow for unrestricted access to all ████ forms.

The ████ form includes the following
- PII such as SSN, DoB, addresses, etc
- Personal remarks
- Other fields related to security clearances, education, maritial status, etc

## Attachments
No attachments
