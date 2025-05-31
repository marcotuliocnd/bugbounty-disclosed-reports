# Traffic amplification attack via discovery protocol

## Report Details
- **Report ID**: 502207
- **URL**: https://hackerone.com/reports/502207
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-02-26T16:59:53.806Z
- **Disclosed**: 2023-03-13T16:27:00.039Z

## Reporter
- **Username**: luk-matczak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rootstocklabs

## Vulnerability Information
**Summary:** It’s possible to use UDP discovery protocol to amplify DDoS attacks. Ping-pong mechanism that was intended to protect against it isn’t properly implemented. An attacker can successfully finish it, even with spoofed IP. Then he can send "FindNodePeerMessage" with spoofed IP in UDP packet and RSKJ node will send much larger "NeighborsPeerMessage" to third-party victim. This way an attacker can easily perform DDoS attack both on RSKJ node and third-party server.

**Description:** An attacker can send "PingPeerMessage" with his correct IP as source IP. It will cause RSKJ node to send "PingPeerMessage" with random "check" value to the attacker. Then he can reply with "PongPeerMessage" containing correct "check" but with spoofed IP. RSKJ doesn't check if pong message comes from the same IP as ping message and this way spoofed IP is added to establishedConnections. Then attacker can send "FindNodePeerMessage" with spoofed IP to perform traffic amplification attack. This vulnerability can be resolved by checking if source IP in pong message is the same as IP in ping message.

## Steps To Reproduce:

  1. Send "PingPeerMessage" with correct victim's IP
  2. Wait for "PingPeerMessage" from RSKJ
  3. Send "PongPeerMessage" with correct "check" value but spoofed IP
  4. Send "FindNodePeerMessage" in a loop to perform traffic amplification attack

I'm attaching PoC in the attachment. Need to fill correct RSKJ node IP and port and DDoS victim's IP (and run with root privileges on attacker's host).

## Supporting Material/References:

  * I'm sending patch in the attachment

## Impact

It makes much easier to perform DDoS attack and it can lead to DoS both of RSKJ node and third-party servers.

## Attachments
- ddos_poc.py
- ddos.patch
