# Unauthenticated phpinfo()files could lead to ability file read at █████████  [HtUS]

## Report Details
- **Report ID**: 1794884
- **URL**: https://hackerone.com/reports/1794884
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-12-06T15:06:04.239Z
- **Disclosed**: 2023-01-06T19:12:57.634Z

## Reporter
- **Username**: hackeronanywhere
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
Many PHP installation tutorials instruct the user to create a PHP file that calls the PHP function 'phpinfo()' for debugging purposes, and various PHP applications may also include such a file by default. By accessing it, a remote attacker can discover a large amount of information about the remote web server configuration to help conduct further attacks, including :
 * root/vps of the web server, operating system and PHP components
 * Details of the PHP configuration
 * Loaded PHP extensions with their configurations
 * Server environment variables.


**Proof On Concepts:**
https://███████/info.php
```
Linux ███████ 3.10.0-1160.80.1.el7.x86_64 #1 SMP Sat Oct 8 18:13:21 UTC 2022 x86_64
```

## Impact

The remote web server contains a PHP script that is prone to an information disclosure attack.

## System Host(s)
███

## Affected Product(s) and Version(s)
https://███████/info.php

## CVE Numbers


## Steps to Reproduce
* Visit the target scope is https://██████████
 * You can used `burp-suite-intruder` for finding sensitive directory
 * And now we found a directory is `info.php`
 * Let's see opened in our browser is directory https://████████/info.php
 * You can see this page can be view without authenticate

## Suggested Mitigation/Remediation Actions
Remove the affected file(s).
http://php.net/manual/en/function.phpinfo.php



## Attachments
No attachments
