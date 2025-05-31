# Multiple cryptographic vulnerabilities in login page on ███████

## Report Details
- **Report ID**: 223936
- **URL**: https://hackerone.com/reports/223936
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-26T01:01:49.535Z
- **Disclosed**: 2019-12-02T18:53:22.652Z

## Reporter
- **Username**: tcpiplab
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
I realize that this report's title may not make sense yet. In one sentence: users logging in to the [███████ Server REST API Login page](http://██████/server/rest/login) can have their passwords stolen by an attacker on the same LAN or WiFi as the victim trying to log in.

**Description:**
To save the reader any confusion, I'll point out that this is an unusual case where, instead of using HTTPS for password confidentiality in transit, the server sends RSA encryption scripts to the browser. The browser then encrypts the password before sending the login request to the server. Using ARP poisoning  I was able to Man-in-the-Middle (MitM) traffic between a victim and the login server. This enabled me to inject my public key into the login page, capture the encrypted password and decrypt it (using my private key), revealing the victim's plaintext password.

## Impact

User accounts on the [████████ Server REST API server](http://███████/server/rest/login) could be compromised.

## Step-by-step Reproduction Instructions
Because this report is so long, I'm only putting in this summarized list of steps. But if you want a full step-by-step with screenshots, the Ettercap filter, my Python decryption script and everything, I've already written it up. Just ask. 

1. The attacker must be on the same Layer 2 network segment (LAN, or WiFi) as the victim's computer.
1. The attacker runs Ettercap, specifying the IP addresses of:
   * The gateway router
   * The victim's computer
1. Using Ettercap, the attacker conducts an ARP Poisoning attack against the victim's computer and that of the gateway router, thereby acting as a proxy for traffic between those two devices.
1. When the victim's browser sends a `GET` for `http://███/server/rest/login`, the attacker:
   1. intercepts the server's response,
   1. modifies the HTML form, replacing the server's public key modulus string with the attacker's public key modulus string.
1. The victim enters `username` and `password` values in the modified HTML form and clicks the `Login` button. The `RSA.js` (and other scripts) run in the victim's browser as usual, but the resulting ciphertext is the user's password encrypted for the public key of the attacker. The victim's browser sends these values in a `POST` to `/server/rest/login`, but because of the ARP Poisoning attack, the `POST` is sent to the attacker's computer.
1. The attacker, using OpenSSL and their own RSA private key, decrypts the encrypted password, thus recovering the plaintext password.
1. Optional: The attacker re-encrypts the victim's plaintext password using the login page's original public key.
1. Optional: The attacker places the now encrypted password value into a new `POST` to `/server/rest/login` and sends the request to the gateway router, thereby allowing the victim to authenticate to the server.
1. At this point the attack is successful. Note: the attacker still needs to tell Ettercap to stop the ARP Poisoning attack, causing it to send the ARP Correction packet, thereby restoring normal connectivity between the victim and the gateway router.
## Product, Version, and Configuration (If applicable)

## Suggested Mitigation/Remediation Actions

1. Require HTTPS for sending username/password to the server.
   * This would solve the whole problem
1. At the risk of sounding pedantic, client-side encryption via Javascript is not an effective security control. But I do realize that there may be use-case requirements for your application that I don't know about.   
1. If you do have some reason why you *must* continue using client-side encryption, please know that the `RSA.js` script is using a vulnerable padding standard (PKCS#1v1.5). Unfortunately, the developer's [new RSA.js script](http://www.ohdave.com/rsa/RSA.js) is still using PKCS#1v1.5 padding which is vulnerable to a chosen ciphertext attack. The [Cryptosense](https://cryptosense.com/why-pkcs1v1-5-encryption-should-be-put-out-of-our-misery/) blog explains in detail. FYI I did not attempt to exploit this padding vulnerability.

## Attachments
No attachments
