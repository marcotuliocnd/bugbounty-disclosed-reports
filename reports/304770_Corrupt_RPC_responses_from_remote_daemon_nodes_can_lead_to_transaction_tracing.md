# Corrupt RPC responses from remote daemon nodes can lead to transaction tracing

## Report Details
- **Report ID**: 304770
- **URL**: https://hackerone.com/reports/304770
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-01-14T21:22:24.574Z
- **Disclosed**: 2018-03-16T22:10:21.957Z

## Reporter
- **Username**: monero-hax123
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
Dear Monero security team,
    We’re writing to disclose a privacy vulnerability when using monero-cli or monero-gui with an untrusted remote node.

When using a remote node, the Monero client relies on the node to provide information from the blockchain, in particular the public keys and transaction outputs corresponding to mixins that the client chooses by global index (gidx). The client selects a handful of gidxs, and passes these in a request to the “get_outs.bin” RPC endpoint. The client is generally designed to provide *untraceability* even against the untrusted remote node, e.g. by masking which index in the request is the real one being spent. However, if the remote node provides an invalid response then the client may end up inadvertently revealing information about the real gidx being spent.

In more detail there, we've made a proof-of-concept of two forms of this attack:

#1 Retry-and-intersect attack. 
====
If the attacker remote node returns bogus data, and the user *retries the same transaction* after clicking through the error message, it most likely reveals to the remote node exactly which coin in the transaction is the real one being spent.

1. The attacker modifies monerod to return all bogus public keys in response to the first “get_outs.bin” request.

2. The client reports an error that invalid data was received, but does not disconnect from the remote node or otherwise change its behavior. The outputs remain available for use.

3. If the user dismisses the error and then tries the same transaction again, then the client samples a *new set of mixins* to request along with the real output again.

4. The remote node looks at the two requests. Most likely, there is a unique intersection between the two sets of requested gidxs, which corresponds to the real transaction output.

5. The remote node responds to the second request with correct data, so the transaction goes through.
As a proof of concept, we tested this 10 times with a monero-cli and our own modified monerod, and found that the correct output was detected in each trial. It is possible that two such requests do not have a unique intersection, but this appears to happen with low frequency.

This is an active attack, and involves showing an error message to the client. This would likely raise suspicion if occurred many times in a row. However, since the transaction goes through without error on the second request, used sparingly it may not raise suspicion.

#2 Guess-and-check attack
====
If the remote node returns bogus data for some but not all of of the requested gidxs, then by observing the client’s behavior it can tell whether the real transaction input is one of the bogus ones or not.

1. The attacker modifies monerod to return bogus public keys for all but one of the requested gidxs. There are two cases, depending on whether the real transaction input is one of the bogus ones.

2a. The real input is one of the bogus public keys.
   The client is able to identify the incorrect response. It throws an exception, and will not sign and transmit any transaction (until after making subsequent get_out.bin requests). The attacker learns that the real transaction input is not one of the bogus ones.

2b. The real input corresponds to the non-bogus response

   The wallet is unable to discover that the response is invalid, and therefore proceeds to sign and transmit the transaction to the remote node. The attacker learns that the real transaction input is the bogus one.

Since the transaction is invalid, it will not show up on the blockchain. However, the client stores the transaction in the wallet as “pending”, such that its transaction inputs will not be reused again for 24 hours.

Because the client requests many more public keys than it actually needs for mixins (e.g., a default of 58 gidx requested for a ring size of 5), the probability of succeeding is small but non-negligible. If the attack fails (case 2a), the attacker cannot easily “try again”, since the transaction inputs are unavailable for 24 hours. (However, we note that this behavior could also be considered a DoS vector for a remote node, and hence we imagine there could be a pressure to change this behavior, trading off privacy for DoS-resilience.)

Attacks exacerbated by unauthenticated RPC
======
We have described these two attack scenarios from the point of view of a corrupted remote node. However, because data between clients and the remote node is not authenticated (http json rather than https), this attack could also be performed by any on-path adversary (such as a router or ISP)

## Impact

Severity:
=======
The first of the two attacks is more severe, since the attacker can trace the transaction inputs with high probability while raising minimal suspicion to the user. We therefore recommend immediately implementing mitigations 1-3 as suggested below. The second attack type is less severe, since it has a smaller chance of success and cannot easily be repeated multiple times to increase the chance.
Remote node operation can be considered a “non-default” configuration, which is a mitigating factor. However, it is clear that many users would prefer a light client for administrative and performance reasons (it takes a while to sync a full node). Instructions for remote node operation appear on the getmonero.org user guides page, and infrastructure support is increasing (e.g., there are several “open nodes” services that provide lists of available remote nodes to connect to). So we think it is likely that this usage mode will see increased use in the near future. Statistics from moneroworld could be requested to estimate the popularity of this configuration.

The instructions at MoneroWorld https://moneroworld.com/#nodes do stress that remote nodes is not the recommended mode of operation and could lead to additional privacy risks. However, the instructions explain “the primary risk is that a remote node can get your IP address.” Hence we think it is likely that users may follow these instructions, and even take precautions to shield their IP address (e.g., use Tor), but still fail to achieve the untraceability they expect. The instructions at getmonero do not provide warnings at all: https://getmonero.org/resources/user-guides/remote_node_gui.html )
To our knowledge, this attack vector is new and has not been discussed before in forums or reddit.
We suggest this should be considered MEDIUM severity according to the standards of the Vulnerability Response Process.

Potential Mitigations
=========
1. _User warnings._ Any exceptions encountered in the RPC, after sending the list of gidxs to the remote node but prior to committing the transaction, should come with enhanced error messages warning about the potential of an active tracing attack. The instructions on using remote nodes should be expanded to warn the user in advance of this possibility against retrying a transaction. Statistics from moneroworld should be used to estimate the number of potentially affected users.

2. _Caching of get_outs requests._ After the client samples a list of gidxs associated with a transaction output, it should immediately commit these to a persistent data structure (similar to the pending transactions in the wallet). If the output is used again in a short time interval (because of an exception through in the get_outs.bin RPC query or for any other reason), then the exact same gidxs should be sampled. This directly prevents the intersection attack #1 described above, however it does nothing to address attack #2.

3. _Use a secure channel (TLS) between the client and remote node._ Communications should be JSON-RPC over HTTPS instead of over HTTP. Even opportunistic encryption (if the remote cannot be authenticated by a standard certificate) would require a network attacker to mount an active MitM first, which at least requires them to conduct a more invasive attack

4. _Disconnect & blacklist remote node on failures._
Both of the attacks involve a remote node sending corrupt information in response to get_outs. Immediately blacklisting the node upon such an event reduces the effectiveness of the attack. A caveat is that with several “open nodes” services, e.g. nodes.moneroworld.com, which DNS-resolve to multiple IP addresses of different volunteers, the blacklist should be at the IP level rather than the hostname level. This should only be implemented after mitigation 3, since otherwise it would allow on-path adversaries to cause honest remote nodes to be falsely blacklisted.

5. _Use authenticated data structures._ Although attack #2 is of lower severity, it is difficult to stamp out entirely. The general problem is that it is currently impossible for a client to authenticate get_outs.bin responses from a remote node except for public keys that it already knows, i.e. the real transaction input. Hence the differential behavior reveals information about the treal transaction inputs. A systematic mitigation would be to add an additional Merkle tree data structure to the Monero blockchain, indexed by gidx, that allows the client to authenticate responses to get_idx. We are currently working on a writeup about this mitigation, but the simpler mitigations could be employed in the meantime.

## Attachments
No attachments
