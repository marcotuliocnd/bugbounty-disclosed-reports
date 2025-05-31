# There is any issue No valid SPF Records

## Report Details
- **Report ID**: 864696
- **URL**: https://hackerone.com/reports/864696
- **State**: Closed
- **Severity**: none
- **Submitted**: 2020-05-02T10:55:15.569Z
- **Disclosed**: 2020-07-24T00:36:14.829Z

## Reporter
- **Username**: blackviper21
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
There is a email spoofing vulnerability.Email spoofing is the forgery of an email header so that the message appears to have originated from someone or somewhere other than the actual source. Email spoofing is a tactic used in phishing and spam campaigns because people are more likely to open an email when they think it has been sent by a legitimate source. The goal of email spoofing is to get recipients to open, and possibly even respond to, a solicitation.

I found :

SPF record lookup and validation for: Kubernetes.io

SPF records are published in DNS as TXT records.

The TXT records found for your domain are:
v=spf1 include:_spf.google.com ~all
google-site-verification=oPORCoq9XU6CmaR7G_bV00CLmEz-wLGOL7SXpeEuTt8

Checking to see if there is a valid SPF record.

Found v=spf1 record for Kubernetes.io:
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
- kubernetes.png
- spf_vulneribility.mp4
