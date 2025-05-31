# Fix : (Security) Mitigate Path Traversal Bug

## Report Details
- **Report ID**: 1635321
- **URL**: https://hackerone.com/reports/1635321
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-07-13T06:20:36.282Z
- **Disclosed**: 2022-08-05T21:41:29.606Z

## Reporter
- **Username**: bhaskar_ram
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: hyperledger

## Vulnerability Information
Unsanitized input from arg[0] argument flows into java.io.FileOutputStream, where it is used as a path. This may result in a Path Traversal vulnerability and allow an attacker to write to arbitrary files.

## Impact

Being able to access and manipulate an arbitrary path leads to vulnerabilities when a program is being run with privileges that the user providing the path should not have. A website with a path traversal vulnerability would allow users access to sensitive files on the server hosting it. CLI programs may also be vulnerable to path traversal if they are being ran with elevated privileges (such as with the setuid or setgid flags in Unix systems)

## Attachments
No attachments
