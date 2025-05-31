# PHP info page disclosure

## Report Details
- **Report ID**: 1118898
- **URL**: https://hackerone.com/reports/1118898
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-03-06T17:33:17.325Z
- **Disclosed**: 2021-04-14T15:23:52.164Z

## Reporter
- **Username**: valluvarsploit_h1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_vdp

## Vulnerability Information
phpinfo() is a debug functionality that prints out detailed information on both the system and the PHP configuration.

Step to reproduce:
Go here: https://mysmartplans.gsa.gov/phpinfo.php


An attacker can obtain information such as:
Exact PHP version.
Exact OS and its version.
Details of the PHP configuration.
Internal IP addresses.
Server environment variables.
Loaded PHP extensions and their configurations and etc.

## Impact

This information can help an attacker gain more information on the system. After gaining detailed information, the attacker can research known vulnerabilities for that system under review. The attacker can also use this information during the exploitation of other vulnerabilities.

## Attachments
- phpinfo_disclosure.png
