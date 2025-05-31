# Spamming highly nested JSON RPC requests cause node to disconnect from p2p network

## Report Details
- **Report ID**: 2677306
- **URL**: https://hackerone.com/reports/2677306
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2024-08-22T15:54:54.102Z
- **Disclosed**: 2025-04-23T12:05:28.755Z

## Reporter
- **Username**: asurar0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
## Summary:
By forging a highly nested JSON payload, and spamming it through a restricted RPC interface, an adversary can remotely lock monerod from syncing with the rest of the p2p network. This vulnerability apply to syncing node as well synced one (which then become outdated)
Epee JSON parser allow duplicated fields and set a recursion limit reasonably too high (100). By appending 1747 Json object of depth 98, an attacker can forge a JSON RPC payload that will cause CPU intensive parsing operations, locking the rest of the node from syncing with the P2P network.

This apply to monerod (master branch a1dc85c)

## Proof of Concept:

A rust written proof of concept is shared at the bottom of this document. You can compile it using the latest stable rust toolchain and importing the corresponding crate in your Cargo.toml file

## Additional information:

The proof of concept has been only tested against 18089 restricted rpc port and using the `get_info` method. I was able to effectively lock a synced node from syncing during a period of 3 hour. monerod was running on an AMD Ryzen 7 5800X. Another test has been performed with a single and empty `params` field, which concluded in no overhead for the Monero daemon.

Other I/O requesting methods could be exploited as well (`get_blocks`). if multiple `params` fields are set, only the last one being parsed will be used. You can therefore replace the last `params` field with genuine arguments and still trigger the execution of the routine. Combined with a low vulnerability (that will be submitted soon after this report), this could lead to I/O overhead by both writing and reading at high bandwith.

## Potential mitigation:

- Lower the 1MB limit set by `m_net_server.get_config_object().m_max_content_length = MAX_RPC_CONTENT_LENGTH` in `src/rpc/core_rpc_server.cpp`
- Disable duplicated fields (as recommended by RFC 8259).
- Reduce `EPEE_JSON_RECURSION_LIMIT_INTERNAL` (`contrib/epee/include/storages/portable_storage_from_json.h`) to a reasonable amount: 10~20.
- Enable an iteration limit to objects and arrays. Potentially 1000 as it is the maximum number of blocks a restricted `get_blocks` call can process.
- Move JSON RPC parsing to another thread.
- Implement API throttling for the HTTP RPC Server. At my understanding, an API throttling already exist for P2P, maybe could it be reused ?

XMR Address: ███

## Impact

At individual scale, it enable remote and temporary (or definitive) disconnection of nodes from the p2p network.
Used at higher scale, it can be used against mining pool nodes to prohibit them from syncing and enable easier 51% attack.

## Attachments
- disconnection.png
- 15mintest.png
- main.rs
- Cargo.toml
