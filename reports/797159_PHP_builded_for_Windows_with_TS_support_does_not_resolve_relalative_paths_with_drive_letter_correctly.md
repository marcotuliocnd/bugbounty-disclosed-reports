# PHP builded for Windows with TS support does not resolve relalative paths with drive letter correctly

## Report Details
- **Report ID**: 797159
- **URL**: https://hackerone.com/reports/797159
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-02-15T11:05:39.461Z
- **Disclosed**: 2020-11-09T01:47:33.238Z

## Reporter
- **Username**: vorismi3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Currently PHP process Windows paths like `C:Users` as if they were absolute. But they are not and PHP builded with TS (thread-safe support) currently points to root drive location instead of the current directory. This gives the attaker unlimited access to the root drive if a) the path is resolved/normalized by the app before used b) permissions are denied (but on Windows the system files are almost always accessible)

Reported to PHP:
https://bugs.php.net/bug.php?id=78939
https://github.com/php/php-src/pull/5001

## Impact

Attaker can get access to all files on the same drive if the path is validated by some middleware correctly but PHP then points to bad location.

Example scenario:
- PHP pwd: `C:/Web/uploads`
- path: `C:secret_data.txt`
- apps checks if the path is within pwd - yes, it is, correct resolved location should be `C:/Web/uploads/secret_data.txt`
- but PHP accesses `C:/secret_data.txt`

If app can write with user supplied path, the path can be handcrafted to point to location like `C:\Users\<USER>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup` and inject malicious file to be started when the user logs in.

## Attachments
No attachments
