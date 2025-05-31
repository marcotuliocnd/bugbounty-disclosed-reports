# Email Spoofing bug

## Report Details
- **Report ID**: 1176090
- **URL**: https://hackerone.com/reports/1176090
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2021-04-27T01:54:30.923Z
- **Disclosed**: 2021-12-09T17:43:48.396Z

## Reporter
- **Username**: ridoykhan0x1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
Hi team,

An SPF/DMARC record is a type of Domain Name Service (DNS) record that identifies which mail servers are permitted to send email on behalf of your domain. The purpose of an SPF/DMARC record is to prevent spammers from sending messages on the behalf of your organization.

Remediation: Create a SPF record. And configure the DMARC policy so that only authorized and allowed mail server could send the mails on the behalf of the organization.

Reference links: Below are the links which will help you to understand more about this issue including the remediation
https://hackerone.com/reports/575
https://hackerone.com/reports/182467
https://hackerone.com/reports/182467
https://hackerone.com/reports/731878

## Impact

Impact: The impact is, attacker can send the mail on the behalf of your organization and ask any kind of password or personal sensitive information from the victim.

## Attachments
- IMG_20210427_074809.jpg
- IMG_20210427_074927.jpg
- IMG_20210427_074312.jpg
- IMG_20210427_074246.jpg
