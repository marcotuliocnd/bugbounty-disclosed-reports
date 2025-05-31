# Malformed .BSP Access Violation in CS:GO can lead to Remote Code Execution

## Report Details
- **Report ID**: 351014
- **URL**: https://hackerone.com/reports/351014
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-05-13T00:57:18.088Z
- **Disclosed**: 2018-07-19T21:55:29.472Z

## Reporter
- **Username**: chippy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: valve

## Vulnerability Information
A malformed .BSP can trigger an Access Violation on CS:GO that can lead to arbitrary code execution on a remote computer. I have attached a copy of the malformed .BSP which reliably triggers an Access Violation on CS:GO.

## Impact

An attacker hosting a malicious server could compromise a remote client by having them download a custom map, triggering remote code execution on the victim's computer.

## Attachments
- de_fuzz.zip
