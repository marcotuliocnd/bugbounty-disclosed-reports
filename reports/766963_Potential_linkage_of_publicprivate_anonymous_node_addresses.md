# Potential linkage of public/private (anonymous) node addresses

## Report Details
- **Report ID**: 766963
- **URL**: https://hackerone.com/reports/766963
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-01-02T04:08:39.991Z
- **Disclosed**: 2020-03-11T23:12:37.318Z

## Reporter
- **Username**: ahook
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
During the handshake for an incoming connection, the peer id is checked against the local node's peer id only for the specific zone of the incoming peer, in order to avoid linking public addresses to tor addresses:
https://github.com/monero-project/monero/blob/5d7ae2d2791c0244a221872a7ac62627abb81896/src/p2p/net_node.inl#L2343

However, on handshakes for outgoing connections, all zones are checked:
https://github.com/monero-project/monero/blob/5d7ae2d2791c0244a221872a7ac62627abb81896/src/p2p/net_node.inl#L1064

If an attacker wanted to link a specific tor node to a public node, they could potentially connect to as many public nodes as possible, get themselves added to the peer whitelist, maybe stuff some more attacker-owned addresses into the greylist, then disconnect, and for any future incoming connections, respond with the tor node's id in an attempt to link the public/tor addresses.

Low severity since it would probably take a while before they got lucky and the desired public node attempted an outgoing connection. But it would probably make sense to only check the right zone for outgoing handshakes as well to prevent such a possibility.

Also had another idea when brainstorming ways to link nodes, but it's more theoretical. An attacker could wait until a new release was about to drop, connect to as many nodes as possible, both public and tor, and log when disconnects occur. If a public node and tor node disconnect at the same time, it would be a pretty good indicator that they are the same node which was restarted due to the upgrade. Haven't thought of a way to mitigate such a timing attack yet.

## Impact

Exposure of a tor node's public address

## Attachments
No attachments
