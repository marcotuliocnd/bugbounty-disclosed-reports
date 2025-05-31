# Impact of Using the PHP Function "phpinfo()" on System Security - PHP info page disclosure

## Report Details
- **Report ID**: 1822665
- **URL**: https://hackerone.com/reports/1822665
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-01-04T22:44:12.469Z
- **Disclosed**: 2023-05-18T21:12:19.896Z

## Reporter
- **Username**: carpc
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: us-department-of-state

## Vulnerability Information
## Summary:
phpinfo() is a debug functionality that prints out detailed information on both the system and the PHP configuration.
This function can reveal sensitive information such as the exact PHP version, operating system and its version, internal IP addresses, server environment variables, and loaded PHP extensions and their configurations. An attacker can use this information to research known vulnerabilities for the system and potentially exploit other vulnerabilities.

## Steps To Reproduce:

  1. Access the address https://rewardsforjustice.net/phpinfo.php 


##Remediation Guidance
To remediate this issue, you should remove the phpinfo() function from your code, or ensure that it is only accessible to trusted individuals. Additionally, you should ensure that your server environment variables are not accessible to unauthorized users.

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * "Secure Configuration Guide for PHP" by the National Institute of Standards and Technology (NIST): https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-42.pdf
* "PHP Security Best Practices" by the Open Web Application Security Project (OWASP): https://www.owasp.org/index.php/PHP_Security_Best_Practices
* "PHP Configuration and Hardening" by the SANS Institute: https://www.sans.edu/security-resources/policies/general/docs/php-configuration-hardening

## Impact

This information can help an attacker gain more information on the system. After gaining detailed information, the attacker can research known vulnerabilities for that system under review. The attacker can also use this information during the exploitation of other vulnerabilities.

## Attachments
No attachments
