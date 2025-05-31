# No BruteForce Protection

## Report Details
- **Report ID**: 223337
- **URL**: https://hackerone.com/reports/223337
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-24T09:26:18.124Z
- **Disclosed**: 2017-05-17T18:04:05.577Z

## Reporter
- **Username**: jaypatel
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
A common threat web developers face is a password-guessing attack known as a brute force attack. A brute-force attack is an attempt to discover a password by systematically trying every possible combination of letters, numbers, and symbols until you discover the one correct combination that works.

hosted.weblate.org/accounts/login/ 

This login page doesn't have any protection against password-guessing attacks (brute force attacks). It's recommended to implement some type of account lockout after a defined number of incorrect password attempts. Consult Web references for more information about fixing this problem.

**The impact of this vulnerability:**

An attacker may attempt to discover a weak password by systematically trying every possible combination of letters, numbers, and symbols until it discovers the one correct combination that works.

**How to fix this vulnerability:**

It's recommended to implement some type of account lockout after a defined number of incorrect password attempts.



## Attachments
No attachments
