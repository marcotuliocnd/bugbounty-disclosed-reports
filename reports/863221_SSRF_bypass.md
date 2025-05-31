# SSRF bypass

## Report Details
- **Report ID**: 863221
- **URL**: https://hackerone.com/reports/863221
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-04-30T13:38:41.988Z
- **Disclosed**: 2021-10-04T15:53:07.833Z

## Reporter
- **Username**: pabl00nicarres
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: concretecms

## Vulnerability Information
This simply describes a bypass for report at https://hackerone.com/reports/243865, using a decimal notation encoded IP address (0177.0.0.1
) currently bypasses the limitations in place for localhost.
crayons (re-submitting report including "magic" string)
Concrete5 version used is 8.5.2

## Impact

Interacting with local services, impact may vary depending on services actually exposed.

## Attachments
- concrete5_ssrf1.png
- concrete5_ssrf_2.png
