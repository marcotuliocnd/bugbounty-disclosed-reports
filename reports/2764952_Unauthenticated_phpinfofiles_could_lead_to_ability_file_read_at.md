# Unauthenticated phpinfo()files could lead to ability file read at █████████ 

## Report Details
- **Report ID**: 2764952
- **URL**: https://hackerone.com/reports/2764952
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-10-07T19:34:05.521Z
- **Disclosed**: 2024-11-15T02:30:57.252Z

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
█████
```
Linux uggogamesdb 5.4.17-2136.323.8.2.el8uek.x86_64 #2 SMP ████ █████ PDT 2023 x86_64
```

## Steps to Reproduce
* Visit the target scope is ██████
 * You can used `burp-suite-intruder` for finding sensitive directory
 * And now we found a directory is `info.php`
 * Let's see opened in our browser is directory ██████████
 * You can see this page can be view without authenticate

## Suggested Mitigation/Remediation Actions
Remove the affected file(s).
███████

The remote web server contains a PHP script that is prone to an information disclosure attack.

## Attachments
- image.png
