# Email Spoofing

## Report Details
- **Report ID**: 793532
- **URL**: https://hackerone.com/reports/793532
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-02-11T12:14:28.603Z
- **Disclosed**: 2020-02-20T09:17:23.166Z

## Reporter
- **Username**: mayankraheja069
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
An SPF/DMARC record is a type of Domain Name Service (DNS) record that identifies which mail servers are permitted to send email on behalf of your domain. The purpose of an SPF/DMARC record is to prevent spammers from sending messages on the behalf of your organization.

Remediation: Create a SPF record. And configure the DMARC policy so that only authorized and allowed mail server could send the mails on the behalf of the organization.

## Impact

Impact: The impact is, attacker can send the mail on the behalf of your organization and ask any kind of password or personal sensitive information from the victim.

## Attachments
- NextcloudSPF.png
- NextcloudDMARC.png
