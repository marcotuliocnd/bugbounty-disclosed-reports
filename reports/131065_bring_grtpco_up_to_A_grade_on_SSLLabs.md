# bring grtp.co up to A grade on SSLLabs

## Report Details
- **Report ID**: 131065
- **URL**: https://hackerone.com/reports/131065
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-04-15T11:45:34.151Z
- **Disclosed**: 2016-08-13T22:03:09.890Z

## Reporter
- **Username**: mmyamin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Issues at https://grtp.co/
reference for Weak SSL Ciphers:https://www.owasp.org/index.php/Testing_for_Weak_SSL/TLS_Ciphers,_Insufficient_Transport_Layer_Protection_(OTG-CRYPST-001)
Weak SSL Ciphers supported at port 443:
TLS 1.0:
 TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA (ec 256) - C
 TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA (dh 1024) - D
 TLS_RSA_WITH_3DES_EDE_CBC_SHA (rsa 4096) - C
TLSv1.2: 
TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA (ec 256) - C
TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA (dh 1024) - D
TLS_RSA_WITH_3DES_EDE_CBC_SHA (rsa 4096) - C
Evidence of Weak SSL ciphers is attached in figure 1

Weak SSH Ciphers supported at port 22:
Reference :https://www.tenable.com/plugins/index.php?view=single&id=70658
Supported CBC ciphers
aes128-cbc
3des-cbc
blowfish-cbc
cast128-cbc
aes192-cbc
aes256-cbc

Evidence related to supported CBC ciphers is attached in figure 2

## Attachments
- figure_2_weak_ssh_ciphers.png
- figure_1_weak_ssl_ciphers.png
