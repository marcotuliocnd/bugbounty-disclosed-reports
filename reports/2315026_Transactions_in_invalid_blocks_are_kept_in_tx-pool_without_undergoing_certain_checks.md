# Transactions in invalid blocks are kept in tx-pool without undergoing certain checks.

## Report Details
- **Report ID**: 2315026
- **URL**: https://hackerone.com/reports/2315026
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2024-01-13T23:44:14.629Z
- **Disclosed**: 2025-04-23T18:26:38.708Z

## Reporter
- **Username**: boog900
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
## Summary:
When adding blocks to the blockchain monerod first adds the transaction(s) to the tx pool with `relay_method::block`, this means the tx-pool skips certain checks like fee and extra field size, this is expected though. However if the block turns out to be invalid the transactions are kept in the pool and do not undergo the relay checks, this wouldn't be too bad if one of the checks ignored wasn't that the inputs are valid.

Because monerod [ignores the input validity check](https://github.com/monero-project/monero/blob/ac02af92867590ca80b2779a7bbeafa99ff94dcb/src/cryptonote_core/tx_pool.cpp#L274) for `relay_method::block` txs it is possible for someone to craft a block full of completely invalid txs and fill a nodes tx-pool with junk.

## Steps To Reproduce:

I have created a PoC, it is very rough and may need a couple runs, what it does is repeatedly send blocks full of invalid txs to the node address provided. 

To run you need a synced node, the node must also think it is synced, how I did it was first allowing the node to connect to the network and the disconnecting it with `out_peers 0` when it reports it's synchronized just to be safe. The top block in the blockchain must also have at least one tx (not including the miner tx) as the PoC will use this tx to create more invalid txs.

I have uploaded the code here I don't know if that's the best way to share it, if not I'm happy to share it another way. As it seems folders aren't supported here you will need to create a `src` folder and move `utils.rs` and `main.rs` inside keeping `Cargo.toml` and `Cargo.lock` on the outside.

It uses Cuprate's p2p code so you will need Rust installed to run it. 

with Rust installed to run you would do this from the root of the files:

```
cargo run -r  [network] [node]
```
so to target a node at `127.0.0.1:18080` on mainnet you would do:

```
cargo run -r  mainnet 127.0.0.1:18080
```
## Potential Fix

A way to fix this is keeping track of what txs we didn't already know about when a new block comes in and then if the block turns out to be invalid checking the txs again with a different relay method (not block).

## Impact

The most obvious issue this causes is stopping the flow of txs around the network as if a tx is `relay_method::block` then when pruning the tx pool [it will never be removed](https://github.com/monero-project/monero/blob/ac02af92867590ca80b2779a7bbeafa99ff94dcb/src/cryptonote_core/tx_pool.cpp#L465), leaving other, valid, txs to be removed, the `prune` function is called after every tx is added to the pool so you could empty a nodes pool of valid txs and stop it accepting more txs.

However when I ran my PoC on my node it completely broke it, it froze it and then I could not start it again the logs just repeated this:

```
2024-01-13 20:43:59.190	[P2P6]	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1887	BlockchainLMDB::get_txpool_tx_meta
2024-01-13 20:43:59.190	[P2P6]	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1887	BlockchainLMDB::get_txpool_tx_meta
2024-01-13 20:43:59.190	[P2P6]	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1887	BlockchainLMDB::get_txpool_tx_meta
2024-01-13 20:43:59.190	[P2P6]	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1887	BlockchainLMDB::get_txpool_tx_meta
2024-01-13 20:43:59.190	[P2P6]	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1887	BlockchainLMDB::get_txpool_tx_meta
``` 
I couldn't see anywhere where it could be stuck in a loop (I didn't look much though) and I couldn't manually flush the txpool.


Another issue I can think of is sending "valid" transactions with no fee, although other nodes wont be able to broadcast this around the network if the attacker manages to send it to a miner the miner might include it in the block template if there is enough room (it should be lowest priority though as no fee) then this can be repeated to spam the chain to bloat it or to try de-anonymize txs for cheap (free?).

## Attachments
- Cargo.lock
- Cargo.toml
- utils.rs
- main.rs
