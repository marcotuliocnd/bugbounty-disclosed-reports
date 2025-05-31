# SSRF via webhook

## Report Details
- **Report ID**: 243277
- **URL**: https://hackerone.com/reports/243277
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-06-26T16:39:25.035Z
- **Disclosed**: 2017-07-18T18:20:49.659Z

## Reporter
- **Username**: cablej
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mixmax

## Vulnerability Information
Hi,

There exists an SSRF vulnerability with the account webhook feature, allowing an attacker to verify the existence of the EC2 metadata url and enumerate URL's.

POC:

1. Create a webhook at https://app.mixmax.com/dashboard/settings/rules with url `http://169.254.169.254/latest/meta-data/`.
2. Trigger this webhook by sending/receiving an email. Wait a few hours.
3. Note that an email is not sent saying the webhook failed. I tried for other internal urls such as 'http://localhost', but they sent a failure email, indicating that `http://169.254.169.254/latest/meta-data/` is open to the webhook.
4. In addition to verifying that this endpoint exists, an attacker could enumerate endpoints on this domain. For example, an attacker could enumerate MAC addresses at `http://169.254.169.254/latest/meta-data/network/interfaces/macs/xx:xx:...`.

Suggested fix:

Blacklist the AWS metadata url and any other sensitive internal urls.

Thanks.

## Attachments
No attachments
