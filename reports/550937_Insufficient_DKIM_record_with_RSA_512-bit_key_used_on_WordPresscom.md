# Insufficient DKIM record with RSA 512-bit key used on WordPress.com

## Report Details
- **Report ID**: 550937
- **URL**: https://hackerone.com/reports/550937
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-04-29T19:23:13.697Z
- **Disclosed**: 2019-05-30T13:45:35.608Z

## Reporter
- **Username**: vavkamil
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
### What is DomainKeys Identified Mail (DKIM) ?
DKIM allows the receiver to check that an email claimed to have come from a specific domain was indeed authorized by the owner of that domain. It achieves this by affixing a digital signature, linked to a domain name, to each outgoing email message. The recipient system can verify this by looking up the sender's public key published in the DNS.

### Length of the Key
With rapidly increasing processing power of computers, RSA keys with a 512-bit length, previously considered to be secure, can be cracked in a short period of time. Today, a minimum of 1024 bit RSA should be used. Organizations like the American National Institute of Standards and Technology (NIST) go further, and recommend aminimum of 2048 bits.

### Short key vulnerability
According to RFC 6376 the receiving party must be able to validate signatures with keys ranging from 512 bits to 2048 bits, thus usage of keys shorter than 512 bits might be incompatible and shall be avoided. The RFC 6376 also states that signers must use keys of at least 1024 bits for long-lived keys, though long-livingness is not specified there.

### CWE-326: Inadequate Encryption Strength
I was scanning WordPress.com DNS DKIM records using own wordlist of DKIM selectors. I was able to find one selector "my1" which is using RSA 512 bits key.

```
vavkamil@desktop:~$ dig txt my1._domainkey.wordpress.com +short
"p=MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAMXyekdYBZjcTskG1hwEji+J17DI9hPif0RsNF3aDPorKUnOLRN/bxCZ82BRpwXhgmbJ91KNe1fQMdZRs3iOdFcCAwEAAQ=="
```
More details:
```
# fqdn: my1._domainkey.wordpress.com
# txt:  p=MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAMXyekdYBZjcTskG1hwEji+J17DI9hPif0RsNF3aDPorKUnOLRN/bxCZ82BRpwXhgmbJ91KNe1fQMdZRs3iOdFcCAwEAAQ==
# key:  MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAMXyekdYBZjcTskG1hwEji+J17DI9hPif0RsNF3aDPorKUnOLRN/bxCZ82BRpwXhgmbJ91KNe1fQMdZRs3iOdFcCAwEAAQ==
# size:  512 bits
# n:    10367334950201306539131289202809840614738220453757190856643449770342237105356400464470413674101052983691492083310061606610679073552649560621665862279918679
# e:    65537
# fp:   1651db71c5ae43c40473dcea2af993ba50c6291c  512 wordpress.com my1 PROD

-----BEGIN PUBLIC KEY-----
MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAMXyekdYBZjcTskG1hwEji+J17DI9hPi
f0RsNF3aDPorKUnOLRN/bxCZ82BRpwXhgmbJ91KNe1fQMdZRs3iOdFcCAwEAAQ==
-----END PUBLIC KEY-----
```

Exploitation
=====================
A 512-bit RSA key is insecure, as was proved in 1998.  Nowadays a 512-bit integers can be factored in only a few hours, for less than $100 of compute time in a public cloud environment: https://github.com/eniac/faas
An attacker therefore might be able to obtain private key for said DKIM record and sign any emails for the associated domain (WordPress.com). This can be used to spoof e-mails for example in targeted attacks (phishing/spear-phishing, ...).

Historical reports
--------------------------------------
I wasn't able to find any related bug bounty reports, but the same problem was reported to Google back in 2012: https://www.wired.com/2012/10/dkim-vulnerability-widespread

## Impact

Attacker can obtain 512-bit RSA private key from DKIM record with selector "my1" (my1._domainkey.wordpress.com) and use it to sign spoofed e-mails sent from @wordpress.com. This can lead to more sufficient phishing campaigns against Automattic customers.

## Attachments
- my1._domainkey.wordpress.com.txt
