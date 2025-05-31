# A bug in the Monero wallet balance can enable theft from exchanges

## Report Details
- **Report ID**: 377592
- **URL**: https://hackerone.com/reports/377592
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-07-05T16:49:15.267Z
- **Disclosed**: 2018-08-02T00:12:00.655Z

## Reporter
- **Username**: jagerman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
**Summary:**
A Monero bug (already fixed in master) allows theft from exchanges.  This has been exploited again a Monero-derived coin, so the exploit may be underway currently.

**Description:**
(fluffypony: Also please mention you spoke to me and I recommended you put it on HackerOne)

PR #3985 fixed a wallet balance display bug, which seems innocuous enough, but this bug also extends to exchanges: a transfer of, e.g., 1 XMR to an exchange with a duplicated TX pub key will show up on an exchange as a 2 XMR deposit, which then allows the attacker to withdraw 2 XMR from the exchange's wallet.  An attacker could exploit this repeatedly to siphon of all of the exchange's balance.

## Releases Affected:

  * 0.12.2.0, which is currently active and used by exchanges, and likely earlier releases.
  * current master and the 0.12.3.0 PR branch have the fix applied

## Steps To Reproduce:

  1. deliberately double-sign a transaction with the tx pub key, e.g. by doubling the `add_tx_pub_key_to_extra(tx, txkey_pub);` call in `src/cryptonote_core/cryptonote_tx_utils.cpp`.
  1. Transfer an amount (or send to an exchange)
  1. See 2x the transferred amount appear on the recipient wallet (or the exchange).

## Supporting Material/References:

  * I've notified several other Monero-derived coins that I am in contact with, along with Cryptopia.
  * This attack was carried out against ArQmA on altex.exchange; 4 different wallets managed to steal the entire ARQ exchange deposits before the ARQ wallet was put into maintenance.

## Impact

Theft of all coins deposited in an exchange wallet.

## Attachments
No attachments
