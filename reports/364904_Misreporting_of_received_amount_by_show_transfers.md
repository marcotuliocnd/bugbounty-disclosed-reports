# Misreporting of received amount by show_transfers

## Report Details
- **Report ID**: 364904
- **URL**: https://hackerone.com/reports/364904
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-06-12T06:56:21.516Z
- **Disclosed**: 2018-08-02T00:26:01.794Z

## Reporter
- **Username**: moneromooo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
**Summary:**

A sender may cause show_transfers to report a higher amount that was actually sent on the recipient's show_transfers output.

**Description:** 

Due to a flaw in process_new_transaction in wallet2.cpp, if the tx pubkey is present multiple times, it will decode outputs correctly as many times, and add up the amounts. This means the final amount reported by show_transfers will be the actual amount received multiplied by the number of duplicate tx pubkeys present in the transaction extra field.

Probably does not work if the recipient expects an integrated address, since someone stripping the payment id and contacting support would be unlikely, so priming the exchange to be suspicious.

This was found by investigating a bug report: https://github.com/monero-project/monero/issues/3983.

A simple patch fixes this: keeping track of pubkeys already scanned for, and skipping those that were already scanned.

## Releases Affected:

Current master and release versions.

## Steps To Reproduce:

1. duplicate the "add_tx_pub_key_to_extra(tx, txkey_pub);" line as many times as wanted in src/cryptonote_core/cryptonote_tx_utils.cpp
2. send a transaction to an exchange, without payment id (so it doesn't get processed automatically)
3. give the tx details to the support person, telling them to check show_transfers for the amount

## Supporting Material/References:

Sending wallet sending 5 (difficulty was set to 100 for ease of mining on an offline testnet):

[wallet 9yvGzy]: transfer 9zcJy2vKeDzCWJXgDApGP3ee1YJvUNWS7UQ9Vn33HT4aSyXKrE9Fs2YCCtGMo7NbuE7zzvYZADkU3SgScqxkkLwnNR1wJdn 5

Transaction 1/1:
Spending from address index 0
Sending 5.000000000000.  The transaction fee is 0.000902370000
Transaction 1/1: txid=<a99c5017037039466f3191940fb03d234b23716b6d135ba01154ebc34bf95b00>
Input 1/1: amount=1000.000000000000
Originating block heights:  877928 920324 968699 1026359 *1055454 1116950 1120914
|_____________________________________________________________o__o___o___o_*___o|


Is this okay?  (Y/Yes/N/No): y
Transaction successfully submitted, transaction <a99c5017037039466f3191940fb03d234b23716b6d135ba01154ebc34bf95b00>
You can check its status by using the `show_transfers` command.
[wallet 9yvGzy]: start_mining 1
Mining started in daemon
[wallet 9yvGzy]: stop_mining
Mining stopped in daemon
Height 1121390, txid <3ccb5e289b34e03a72319ac2ee8058e2cddffc73dfcdc1ac21a6155d37614a49>, 7.520434042934, idx 0/0
Height 1121390, txid <a99c5017037039466f3191940fb03d234b23716b6d135ba01154ebc34bf95b00>, 994.999097630000, idx 0/0
Height 1121390, txid <a99c5017037039466f3191940fb03d234b23716b6d135ba01154ebc34bf95b00>, spent 1000.000000000000, idx 0/0
Height 1121391, txid <1b7ecae0238c030486f073480d6431fe5e5958ad59b70b5dee6dec2d05a90259>, 7.519517330565, idx 0/0
Height 1121392, txid <a38f31c5d7257fa803417d9055124627567ea86c7b2c5d2456dbeeb89bc2c288>, 7.519502988224, idx 0/0
[wallet 9yvGzy]: get_tx_key a99c5017037039466f3191940fb03d234b23716b6d135ba01154ebc34bf95b00
Tx key: d8c626596898013ee57aee1e8c974408cd153ea6ef64b44cb9d888730434fc00

Recipient wallet receiving the tx (it is set up to use millinero as unit, hence the x1000), all is good:

[wallet 9zcJy2]: refresh
Starting refresh...
Height 1121390, txid <a99c5017037039466f3191940fb03d234b23716b6d135ba01154ebc34bf95b00>, 5000.000000000, idx 0/0
Refresh done, blocks received: 3                                

And yet, show_transfers reports 20 monero (20k millinero):

 1121390     in      04:44:06 AM      20000.000000000 a99c5017037039466f3191940fb03d234b23716b6d135ba01154ebc34bf95b00 0000000000000000 0 - 


Note that check_tx_key will show the correct amount, so this is not a sure fire way if the exchange support person is vigilant and asks for such a proof.

## Impact

Scamming a recipient of a lot of monero (up to about 8k times more than sent). Given exchanges using payment ids are used to people forgetting them and having to credit manually, they're likely to wave this through more easily.

## Attachments
No attachments
