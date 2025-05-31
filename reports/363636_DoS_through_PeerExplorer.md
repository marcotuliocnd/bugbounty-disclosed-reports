# DoS through PeerExplorer

## Report Details
- **Report ID**: 363636
- **URL**: https://hackerone.com/reports/363636
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-06-09T05:00:54.753Z
- **Disclosed**: 2019-09-18T13:16:28.759Z

## Reporter
- **Username**: z3t
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rootstocklabs

## Vulnerability Information
**Summary:** The peer discovery implementation is vulnerable to a Denial of Service attack due to improper management of connections.

**Description:** The two main files of interest in detailing this vulnerability are [PeerExplorer.java](https://github.com/rsksmart/rskj/blob/master/rskj-core/src/main/java/co/rsk/net/discovery/PeerExplorer.java) and [NodeChallengeManager.java](https://github.com/rsksmart/rskj/blob/master/rskj-core/src/main/java/co/rsk/net/discovery/NodeChallengeManager.java). To explain the flow of execution I'll be mentioning two theoretical nodes: an attacker, "N1" and a target, "N2".

When N1 sends an initial "ping" message to N2, N2 will reply with a "pong" message and a subsequent ping message to continue the handshake. After this, when N1 replies with a pong message, N2 will attempt to add N1 to its structure holding established connections. The relevant code snippets from `PeerExplorer.java` are below:
```    
public void handlePong(String ip, PongPeerMessage message) {
	PeerDiscoveryRequest request = this.pendingPingRequests.get(message.getMessageId());

	if (request != null && request.validateMessageResponse(message)) {
		this.pendingPingRequests.remove(message.getMessageId());
		NodeChallenge challenge = this.challengeManager.removeChallenge(message.getMessageId());
		if (challenge == null) {
			this.addConnection(message, ip, message.getPort());
		}
	}
}
...
private void addConnection(PongPeerMessage message, String ip, int port) {
	Node senderNode = new Node(message.getNodeId().getID(), ip, port);
	if (!StringUtils.equals(senderNode.getHexId(), this.localNode.getHexId())) {
		OperationResult result = this.distanceTable.addNode(senderNode);

		if (result.isSuccess()) {
			NodeID senderId = senderNode.getId();
			this.establishedConnections.put(senderId, senderNode);
			logger.debug("New Peer found ip:[{}] port[{}]", ip, port);
		} else {
			this.challengeManager.startChallenge(result.getAffectedEntry().getNode(), senderNode, this);
		}
	}
}
```
The `addConnection` method first attempts to add N1 to the `NodeDistanceTable` - a structure designed to hold a limited number of nodes (by default, 4096). If this insertion fails due to the target `NodeDistanceTable` bucket already being full, the attempted connection is instead added to `NodeChallengeManager`. The relevant code snippets from `NodeChallengeManager.java` are below:
```
public NodeChallenge startChallenge(Node challengedNode, Node challenger, PeerExplorer explorer) {
	PingPeerMessage pingMessage = explorer.sendPing(challengedNode.getAddress(), 1, challengedNode);
	String messageId = pingMessage.getMessageId();
	NodeChallenge challenge = new NodeChallenge(challengedNode, challenger, messageId);
	activeChallenges.put(messageId, challenge);
	return challenge;
}

public NodeChallenge removeChallenge(String challengeId) {
	return activeChallenges.remove(challengeId);
}
```

Through the `startChallenge` method N2 will send N1 another ping message, adding a "challenge" to `activeChallenges` with that new ping message's `messageId`. The issue here is that **the entry is only ever removed from `activeChallenges` if N1 replies with a pong that has the same `messageId` as the new ping message** - as seen in `PeerExplorer.handlePong`. Thus, N1 is able to create an arbitrary number of entries in `activeChallenges` by never sending N2 a pong with the challenge ping's `messageId`.

It should be noted that there is a slight limitation as to how this could be exploited by a single host. The relevant code snippets from `PeerExplorer.java` are below:
```
public PingPeerMessage sendPing(InetSocketAddress nodeAddress, int attempt, Node node) {
	PingPeerMessage nodeMessage = checkPendingPeerToAddress(nodeAddress);

	if (nodeMessage != null) {
		return nodeMessage;
	}
	....
}
...
private PingPeerMessage checkPendingPeerToAddress(InetSocketAddress address) {
	for (PeerDiscoveryRequest req : this.pendingPingRequests.values()) {
		if (req.getAddress().equals(address)) {
			return (PingPeerMessage) req.getMessage();
		}
	}

	return null;
}

```
The `sendPing` method will only ever actually send a new ping to N1 if there are no pending pings to its `InetSocketAddress` (which is deemed equal if the host and port match) - as seen in `checkPendingPeerToAddress`. However, pending pings have a set expiry time (by default, 30 seconds) and those that have expired are cleared by `PeerExplorerCleaner` at a fixed rate (by default, every 60 seconds). So due to this limitation, with the default configuration settings a single host can only complete 65,535 handshakes (one per port) every minute - imposing a (perhaps unreachable) limit on the time it takes to exhaust the target node's memory. Though this can obviously be circumvented by using multiple hosts to attack a target node. 


Because most peer discovery functionality identifies nodes by their `NodeID` and not by host/port, it's trivial to send a flood of requests with unique `NodeID`s to fill `NodeDistanceTable` and subsequently make an unrestricted amount of in-memory insertions into `NodeChallengeManager.activeChallenges`. This is further aided by the fact that `NodeChallengeManager` is never purged, so the request flood does not have to occur within a short period of time. Memory exhaustion will eventually occur as the `NodeChallenge` objects begin taking up a significant amount of memory and are not eligible for garbage collection. This is expected to eventually disable node functionality as individual threads die when they throw `OutOfMemoryError`s, but in my testing it ended up crashing the whole JVM after reaching ~200,000 insertions.

## Steps To Reproduce:

I've attached a PoC program that interfaces with the RSKj library for the sake of simplicity. Due to the PoC program being somewhat inefficient and unreliable, I ended up accelerating the testing process by modifying my testing node's `NodeChallengeManager` to make 10 insertions per valid `startChallenge` call. If you're interested in running the PoC despite those issues, follow these steps:
  1. Download a copy of the RSKj code
  2. Move the PoC files into the `co.rsk.net.discovery` package (overwrite `PeerExplorer.java` with my modified version)
  3. Launch a node for testing - ensure peer discovery is enabled
  4. Compile and run the PoC from `PeerFlood` - arguments format: `<local_address> <target_address> <target_port> <num_threads>`
  5. Monitor testing node's logs and stability

If you're developing your own PoC, you need to simply flood a testing node with connections that use random `NodeID`s, completing a single ping<->pong handshake then immediately disconnecting.

## Mitigation
This could be mitigated by implementing expiring challenges that are cleared by `PeerExplorerCleaner`.

## Impact

An attacker could crash any RSKj node with peer discovery enabled (which it is by default).

## Attachments
- PoC.zip
