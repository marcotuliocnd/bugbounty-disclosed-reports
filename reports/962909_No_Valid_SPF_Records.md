# No Valid SPF Records

## Report Details
- **Report ID**: 962909
- **URL**: https://hackerone.com/reports/962909
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-08-20T03:33:31.857Z
- **Disclosed**: 2020-08-24T14:38:16.001Z

## Reporter
- **Username**: harshita174
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: dropcontact

## Vulnerability Information
Hiii,

There is any issue No valid SPF Records

Desciprition :

There is a email spoofing vulnerability.Email spoofing is the forgery of an email header so that the message appears to have originated from someone or somewhere other than the actual source. Email spoofing is a tactic used in phishing and spam campaigns because people are more likely to open an email when they think it has been sent by a legitimate source. The goal of email spoofing is to get recipients to open, and possibly even respond to, a solicitation.

I found :
SPF record lookup and validation for: dropcontact.io

SPF records are published in DNS as TXT records.

The TXT records found for your domain are:
ahrefs-site-verification_da4576e20728e7b119ad73ce3c8a38c90e3f2165a1f22a7f95659ee3d148c641
google-site-verification=4pf1hRw41bB09V-_Bh2qIUD1XvHCsj5nRwc_dc996GY
v=spf1 include:_spf.google.com include:mailgun.org include:helpscoutemail.com ~all
google-site-verification=6aqn1g7FwGyypU0Q58edBt7P2JW7CurEQ7OKXOL6rIs
google-site-verification=ebjIUy-P4WZpwjBrSqOx2kcpTgUe-qjbBfVBrXE6LYQ

Checking to see if there is a valid SPF record.

Found v=spf1 record for dropcontact.io:
v=spf1 include:_spf.google.com include:mailgun.org include:helpscoutemail.com ~all

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
- Screenshot_(47).png
- Screenshot_(49).png
- Screenshot_(48).png
