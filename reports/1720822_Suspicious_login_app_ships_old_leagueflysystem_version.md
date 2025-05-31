# Suspicious login app ships old league/flysystem version

## Report Details
- **Report ID**: 1720822
- **URL**: https://hackerone.com/reports/1720822
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2022-10-03T14:32:41.025Z
- **Disclosed**: 2023-02-08T05:44:19.588Z

## Reporter
- **Username**: mik-patient
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
The vulnerability allows a remote attacker to compromise vulnerable system.
The vulnerability exists due to a race condition. A remote attacker can send a specially crafted request and execute arbitrary code on the target system.
`Flysystem: 0.1.0 - 2.1.0`


https://github.com/nextcloud/suspicious_login/
```php
<?php
namespace League\Flysystem;
use RuntimeException;
final class CorruptedPathDetected extends RuntimeException implements FilesystemException
{
    public static function forPath(string $path): CorruptedPathDetected
    {
        return new CorruptedPathDetected("Corrupted path detected: " . $path);
    }
}
```
```php
   {
        $path = str_replace('\\', '/', $path);
        $path = $this->removeFunkyWhiteSpace($path);
        $this->rejectFunkyWhiteSpace($path);
```

**Supporting References:**
The unicode whitespace removal has been replaced with a rejection (exception).
The library has been patched in:
 * [1.x: thephpleague/flysystem@f3ad691](https://github.com/thephpleague/flysystem/commit/f3ad69181b8afed2c9edf7be5a2918144ff4ea32)
 * [2.x: thephpleague/flysystem@a3c694d](https://github.com/thephpleague/flysystem/commit/a3c694de9f7e844b76f9d1b61296ebf6e8d89d74)

**CVE-2021-32708**
`CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`
[GHSA-9f46-5r25-5wfm](https://github.com/thephpleague/flysystem/security/advisories/GHSA-9f46-5r25-5wfm)

## Impact

The whitespace normalisation using in 1.x and 2.x removes any unicode whitespace. Under certain specific conditions this could potentially allow a malicious user to execute code remotely.

The conditions:
 * A user is allowed to supply the path or filename of an uploaded file.
 * The supplied path or filename is not checked against unicode chars.
 * The supplied pathname checked against an extension deny-list, not an allow-list.
 * The supplied path or filename contains a unicode whitespace char in the extension.
 * The uploaded file is stored in a directory that allows PHP code to be executed.

Given these conditions are met a user can upload and execute arbitrary code on the system under attack.

## Attachments
No attachments
