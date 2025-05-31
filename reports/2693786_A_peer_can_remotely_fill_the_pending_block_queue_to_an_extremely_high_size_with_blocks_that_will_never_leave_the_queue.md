# A peer can remotely fill the pending block queue to an extremely high size, with blocks that will never leave the queue.

## Report Details
- **Report ID**: 2693786
- **URL**: https://hackerone.com/reports/2693786
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2024-09-01T23:01:32.582Z
- **Disclosed**: 2025-04-23T15:05:22.003Z

## Reporter
- **Username**: boog900
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
## Summary:

The pending block queue holds the blocks that we have downloaded but have yet to verify, because of a few lax rules in the synchronization code it's possible to fill this queue past the limit. My PoC could get the queue to ~54 GB, slightly larger would be possible with slight modifications. I _think_ you could fill the queue to an arbitrary size but it would require an extra step that I haven't tested yet. I think 54 GBs is enough to kill almost all nodes though.

# Issues 

Some parts of this section are not directly issues on their own, but they are part of the wider problem.

## The block queue can grow past its limit under certain circumstances

Here is where we decide whether to proceed and download blocks or wait: https://github.com/monero-project/monero/blob/a1dc85c5373a30f14aaf7dcfdd95f5a7375d3623/src/cryptonote_protocol/cryptonote_protocol_handler.inl#L2130

As you can see if `stripe_proceed_main` is `true` the limit is ignored. The `stripe_proceed_main` condition is pretty ugly so here is some helping comments:

```
bool stripe_proceed_main =
    (
        (m_sync_pruned_blocks && local_stripe && add_stripe != local_stripe) // True if we should sync pruned blocks, we are pruned and the peer has the next blocks pruned.
        || add_stripe == 0 // True if the next block is within the tip-blocks which won't be pruned.
        || peer_stripe == 0 // True if the peer does no pruning.
        || add_stripe == peer_stripe // True if the peer is pruned and has the next block un-pruned.
    )
    && 
    (
        next_block_height < bc_height + BLOCK_QUEUE_FORCE_DOWNLOAD_NEAR_BLOCKS // True if next_block_height is less than 1000 blocks above our blockchain
        || next_needed_height < bc_height + BLOCK_QUEUE_FORCE_DOWNLOAD_NEAR_BLOCKS // True if next_needed_heightis less than 1000 blocks above our blockchain
    );
```

The first part before the `&&` is just checking that the peer has the blocks unpruned or that we are syncing pruned blocks.

The problem is the next part, which allows the queue to grow past its allowed size if  `next_needed_height` or `next_block_height`  is less than 1000 above our chain.

`next_block_height` is the height of the next block we expect from the peer.

`next_needed_height` is got from https://github.com/monero-project/monero/blob/a1dc85c5373a30f14aaf7dcfdd95f5a7375d3623/src/cryptonote_protocol/block_queue.cpp#L160

As a side note `get_next_needed_height` seems to be incorrect, but I don't know what it was originally meant to do to confirm that. It's called `get_next_needed_height` and under normal circumstances in gets one more than the highest requested block, however under some conditions it will return a block way under that. Although this function being incorrect is not relied on for this issue.

## You can send blocks in a `GetObjectsResponse` that are not directly related

When receiving a  `GetObjectsResponse` monerod does not check that blocks are directly related to each other before adding the blocks to the queue.

It is possible to request blocks not in chronological order  but monerod wont do this, so it seems like we should be checking the blocks actually follow each other.

## Blocks currently downloaded, pending in the block queue, are in the `requested_hashes` list.

This may be intended behavior, but it does seem we should probably keep a separate list for actually downloaded blocks in the queue. 

## When trying to add blocks to the blockchain we check if the block parent is in the `requested_hashes` and skip

here: https://github.com/monero-project/monero/blob/a1dc85c5373a30f14aaf7dcfdd95f5a7375d3623/src/cryptonote_protocol/cryptonote_protocol_handler.inl#L1471

 # The attack

The attack now may be pretty obvious but the rough steps are to choose a height below the target peers to split the chain, create a dummy block a small number of blocks above the split point, this block is then the "anchor", set the first block in your split chain's `prev_id` to the hash of the anchor block and now just fill the rest of the blocks in with any `prev_id`.

Now because we are below the peers blockchain the size limit of the queue is ignored (?!?) and when the peer goes to add the blocks to the blockchain it would see the block's parent as still being "downloaded" and wait for it.

## Steps To Reproduce:

I have made a PoC, it is very rough, only works on a synced mainnet node and only makes a single connection so is pretty slow.

To run download the attached files, move the `.rs` files to a `src` directory and run:

```bash
cargo run -- --addr <NODE_ADDRESS>
```

For example to target a node at `127.0.0.1:18080`:

```bash
cargo run -- --addr 127.0.0.1:18080
```

You can run `sync_info` in monerod to see the size of the block queue.

---- 

This issue was found while helping  0xFFFC0000 with an issue ofrnxmr had, while testing their dynamic block sync size PR.

## Impact

Killing a node over a P2P connection.

## Attachments
- main.rs
- Cargo.toml
