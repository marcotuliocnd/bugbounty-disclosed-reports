# No Valid SPF Records.

## Report Details
- **Report ID**: 629087
- **URL**: https://hackerone.com/reports/629087
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-06-25T12:18:06.480Z
- **Disclosed**: 2019-07-18T15:27:29.951Z

## Reporter
- **Username**: danangtriatmaja
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: chainlink

## Vulnerability Information
Hiii,

There is any issue No valid SPF Records

Desciprition :

There is a email spoofing vulnerability.Email spoofing is the forgery of an email header so that the message appears to have originated from someone or somewhere other than the actual source. Email spoofing is a tactic used in phishing and spam campaigns because people are more likely to open an email when they think it has been sent by a legitimate source. The goal of email spoofing is to get recipients to open, and possibly even respond to, a solicitation.

I found : 

SPF record lookup and validation for: chain.link
SPF records are published in DNS as TXT records.

The TXT records found for your domain are:
google-site-verification=a4ghJBW7o-Ss_TB82G2VqvQKq_8Km3UfqcuTgfc8lSY
v=spf1 include:_spf.google.com ~all

Checking to see if there is a valid SPF record.

Found v=spf1 record for chain.link:
v=spf1 include:_spf.google.com ~all

evaluating...
SPF record passed validation test with pySPF (Python SPF library)!

Use the back button on your browser to return to the SPF checking tool without clearing the form.

Remediation :

Replace ~all with -all to prevent fake email.

Refferences :

https://www.digitalocean.com/community/tutorials/how-to-use-an-spf-record-to-prevent-spoofing-improve-e-mail-reliability

## Impact

An attacker would send a Fake email. The results can be more dangerous.

## Attachments
- chain.png
