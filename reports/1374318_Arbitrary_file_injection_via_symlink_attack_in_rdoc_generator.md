# Arbitrary file injection via symlink attack in rdoc generator

## Report Details
- **Report ID**: 1374318
- **URL**: https://hackerone.com/reports/1374318
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-10-19T11:51:48.135Z
- **Disclosed**: 2023-07-18T08:43:02.493Z

## Reporter
- **Username**: sighook
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
There is a vulnerability that can allow an attacker to spoof the symbolic link and traverse the file system to unintended locations or access arbitrary files. The symbolic link can permit an attacker to read  a file that they originally did not have permissions to access and to inject its content to the placed-on-the-web documentation.

# PoC

1.
```sh
$ mkdir test
$ cd test
$ ln -s /etc/passwd test
$ rdoc
```
2.
See `doc/test.html` and `doc/js/search_index.js`, they contain the data of `/etc/passwd`.

The spoofed link can refer to files in `~/.ssh`, `~/.gnupg`, `/etc`, `/proc`/, `/sys`, thus, the nature of the disclosed data varies from secrets/credentials to system configurations, hardware info, firewall rules,  and so on.

## Impact

An attacker could gain access to sensitive data or system resources. This could allow access to protected files or directories including configuration files and files containing sensitive information.

## Attachments
No attachments
