# Slack DTLS uses a private key that is in the public domain, which may lead to SRTP stream hijack

## Report Details
- **Report ID**: 531032
- **URL**: https://hackerone.com/reports/531032
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-04-08T09:20:55.916Z
- **Disclosed**: 2020-03-12T00:17:02.105Z

## Reporter
- **Username**: sandrogauci
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
- Affects: Janus DTLS certificate

### Description

The Janus server in use by Slack is configured using a certificate and private key that were previously distributed by default. This certificate is used to authenticate the DTLS _connection_ which is later used to exchange keys for the SRTP stream. As a result, the confidentiality of the WebRTC call over Slack cannot be ensured.


### How to reproduce the issue

1. Start Wireshark and set a display filter for stun
2. In the web browser, open `about:webrtc-internals`
3. Start a call on Slack
4. Observe the packets containing the string _rainmaker_ which would be part of the DTLS certificate
5. Notice that the `SetRemoteDescription` fingerprint in the `about:webrtc-internals` page is `C5:5F:DA:7D:84:47:B1:BF:6B:55:16:62:48:31:3E:D3:F1:7B:25:89:92:4A:4B:4D:4D:D9:D5:AF:EA:D8:15:44`

The old certificate can be obtained from the following commit where it was previously removed:

https://github.com/meetecho/janus-gateway/commit/6f98f2dde644b3ead4a162c241dff9da1587ec13

The certificate's SHA256 checksum can be calculated using the OpenSSL command line tool as follows:

```
openssl x509 -noout -fingerprint -sha256 -inform pem -in janus-cert1.crt 
SHA256 Fingerprint=C5:5F:DA:7D:84:47:B1:BF:6B:55:16:62:48:31:3E:D3:F1:7B:25:89:92:4A:4B:4D:4D:D9:D5:AF:EA:D8:15:44
```

Attachments:

- `dump-stun.pcapng`: contains the data stream containing the TURN tunnelled DTLS exchange and SRTP stream that follows
- `janus-cert1.crt` and `janus-cert1.key` are the certificate and key in use by Slack
- `2019-04-07_16-06-wireshark.png` shows the certificate in the Wireshark dump
- `2019-04-07_16-13-fingerprint.png` shows the SHA256 fingerprint which matches the public certificate and corresponding private key

An attacker would probably need to take the following steps to exploit this issue in the case of Slack:

1. Start a man-in-the-middle attack using any known method (ARP cache poisoning, DNS cache poisoning, static routes on compromised network router etc)
2. Actively hijack the Slack TURN servers between the victim and the Internet
3. Wait for victim to make a Slack call
4. Handle STUN packets from victim to attacker-controlled TURN server; allow authentication with any password
5. Start DTLS exchange
6. When DTLS certificate is required, present victim with the Janus default certificate
7. The attacker does __NOT__ verify the victim's DTLS certificate
8. The SRTP Master Key is set over this DTLS connection
9. Attacker can now handle the SRTP stream between the victim and attacker

### Solutions and recommendations

It is recommended to generate a new certificate and private key.

## Impact

Attackers positioned as man-in-the-middle may hijack the DTLS connection and set their own SRTP keys, handling the SRTP stream instead of Slack. This is still research in progress but it does not appear that attackers can perform a two-way MITM attack due to the mutual authentication required by the DTLS exchange. Therefore, it seems that this vulnerability can only be abused to hijack the SRTP stream between the WebRTC client and Slack but not the other way round.

## Attachments
- janus-cert1.key
- janus-cert1.crt
- dump-stun.pcapng
- 2019-04-07_16-13-fingerprint.png
- 2019-04-07_16-06-wireshark.png
