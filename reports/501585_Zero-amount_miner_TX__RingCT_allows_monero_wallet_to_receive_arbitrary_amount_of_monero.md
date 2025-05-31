# Zero-amount miner TX + RingCT allows monero wallet to receive arbitrary amount of monero

## Report Details
- **Report ID**: 501585
- **URL**: https://hackerone.com/reports/501585
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-02-25T20:14:12.249Z
- **Disclosed**: 2019-07-03T00:12:36.057Z

## Reporter
- **Username**: cutcoin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty, so be sure to take your time filling out the report!

**Summary:** 

By mining a specially crafted block, that still passes daemon verification an attacker can create a miner transaction that appears to the wallet to include sum of XMR picked by the attacker. It is our belief that this can be exploited to steal money from exchanges.

**Description:** 

I'm the lead developer of CUT coin (https://github.com/cutcoin/cutcoin), a coin based on Monero codebase. Our aim is to build a cryptonote coin with proof of stake consensus.  In order to achieve this we needed to deeply analize both block verification in daemon and get familiar with wallet code. This lead us to discovering a vulnerability in (mainly) the wallet, that allows an attacker to convince any cli wallet that it received transaction with amount chosen by the attacker, that is virtually any. It is our believe that this can be used to send such counterfeit XMR to an exchange, that will credit the attacker with the sait amount of XMR inside the exchange, which can be exchanged for other coins and withdrawn. However this was of course not attempted. It is our belief that the vulnerability can not be used to "mint" real, transactable monero out of thin air, at least without knowledge of private key of rct::H.

The vulnerability is not very hard to describe. According to current verification rules in the daemon, it is perfectly fine to have a zero amount in the miner transaction (besides the real, non-zero amount). It is also perfectly fine to have RCT signatures and they of course will not be checked. On the other hand, there is code in the wallet that basically says "if the amount is zero, decode the amount from RCT".

So to exploit the vulnerability an attacker will need to modify the daemon to create blocktemplates with zero amount in the miner tx, with a valid-enough RCT signatures so the amount will decode. The attacker will need to mine a block directly to an exchange wallet. Most exchanges identify their users by payment id. Including the said field in miner tx is not available functionality. While this seems to be trivial to implement, it was not attempted by us.

Obviously this issue can be resolved in both the daemon and the wallet.

We have verified that the vulnerability is exploitable against github master as of today, February 25th.

We have proof of concept code, that can be provided if needed.

We leave decision about disclosure and timeline of this issue entirely to you. We do not intend to disclose it at all, however we will appreciate credit when disclosed.

A fix for this vulnerability was today published to our github as a part of a single huge commit and is unlikely to be noticed by anyone.


## Releases Affected:

  * current git master

## Impact

Tricking an exchange that she has deposited a huge sum of XMR and therefore effectively stealing from the said exchange.

## Attachments
No attachments
