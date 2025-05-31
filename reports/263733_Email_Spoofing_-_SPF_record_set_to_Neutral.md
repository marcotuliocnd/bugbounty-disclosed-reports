# Email Spoofing - SPF record set to Neutral

## Report Details
- **Report ID**: 263733
- **URL**: https://hackerone.com/reports/263733
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-08-27T07:02:02.240Z
- **Disclosed**: 2017-09-06T21:59:21.437Z

## Reporter
- **Username**: ramakanthk35
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_bbp

## Vulnerability Information
Hi, 

Introduction:
There is a email spoofing vulnerability.Email spoofing is the forgery of an email header so that the message appears to have originated from someone or somewhere other than the actual source. Email spoofing is a tactic used in phishing and spam campaigns because people are more likely to open an email when they think it has been sent by a legitimate source. The goal of email spoofing is to get recipients to open, and possibly even respond to, a solicitation.

Steps to Reproduce:
1. goto http://www.kitterman.com/spf/validate.html
2. Enter domain name: 18f.com and click spf record if any under "Does my domain already have an SPF record? What is it? Is it valid?"
3. The SPF record  is observed as below
"Found v=spf1 record for 18f.gov: 
v=spf1 include:spf.mandrillapp.com ?all"

which is set to neutral,Neutral-The SPF record specifies explicitly that nothing can be said about validity.


 

## Attachments
No attachments
