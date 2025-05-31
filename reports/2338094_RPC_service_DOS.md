# RPC service DOS

## Report Details
- **Report ID**: 2338094
- **URL**: https://hackerone.com/reports/2338094
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-01-28T19:29:52.023Z
- **Disclosed**: 2025-05-23T14:25:17.381Z

## Reporter
- **Username**: ptrstr
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
## Summary:
The RPC service running port 18081 (or 28081, 38081) is vulnerable to a DOS rendering the service unusable. This is due to the possibility of a for loop going up until uint64_t's max range (1<<64 - 1).

On the `get_fee_estimate` JSON RPC endpoint, a `uint64_t` parameter `grace_blocks` can be passed. If this parameter is big and the node is on a `hard_fork` version `15` or above, `get_dynamic_base_fee_estimate_2021_scaling` will be called.
https://github.com/monero-project/monero/blob/v0.18.3.1/src/rpc/core_rpc_server.h#L177
{F3012477}

This handler will then be called:
https://github.com/monero-project/monero/blob/v0.18.3.1/src/rpc/core_rpc_server.cpp#L2956
{F3012488}

This function is then called
https://github.com/monero-project/monero/blob/v0.18.3.1/src/cryptonote_core/blockchain.cpp#L3830
{F3012496}

## Releases Affected:
From my research, all versions after commit [b030f207517f59a5122409398549a02ac23829ae](https://github.com/monero-project/monero/commit/b030f207517f59a5122409398549a02ac23829ae) are vulnerable.
  * v0.18.3.1
  * v0.18.3.0
  * v0.18.2.2
  * v0.18.2.1
  * v0.18.2.0
  * v0.18.1.2
  * v0.18.1.1
  * v0.18.1.0
  * v0.18.0.0 

## Steps To Reproduce:
  1. Start a Monero node with the RPC port opened.
  2. Verify the node is using `hard_fork` version `15` or above
    - To do this, you can do the [`hard_fork_info` JSON RPC request](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#hard_fork_info)
  3. Perform a few asynchronous requests to the [`get_fee_estimate` JSON RPC endpoint](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#get_fee_estimate) with `grace_blocks` set to a very very large integer (can go up to 18446744073709551615)
  4. The server should now not be responsive on the RPC port.

## Supporting Material/References:
**Attached is a PoC script using Python's `requests` module to send 500 requests to a server.**
*To run the script, make sure to change the `HOST` variable at the top of the file. You can just replace `127.0.0.1` with any IP you want where a Monero node is running.*


CPU exhaustion in `htop`. From my understanding, the RPC server runs on two threads.
{F3012501}

After this, any request to the port times out, furthermore, it is not shown in Monero's log (with `seg_log 4`)

## Housekeeping

1. Be sure to read our policy before submitting
2. Provide an XMR address within the report if you wish to receive bounty (assuming that the report is valid)
    - `47ZpAkp3sYGhHM6HEMUMDK7WBi6uLXy2H9LtB3aVNJfB54a3c12LybvWH3EjAF3echFrthjMvw17k7hn9Sbwr5Uh9VgKNNS`

## Impact

An attacker could find all open Monero RPC services using a Censys query such as:
- `services.port = 18081 and (services.port = 18080 and services=monero)`

https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=EXCLUDE&q=services.port+%3D+18081+and+%28services.port+%3D+18080+and+services%3Dmonero%29

And bring all those services down.

## Attachments
- image.png
- image.png
- image.png
- image.png
- dos.py
