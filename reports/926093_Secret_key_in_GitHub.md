# Secret_key in GitHub

## Report Details
- **Report ID**: 926093
- **URL**: https://hackerone.com/reports/926093
- **State**: Closed
- **Severity**: none
- **Submitted**: 2020-07-17T10:41:23.798Z
- **Disclosed**: 2020-07-18T09:28:51.362Z

## Reporter
- **Username**: fr0gz0x
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
hello 
I have found secret_key in GitHub is public and noticed something this key have comment # Make this unique, and don't share it with anybody. and it's public in GitHub also I noticed this file has coding to do the payment.db I think information like this must be private 

SECRET_KEY = "qov6(*cp%)b*ot+8c%#4@4or(t@_$y5#d8k9u1^+pknz%lms0x"
Link : https://github.com/WeblateOrg/website/blob/bc65d95a80d90ed95a8e59d0fa5dc14d7c060b3a/weblate_web/settings.py

## Impact

i don't know what attacker can do but i know this info must be private

## Attachments
- Screenshot_from_2020-07-17_12-34-12.png
- Screenshot_from_2020-07-17_12-33-47.png
