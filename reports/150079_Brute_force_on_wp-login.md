# Brute force on wp-login

## Report Details
- **Report ID**: 150079
- **URL**: https://hackerone.com/reports/150079
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-08T19:40:45.966Z
- **Disclosed**: 2016-08-18T01:18:08.025Z

## Reporter
- **Username**: proxynwh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: iandunn-projects

## Vulnerability Information
A common threat web developers face is a password-guessing attack known as a brute force attack. A brute-force attack is an attempt to discover a password by systematically trying every possible combination of letters, numbers, and symbols until you discover the one correct combination that works. 

This login page doesn't have any protection against password-guessing attacks (brute force attacks). It's recommended to implement some type of account lockout after a defined number of incorrect password attempts. 

Consult Web references for more information about fixing this problem.

Affected items:
/wordpress/wp-login.php 

The impact of this vulnerability?
An attacker may attempt to discover a weak password by systematically trying every possible combination of letters, numbers, and symbols until it discovers the one correct combination that works.

How to fix this vulnerability:
It's recommended to implement some type of account lockout after a defined number of incorrect password attempts.

Web references:
https://www.owasp.org/index.php/Blocking_Brute_Force_Attacks

## Attachments
No attachments
