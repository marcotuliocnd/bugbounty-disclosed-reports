# HTTP - Basic Authentication on https://www.stellar.org/wp-login.php

## Report Details
- **Report ID**: 239479
- **URL**: https://hackerone.com/reports/239479
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-06-13T06:25:16.168Z
- **Disclosed**: 2017-06-13T14:00:12.958Z

## Reporter
- **Username**: mrnull1337
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stellar

## Vulnerability Information
Greetings, noticed https://www.stellar.org/wp-login.php using basic authentication.

#PoC:
YWRtaW46YWRtaW4= is base64 encode of admin:admin
#Impact:

Vulnerable to client side attacks.
Vulnerable to MITM attack.
Vulenrable to Eavesdropping attack.
Vulnerable to Brute force attacks.

#Fix:
HTTP-Basic Authentication should be changed for HTTP-Digest Authentication.

Let me know if any further info is required.

Regards,
Mr.R3boot.

## Attachments
- 1.png
- 2.png
