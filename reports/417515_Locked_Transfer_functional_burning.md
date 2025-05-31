# Locked_Transfer functional burning

## Report Details
- **Report ID**: 417515
- **URL**: https://hackerone.com/reports/417515
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-10-02T10:43:45.526Z
- **Disclosed**: 2019-07-09T21:46:20.520Z

## Reporter
- **Username**: keejef
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
**Summary:** Using the `locked_transfer` command in the monero-wallet-cli users can send outputs with high lock times like 1,000,000 blocks. A vendor will accept these transactions with no warnings and credit a user balance. The user can now withdrawal or sell this balance and the vendor is left with outputs that will not unlock for 1000s of years.

**Description:** 

This bug essentially exploits the use of the `show_transfers` command by vendors that credit balances, functionally the result is the same as the double output bug found a week [ago](https://github.com/monero-project/monero/pull/4438). It is presumed at this point that anything in the Cryptonote/ Monero protocol that can show a valid transfer in `show_transfers` will be accepted by vendors, even if it creates un-spendable or functionality un-spendable outputs.

## Releases Affected:

  *  0.12.3.0 Lithium Luna - All Operating Systems 
  *  Current Monero master 

This will also affect all Cryptonote coins with `locked_transfer` and exchanges that use `show_transfers`

## Steps To Reproduce:

  1. Transfer Monero or other Cryptonote coin to wallet-cli 
  2. Use `locked_transfer` set a high amount lockblocks, send to exchange or other vendor that will credit your balance.
  3. Sell, or withdrawal your currency on the exchange, leaving them with locked coins, the attacker only loses the minimal fee that the exchange charges, while the exchange is left with un-spendable coins. 

This bug has been tested against two separate exchanges with very small amounts of Monero, that will unlock after 4 months. This method will likely be effective against all exchanges that use `show_transfers` as a method of auditing incoming transactions (which i think is nearly all of them).  

P.S. Discovery of bugs like these would not be possible without the help of my coworkers at Loki, so i want to thank them for their help brainstorming on this one.

## Impact

This bug cannot be used to create new Monero but it can be used to attack Monero vendors with coins they can functionally never spend.

## Attachments
No attachments
