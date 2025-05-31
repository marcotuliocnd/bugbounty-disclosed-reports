# The login of Hotor Not is Vulnerable to bruteforce.

## Report Details
- **Report ID**: 744692
- **URL**: https://hackerone.com/reports/744692
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-11-22T16:36:11.608Z
- **Disclosed**: 2020-01-23T18:16:56.069Z

## Reporter
- **Username**: oo7hacker3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bumble

## Vulnerability Information
I was able to validate that The Login of HotorNot is Vulnerable to BruteForcing .

Steps to reproduce:
1. https://hotornot.com/signin
2.Use Burp intruder attack for BruteForcing 
3.Send as many requests you want.

Fix:
Proper mitigation of BruteForcing should be done using Ratelimitng etc implementation.

## Impact

If attacker successfully Bruteforces the he/she might takeover it.Which might lead in users Privacy Violation

## Attachments
No attachments
