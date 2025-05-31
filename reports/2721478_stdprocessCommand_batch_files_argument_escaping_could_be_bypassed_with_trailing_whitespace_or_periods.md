# `std::process::Command` batch files argument escaping could be bypassed with trailing whitespace or periods

## Report Details
- **Report ID**: 2721478
- **URL**: https://hackerone.com/reports/2721478
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-09-16T16:45:35.880Z
- **Disclosed**: 2024-11-22T16:21:32.018Z

## Reporter
- **Username**: 4xpl0r3r
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
On April 9th, 2024, the Rust Security Response WG disclosed CVE-2024-24576, where std::process::Command incorrectly escaped arguments when invoking batch files on Windows. We were notified that our fix for the vulnerability was incomplete, and it was possible to bypass the fix when the batch file name had trailing whitespace or periods (which are ignored and stripped by Windows).

The severity of the incomplete fix is low, due to the niche conditions needed to trigger it. Note that calculating the CVSS score might assign a higher severity to this, but that doesn't take into account what is required to trigger the incomplete fix.

The incomplete fix is identified by CVE-2024-43402.

## Impact

All Rust versions before 1.81.0 are affected, if your code or one of your dependencies invoke a batch script on Windows with trailing whitespace or trailing periods in the name, and pass untrusted arguments to it.

## Attachments
No attachments
