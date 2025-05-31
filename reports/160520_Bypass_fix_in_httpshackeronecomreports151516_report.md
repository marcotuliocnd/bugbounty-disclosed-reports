# Bypass fix in https://hackerone.com/reports/151516 report.

## Report Details
- **Report ID**: 160520
- **URL**: https://hackerone.com/reports/160520
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-08-18T20:27:27.247Z
- **Disclosed**: 2016-10-12T04:04:29.634Z

## Reporter
- **Username**: 0x01alka
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: iandunn-projects

## Vulnerability Information
Hi.

**Steps to reproduce:**

1. The same in previous https://hackerone.com/reports/151516 report.
2. But payload to bypass your fix would be like this: `;=cmd|' /C calc'!A0`

**Solution:**

1. Add `;` in your escape function esc_csv() on line 2858 of camptix.php

**References:**

1. https://www.owasp.org/index.php/CSV_Excel_Macro_Injection

Tested on Windows 7 64 + Microsoft Office Exel 2003(think will work and on later versions)

Regards.

## Attachments
- 1.jpg
- 2.jpg
