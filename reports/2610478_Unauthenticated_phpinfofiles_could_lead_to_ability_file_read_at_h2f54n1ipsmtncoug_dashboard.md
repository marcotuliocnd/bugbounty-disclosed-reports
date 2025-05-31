# Unauthenticated phpinfo()files could lead to ability file read at h2f54.n1.ips.mtn.co.ug [/dashboard/]

## Report Details
- **Report ID**: 2610478
- **URL**: https://hackerone.com/reports/2610478
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-07-18T12:09:41.105Z
- **Disclosed**: 2025-02-20T13:32:26.825Z

## Reporter
- **Username**: odaysec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary 
Many PHP installation tutorials instruct the user to create a PHP file that calls the PHP function 'phpinfo()' for debugging purposes, and various PHP applications may also include such a file by default. By accessing it, a remote attacker can discover a large amount of information about the remote web server configuration to help conduct further attacks, including :
 * root/vps of the web server, operating system and PHP components
 * Details of the PHP configuration
 * Loaded PHP extensions with their configurations
 * Server environment variables.


**Proof On Concepts:**
https://h2f54.n1.ips.mtn.co.ug/dashboard/phpinfo.php
```
Windows NT SUNSVR 6.3 build 9600 (Windows Server 2012 R2 Datacenter Edition) AMD64
```

## Steps to Reproduce
* Visit the target scope is https://h2f54.n1.ips.mtn.co.ug
 * You can used `burp-suite-intruder` for finding sensitive directory
 * And now we found a directory is `info.php`
 * Let's see opened in our browser is directory https://h2f54.n1.ips.mtn.co.ug/dashboard/phpinfo.php
 * You can see this page can be view without authenticate

## Suggested Mitigation/Remediation Actions
Remove the affected file(s).
http://php.net/manual/en/function.phpinfo.php

## Impact

The remote web server contains a PHP script that is prone to an information disclosure attack.

## Attachments
No attachments
