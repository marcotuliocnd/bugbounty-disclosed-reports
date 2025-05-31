# Yelp.com is vulnerable to SWEET32 attack

## Report Details
- **Report ID**: 199436
- **URL**: https://hackerone.com/reports/199436
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-01-18T17:43:32.478Z
- **Disclosed**: 2017-11-09T21:47:52.672Z

## Reporter
- **Username**: pkkothawade
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
Researchers have found new attack against 3DES-CBC cipher in TLS,that they can decrypt customer data using a method called SWEET32 Birthday Attack.

This Vulnerability has got CVE-2016-2183 and has cvss score 5.0

This vulnerability can be found manually by simply using nmap script

nmap -Pn -p --script ssl-enum-ciphers ip

Mitigation for SWEET32 attack

->Prefer minimum 128-bit cipher suites

->Limit the length of TLS sessions with a 64-bit cipher, which could be done with TLS renegotiation or closing and starting a new connection

-> Disable cipher suites using 3DES
Reference link: https://sweet32.info/

## Attachments
- Sweet32_Yelp.JPG
