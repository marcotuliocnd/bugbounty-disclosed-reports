# CSV injection in gratipay.com via payment history export feature.

## Report Details
- **Report ID**: 219323
- **URL**: https://hackerone.com/reports/219323
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-07T15:58:07.218Z
- **Disclosed**: 2017-11-03T07:55:04.511Z

## Reporter
- **Username**: edoverflow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
I discovered this issues thanks to Matt who pointed out that the participant's name is directly placed into a CSV file: https://github.com/gratipay/gratipay.com/issues/4399#issuecomment-292250609

# Summary
---

Gratipay allows users to export payment history as a .csv file. By injecting a payload into a participant's name an attacker could exfiltrate data or execute code on the target machine. For instance, with `=cmd|' /C calc'!A0` I am able to open up `calc.exe` on Windows.

# Steps to reproduce
---

1) Create a user A called `=cmd|' /C calc'!A0`;
2) User B donates a small sum to user A;
3) Export payment history from B;
4) Open the .csv file on a Windows machine.

Result: `calc.exe` pops up.

# Fix
---

Prefix `=`, `+`, `-` and `@` symbols with a `'` in issues when exporting them to a .csv file.

## Attachments
No attachments
