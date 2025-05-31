# Testnet address being sent in cleartext as http://rinkeby.chain.link/ is missing SSL certificate

## Report Details
- **Report ID**: 576288
- **URL**: https://hackerone.com/reports/576288
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-05-10T10:56:33.963Z
- **Disclosed**: 2019-07-17T20:49:08.716Z

## Reporter
- **Username**: jaisharma
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: chainlink

## Vulnerability Information
**Summary:** SSL certificate missing for page: http://rinkeby.chain.link/ which is letting an attacker to sniff sensitive information, in this case, user's testnet address as it is being transmitted unencrypted in clear text

**Description:** http://rinkeby.chain.link/ missing SSL encryption, data sent over this address is leaking information to any malicious user and be utilized in any malicious manner, also redirection to correct HTTPS link is missing which is making more vulnerable to sniffing or MiMT attacks.

## Steps To Reproduce:

  1. Go to: http://rinkeby.chain.link/ and submit your personal testnet address
  1. Setup Wireshark and you will get the User's testnet address

## Supporting Material/References:

  * Please see the attached POC doc

## Impact

Pages missing SSL certifications send data in clear text, if the data include sensitive information that can be exposed to anyone who is using any traffic sniffer over the local or wireless network (take Wireshark application as an example)

## Attachments
- chainlink1.PNG
