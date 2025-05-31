# PHP info page disclosure

## Report Details
- **Report ID**: 1050912
- **URL**: https://hackerone.com/reports/1050912
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-12-04T22:56:49.496Z
- **Disclosed**: 2021-01-12T21:36:14.453Z

## Reporter
- **Username**: ba56adcb299ff13a87475bf
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
##Summary:

phpinfo() is a debug functionality that prints out detailed information on both the system and the PHP configuration.

##Step-by-step Reproduction Instructions

1.Go to

 https://███████phpinfo

## Impact

An attacker can obtain information such as:
•Exact PHP version.
•Exact OS and its version.
•Details of the PHP configuration.
•Loaded PHP extensions and their configurations.
This information can help an attacker gain more information on the system. After gaining detailed information, the attacker can research known vulnerabilities for that system under review. The attacker can also use this information during the exploitation of other vulnerabilities

## Attachments
No attachments
