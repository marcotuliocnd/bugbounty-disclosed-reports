# No valid SPF record found

## Report Details
- **Report ID**: 775531
- **URL**: https://hackerone.com/reports/775531
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-01-15T13:48:52.693Z
- **Disclosed**: 2020-02-04T01:59:12.232Z

## Reporter
- **Username**: aravindn
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Desciprition :

There is a email spoofing vulnerability.Email spoofing is the forgery of an email header so that the message appears to have originated from someone or somewhere other than the actual source. Email spoofing is a tactic used in phishing and spam campaigns because people are more likely to open an email when they think it has been sent by a legitimate source. The goal of email spoofing is to get recipients to open, and possibly even respond to, a solicitation.

I found :

SPF record lookup and validation for: prow.k8s.io
SPF records are published in DNS as TXT records.

The TXT records found for your domain are:


Checking to see if there is a valid SPF record.

No valid SPF record found of either type TXT or type SPF.

Remediation :

Replace ~all with -all to prevent fake email.

## Impact

An attacker would send a Fake email. The results can be more dangerous. Email spoofing is a tactic used in phishing and spam campaigns because people are more likely to open an email when they think it has been sent by a legitimate source. The goal of email spoofing is to get recipients to open, and possibly even respond to, a solicitation

## Attachments
- prow.png
