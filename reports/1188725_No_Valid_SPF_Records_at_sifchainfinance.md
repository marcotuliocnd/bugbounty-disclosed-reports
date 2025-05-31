# No Valid SPF Records at sifchain.finance

## Report Details
- **Report ID**: 1188725
- **URL**: https://hackerone.com/reports/1188725
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2021-05-08T00:31:04.391Z
- **Disclosed**: 2021-12-09T17:51:42.789Z

## Reporter
- **Username**: dantt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
Hello,

There is any issue No valid SPF Records
Desciprition :
There is a email spoofing vulnerability.Email spoofing is the forgery of an email header so that the message appears to have originated from someone or somewhere other than the actual source. Email spoofing is a tactic used in phishing and spam campaigns because people are more likely to open an email when they think it has been sent by a legitimate source. The goal of email spoofing is to get recipients to open, and possibly even respond to, a solicitation.
I found :
SPF record lookup and validation for: sifchain.finance
SPF records are published in DNS as TXT records.

Feel free to use this site to check ; https://www.kitterman.com/spf/validate.html
{F1293275}

Remediation :
Replace ~all with -all to prevent fake email.

Refferences :
https://www.digitalocean.com/community/tutorials/how-to-use-an-spf-record-to-prevent-spoofing-improve-e-mail-reliability

PoC
{F1293276}

## Impact

An attacker would send a Fake email.
In gmail it will be marked but if its ".edu" it will not marked and goes directly inbox
in gmail goes directly inbox too with question mark.

## Attachments
- sifchain4.png
- sifchain5.png
