# Incorrect HTTPS Certificate

## Report Details
- **Report ID**: 225540
- **URL**: https://hackerone.com/reports/225540
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-05-02T13:24:13.319Z
- **Disclosed**: 2017-06-16T14:11:58.462Z

## Reporter
- **Username**: numbshiva
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Weblate appears to have a public facing git repository located at git.weblate.org that utilises HTTPS when viewed in the browser. (As a side note, netcat to port 80 results in the default debian landing page).

77.78.107.252 - git.weblate.org

The site has an incorrectly configured certificate, and enforcing HSTS means users are unable to connect.

The certificate in place appears to be for avatar.cihar.com. SSLScan confirms the error presented by the browser:

<..snip..>
**SSL Certificate:**
    Version: 2
    Serial Number: -18446744073709551615
    Signature Algorithm: sha256WithRSAEncryption
    Issuer: /C=US/O=Let's Encrypt/CN=Let's Encrypt Authority X3
    Not valid before: Apr 26 21:26:00 2017 GMT
    Not valid after: Jul 25 21:26:00 2017 GMT
    Subject: /CN=avatar.cihar.com
    Public Key Algorithm: rsaEncryption

A curl request with verbose reporting gives a slightly clearer picture:

**curl -v https://git.weblate.org**
* About to connect() to git.weblate.org port 443 (#0)
*   Trying 77.78.107.252...
* connected
* Connected to git.weblate.org (77.78.107.252) port 443 (#0)
* successfully set certificate verify locations:
*   CAfile: none
  CApath: /etc/ssl/certs
* SSLv3, TLS handshake, Client hello (1):
* SSLv3, TLS handshake, Server hello (2):
* SSLv3, TLS handshake, CERT (11):
* SSLv3, TLS handshake, Server key exchange (12):
* SSLv3, TLS handshake, Server finished (14):
* SSLv3, TLS handshake, Client key exchange (16):
* SSLv3, TLS change cipher, Client hello (1):
* SSLv3, TLS handshake, Finished (20):
* SSLv3, TLS change cipher, Client hello (1):
* SSLv3, TLS handshake, Finished (20):
* SSL connection using ECDHE-RSA-AES128-GCM-SHA256
* Server certificate:
* 	 subject: CN=avatar.cihar.com
* 	 start date: 2017-04-26 21:26:00 GMT
* 	 expire date: 2017-07-25 21:26:00 GMT
* 	 subjectAltName does not match git.weblate.org
* Closing connection #0
* SSLv3, TLS alert, Client hello (1):
* SSL peer certificate or SSH remote key was not OK

curl: (51) SSL peer certificate or SSH remote key was not OK

## Attachments
No attachments
