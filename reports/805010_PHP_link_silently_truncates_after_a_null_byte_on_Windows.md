# PHP link() silently truncates after a null byte on Windows

## Report Details
- **Report ID**: 805010
- **URL**: https://hackerone.com/reports/805010
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-02-26T05:04:15.342Z
- **Disclosed**: 2020-11-09T01:49:11.631Z

## Reporter
- **Username**: ryat
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
The bug submitted at: https://bugs.php.net/bug.php?id=78862
The security advisory at: https://nvd.nist.gov/vuln/detail/CVE-2019-11044

The issue allow remote attackers to read or write arbitrary files via crafted input to an application that calls the vulnerable function. As demonstrated by a file\0.ext attack that bypasses an intended configuration in which users may read or write only files.

## Impact

In PHP versions 7.2.x below 7.2.26, 7.3.x below 7.3.13 and 7.4.0 on Windows, PHP link() function accepts filenames with embedded \0 byte and treats them as terminating at that byte. This could lead to security vulnerabilities, e.g. in applications checking paths that the code is allowed to access.

## Attachments
No attachments
