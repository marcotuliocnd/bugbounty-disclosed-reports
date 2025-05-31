# Out-of-bounds read when importing corrupt blockchain with monero-blockchain-import

## Report Details
- **Report ID**: 284951
- **URL**: https://hackerone.com/reports/284951
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-10-31T20:50:31.348Z
- **Disclosed**: 2018-04-25T05:49:59.363Z

## Reporter
- **Username**: sybr
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
It is possible to trigger an *out-of-bounds read* in *monero-blockchain-import* when importing a corrupt blockchain and not verifying blocks and transitions during import (--verify 0).

Using a corrupt import_file, the attacker has full control over *buffer_block* in import_from_file (blockchain_import.cpp). As shown in the following lines of code (blockchain_import.cpp:404-407), this also enables the attacker to craft a corrupt bootstrap::block_package bp at will:
```
str1.assign(buffer_block, chunk_size);
bootstrap::block_package bp;
if (! ::serialization::parse_binary(str1, bp))
    throw std::runtime_error("Error in deserialization of chunk");
```

If verification is turned off (opt_verify = false), the following line of code (blockchain_import.cpp:484) is executed, where all arguments in the function call are extracted from the corrupt *bp*, hence, controlled by the attacker:
```
core.get_blockchain_storage().get_db().add_block(b, block_size, cumulative_difficulty, coins_generated, txs);
```
The executed function *BlockchainLMDB::add_block* then executes the following line of code (db_lmdb.cpp:2850), which passes the same (corrupt) arguments to the function *BlockchainDB::add_block*, where the actual memory corruption finally happens:
```
BlockchainDB::add_block(blk, block_size, cumulative_difficulty, coins_generated, txs);
```
In *BlockchainDB::add_block*, there is unfortunately no sanity check about the passed arguments and the following lines are executed (blockchain_db:210-217):
```
int tx_i = 0;
crypto::hash tx_hash = null_hash;
for (const transaction& tx : txs)
{
    tx_hash = blk.tx_hashes[tx_i];                   // here the out-of-bounds read happens
    add_transaction(blk_hash, tx, &tx_hash);
    ++tx_i;
}
```
As *txs* as well as *blk* originate from the *bootstrap::block_package bp* generated in blockchain_import, they can be set to arbitrary values by the attacker. In particular, if *bp* is crafted such that *bp.txs.size() > bp.block.tx_hashes.size()*, then an out-of-bounds memory corruption happens in the for loop when accessing *blk.tx_hashes*.

I have not yet examined whether the bug can be exploited in any malicious way, but I think it needs to be fixed anyways. Further, as the bug happens in the database outside of blockchain_import.cpp, it may also affect other code in monero, not only *monero-blockchain-import*. I have also not checked that. The bug can be easily fixed by introducing additional sanity checks, such as, whether *bp.txs.size() != bp.block.tx_hashes.size()*.

I'll be happy to answer any further questions regarding the bug. Thank you!

## Attachments
No attachments
