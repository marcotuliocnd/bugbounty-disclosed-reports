# Unsafe usage of Host HTTP header in Concrete5 version 5.7.3.1

## Report Details
- **Report ID**: 59666
- **URL**: https://hackerone.com/reports/59666
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-05-05T09:26:07.592Z
- **Disclosed**: 2018-01-11T21:59:17.230Z

## Reporter
- **Username**: egix
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: concretecms

## Vulnerability Information
Concrete5 is affected by a design issue related to the Host HTTP header. Such header is being used to define the base URL for the application. Since the Host header can be arbitrarily manipulated by an attacker, this can have some security impacts.

## Attachments
- Concrete5-Host-Header.pdf
