# No DMARC record at cordacon.com

## Report Details
- **Report ID**: 1125143
- **URL**: https://hackerone.com/reports/1125143
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-03-13T19:47:01.674Z
- **Disclosed**: 2021-08-18T08:27:15.217Z

## Reporter
- **Username**: aliyugombe
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: r3

## Vulnerability Information
I am happy to receive your invitation, and i will try my best to keep R3 secured.

As this is my first report and can be considered as low severity and some companies even considered it as N/A, but as I see in your policy its not mention as out of scope.

one of your domain has no DMARC record, which can give attacker access to your domain to send phishing emails to every one with the sender eg `admin@cordacon.com`


## Steps To Reproduce:
1. Visit https://mxtoolbox.com
2. Type the domain cordacon.com
3. click on Ok your will see no DMARC record

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

Attacker access to your domain to send phishing emails to every one with the sender eg `admin@cordacon.com`
Or black mail your domain because sometimes the email will be in spam folder, any one receive such email will think that its from you and you're scammers.

## Attachments
- r3_no_dmarc_poc.png
