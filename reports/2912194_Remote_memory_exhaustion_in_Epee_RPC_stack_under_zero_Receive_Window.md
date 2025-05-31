# Remote memory exhaustion in Epee RPC stack under zero Receive Window

## Report Details
- **Report ID**: 2912194
- **URL**: https://hackerone.com/reports/2912194
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-12-23T02:11:16.389Z
- **Disclosed**: 2025-04-23T13:53:57.953Z

## Reporter
- **Username**: sagewilder2022
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
## Summary

Memory exhaustion can be triggered in `http_protocol_handler.inl` and `abstract_tcp_server2.inl` under delayed ACK or zero Receive Window advertisement. This can lead with specific RPC methods to remote crash of nodes through restricted RPC endpoints.

## Releases Affected

Every branches of monero(d).

## Details

If a socket delays ACK packets and let TCP receive window diminish (for example, by not reading the response from the server), responses are kept in epee server send queue up until a memory exhaustion happen. The RPC method used heavily influence the rapidity of the memory exhaustion.

monerod had the following arguments: `--prune-blockchain --sync-pruned-block --rpc-restricted-bind-port=18089`
Tests have been conducted using the undocumented `get_txids_loose`, `get_info` and `get_output_distribution` methods, generating 208kB, 1.5kB and 17MB response respectively:
```json
{"jsonrpc":"2.0","id":"0","method":"get_output_distribution","params":{"amounts":[0],"from_height":0,"to_height":3300000,"compress":false}}
{"jsonrpc":"2.0","id":"0","method":"get_txids_loose","params":{"txid_template":"0000000000000000000000000000000000000000000000000000000000000000","num_matching_bits":14}}
```
Any JSON-RPC request can be weaponized.

Valgrind of an OOM crash indicated that the memory being leaked originates from a string append at [`/contrib/epee/include/net/http_protocol_handler.inl#L607`](https://github.com/monero-project/monero/blob/893916ad091a92e765ce3241b94e706ad012b62a/contrib/epee/include/net/http_protocol_handler.inl#L607C4-L607C5)
```cpp
  LOG_PRINT_L3("HTTP_RESPONSE_HEAD: << \r\n" << response_data);

	if ((response.m_body.size() && (query_info.m_http_method != http::http_method_head)) || (query_info.m_http_method == http::http_method_options))
		response_data += response.m_body; // <------- here

	m_psnd_hndlr->do_send(byte_slice{std::move(response_data)});
```
This complete string response is then converted into an `epee::byte_slice` and passed to [`/contrib/epee/include/net/abstract_tcp_server2.inl#L756`](https://github.com/monero-project/monero/blob/893916ad091a92e765ce3241b94e706ad012b62a/contrib/epee/include/net/abstract_tcp_server2.inl#L756):
```cpp
template<typename T>
bool connection<T>::send(epee::byte_slice message)
{
  std::lock_guard<std::mutex> guard(m_state.lock);
  if (m_state.status != status_t::RUNNING || m_state.socket.wait_handshake)
    return false;

  // Send queue logic...
```

Here the send queue logic is to accept up to `ABSTRACT_SERVER_SEND_QUE_MAX_COUNT` (1000) responses, if this limit is exceeded then the server starts a random delay between 5 and 6 seconds. If this delay is over, the connection is terminated. All the responses are stored here before being sent, regardless of their size. If we take `get_output_distribution`, one can store up to 17GB in the queue, and more during a period of at least 5 seconds.

The testing virtual machine is equipped with 16 threads, 12GB of RAM and Ubuntu 24.04 LTS.
The PoC has been tested using 1, 4 and 16 sockets with 200 milliseconds delay between requests.
The limit imposed by vtnerd's TCP improvement branch is 31.
A 16 socket execution can kill the node (or machine) in under 30 seconds.
Affected and tested branches are [`master`](https://github.com/monero-project/monero/tree/master) and [`vtnerd:improvement/tcp_throttling`](https://github.com/vtnerd/monero/tree/improvement/tcp_throttling)

### Suspicion of memory leaks

In rare cases (4 times), after the PoC stopped, monerod was let with part of its memory allocated for responses not freed. Effectively leaking memory.
Examining this code I have not been able to assert the exact location of it and the unreliability do not help at profiling the issue.
I do not believe to have introduced something that caused these irregularities. I invite reviewers to be careful upon testing and reviewing the current stack.

### Note

This vulnerability has been assessed after discovering a first bug when fuzzing the RPC stack. The p2p throttle code was entangled with the rpc bandwith leading to complete p2p disconnection under RPC throttling. A search on github permitted to find an open PR fixing this bug and aditional mitigations:
https://github.com/monero-project/monero/pull/9459.

Decision has been taken to test both branches.

### Bounty

XMR address: 8BbCtXoBTuxNYnngbLvfpMQRp2qJEQVtH715eUnM34VvFvUYkdJbSwTCLsBjyr4SjYUskFjNCvoGaA6tiJeKf5jW1PvxPSo

## Impact

Remote crash of any node exposing their RPC interface.

## Attachments
- poc.cpp
- POC_16sockets.mp4
- POC_1socket.mp4
