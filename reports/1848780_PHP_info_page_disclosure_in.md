# PHP info page disclosure in ██████████

## Report Details
- **Report ID**: 1848780
- **URL**: https://hackerone.com/reports/1848780
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-01-27T14:42:49.971Z
- **Disclosed**: 2024-08-30T23:12:32.221Z

## Reporter
- **Username**: 0xmekky
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
[phpinfo() is a debug functionality that prints out detailed information on both the system and the PHP configuration.]

## Steps To Reproduce:
Step to reproduce:

  1. [Go here: ████]
An attacker can obtain information such as:
Exact PHP version.
Exact OS and its version.
Details of the PHP configuration.
Internal IP addresses.
Server environment variables.
Loaded PHP extensions and their configurations and etc.

## Supporting Material/References:


  *████
  ████████

## Impact

This information can help an attacker gain more information on the system. After gaining detailed information, the attacker can research known vulnerabilities for that system under review. The attacker can also use this information during the exploitation of other vulnerabilities.

## Attachments
- php_info_2.PNG
- php_info_3.PNG
- php_info1.PNG
