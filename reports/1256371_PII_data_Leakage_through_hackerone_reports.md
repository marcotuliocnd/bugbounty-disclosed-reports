# PII data Leakage through hackerone reports 

## Report Details
- **Report ID**: 1256371
- **URL**: https://hackerone.com/reports/1256371
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-07-09T20:25:00.018Z
- **Disclosed**: 2021-08-09T20:03:00.042Z

## Reporter
- **Username**: iamr0000t
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
##Summary:

I found PII data leakage through the HackerOne report. I found a link in one of the disclosed report that allow me to get the address and phone numbers of security researchers. Here I got the address and phone number of ████ (███)


Vulnerability Name: PII data Leakage through

##Steps to reproduce:
—>Just visit ███
—>You will find a link swag link there.  (Refer: Screenshot 1)
—>Now visit the swag link ie. ██████████ and add a parameter there ██████████ 
—> link becomes : ████████
—>You will get the PII of researchers.  (Refer: Screenshot 2)

##Fix
1.)████████ should be informed that the data might have leaked. 
2.)Link should be redacted.
3.) When hackerone provides swag to researchers they should mention to keep the link strictly confidential , 
same information should also be provided to the programs on HackerOne , that offer swag.

## Impact

An attacker can get sensitive information about the other researchers like their addresses and phone number.

## Attachments
No attachments
