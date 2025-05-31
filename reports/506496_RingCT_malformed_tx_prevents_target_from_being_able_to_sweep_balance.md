# RingCT malformed tx prevents target from being able to sweep balance

## Report Details
- **Report ID**: 506496
- **URL**: https://hackerone.com/reports/506496
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-03-07T20:46:58.869Z
- **Disclosed**: 2019-04-20T22:44:25.226Z

## Reporter
- **Username**: organdonor1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
## Summary:
An attacker can send a malformed RingCT transaction to an attackee wallet that prevents the attackee from sweeping their wallet balance. This is done by the attacker changing the mask amount in `genRctSimple` with a modified wallet. The attacker does not need any intervention from the attackee other than their public Monero address.

## Releases Affected:

  * Affects all versions of monero-wallet-cli and monero-wallet-rpc

## Steps To Reproduce:

  1. Clone and compile the v0.14.0.2 tagged branch of monero-project/monero
  2. Create a new attackee wallet on stagenet. Load it up by sending a few  transactions of various amounts to this wallet.
  3. Create a new attacker wallet on stagenet. Send one small amount of coins such as 0.1 XMR.
  4. [Modify this line in rctSigs.cpp](https://github.com/monero-project/monero/blob/v0.14.0.2/src/ringct/rctSigs.cpp#L803) to ` rv.ecdhInfo[i].amount = d2h(MONEY_SUPPLY);`
  5. Recompile monero-project/monero
  6. Open the attacker wallet and send a transaction to the attackee wallet. The amount you select to transfer does not matter. Send 0.05 XMR as an example.
  7. Switch back to upstream code without the patch from step 4.
  8. Open the attackee wallet and wait for network confirmations. The malformed transaction will correctly show up as 0 XMR. 
  9. Attempt to sweep all from the attackee wallet to any destination. The attackee wallet will throw an error: “Error: internal error: Daemon response did not include the requested real output.”

## How to fix this:
The bug is fixed by changing two lines in `wallet2.cpp`. [After this conditional](https://github.com/monero-project/monero/blob//v0.14.0.2/src/wallet/wallet2.cpp#L1337) add `if (!tx_scan_info.money_transfered) { return; } outs.push_back(i);` and remove `outs.push_back(i);` from a few lines earlier. Recompile and rescan the attackee wallet.

## Supporting Material/References:
This bug was found by carefully inspecting [this ryo-currency commit](https://github.com/ryo-currency/ryo-currency/commit/e7931ca065baba61bf9b7b96ce567f07669d75de) which was suggested to have a bug fix within. This one line fix makes itself evident because there is no relation to coinbase outputs on this line.

Attackee example stagenet wallet seed: 

```
yesterday doorway sizes royal sipped mesh nephew around
idols laptop cactus present imagine ponies puzzled auctions
poaching jogger surfer launching phase rewind soda tequila ponies
```

## Impact

An attacker can send malformed transactions and prevent an attackee from being able to sweep their balance. The attackee needs to apply the patch described above and rescan their wallet if they have been affected. Since this attack doesn’t cause permanent damage, it is less severe, however forcing the attackee to rescan their wallet causes loss of data such as tx secret keys.

## Attachments
No attachments
