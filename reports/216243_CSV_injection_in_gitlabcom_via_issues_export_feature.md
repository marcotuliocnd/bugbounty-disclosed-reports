# CSV injection in gitlab.com via issues export feature.

## Report Details
- **Report ID**: 216243
- **URL**: https://hackerone.com/reports/216243
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-03-26T15:58:04.615Z
- **Disclosed**: 2017-07-21T06:14:48.309Z

## Reporter
- **Username**: edoverflow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Dear GitLab bug bounty team,

# Summary
---

GitLab allows users to export issues as a .csv file. By injecting a payload into an issue title an attacker could exfiltrate data or execute code on the target machine. For instance, by naming an issue `=cmd|' /C calc'!A0` I am able to open up calc.exe on Windows.

# Steps to reproduce
---

1) Create an issue with `=cmd|' /C calc'!A0` as the title;
2) Export all issues (The file is sent as an email attachment);
3) Open the .csv file on a Windows machine.

**Result:** calc.exe pops up.

# Fix
---

Prefix `=`, `+`, `-` and `@` symbols with a `'` in issues when exporting them to a .csv file.

If you require any further information, feel free to contact me.

Best regards,
Ed

## Attachments
No attachments
