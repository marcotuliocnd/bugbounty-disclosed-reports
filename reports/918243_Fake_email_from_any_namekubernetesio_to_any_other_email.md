# Fake email from <any_name>@kubernetes.io to any other email

## Report Details
- **Report ID**: 918243
- **URL**: https://hackerone.com/reports/918243
- **State**: Closed
- **Severity**: none
- **Submitted**: 2020-07-07T19:39:48.612Z
- **Disclosed**: 2020-07-24T00:42:37.366Z

## Reporter
- **Username**: lamscun
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Hi,
I just found an issue No Valid SPF Records in your mail server  @kubernetes.io

Desciprition :

There is a email spoofing vulnerability.Email spoofing is the forgery of an email header so that the message appears to have originated from someone or somewhere other than the actual source. Email spoofing is a tactic used in phishing and spam campaigns because people are more likely to open an email when they think it has been sent by a legitimate source. The goal of email spoofing is to get recipients to open, and possibly even respond to, a solicitation.

{F898620}

## Impact

An attacker would send a Fake email (from  <any_name>@kubernetes.io to any other email). The results can be more dangerous.

## Attachments
- fake_email.png
