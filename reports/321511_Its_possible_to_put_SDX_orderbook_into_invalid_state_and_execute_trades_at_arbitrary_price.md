# It's possible to put SDX orderbook into invalid state and execute trades at arbitrary price

## Report Details
- **Report ID**: 321511
- **URL**: https://hackerone.com/reports/321511
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-03-03T05:43:51.105Z
- **Disclosed**: 2018-10-14T14:56:53.085Z

## Reporter
- **Username**: nebolsin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stellar

## Vulnerability Information
stellar-core improperly handles creation of a buy offer which crosses existing sell offers (immediate execution) but can only be filled partially due to a trustline limit on the source account. This makes it possible to create a valid offer to buy any custom asset at higher price than existing sell offers. If counter is not native, it's also possible to create a sell offer lower than existing bids.

Steps to reproduce
-------------------
1. Choose any asset ABC with non-empty orderbook ABC-XLM
2. Create and fund account `H`, then set a trustline for ABC with limit 1
3. Choose arbitrary price `P` higher than existing best ask price `Pa`
4. Prepare the tx to sell `P` XLM for ABC  at price P and then increase the trustline limit to 2, sign it with H secret key and send to the network.

```
Transaction(
  source = H, 
  operations = [
    manageOffer(selling=XLM, buying=ABC, amount=P, price=P, offerId=0),
    changeTrust(asset=ABC, limit=2)
  ]
)
```

Account `H` will receive 1 ABC balance and an offer to sell `(P - Pa)` XLM for ABC will be created at price P.

Order book is now in invalid state and contains crossing offers, so `max(bidPrice) > min(askPrice)`. Next offer to sell ABC for XLM with price lower than P will claim our offer and result in a trade at  price P.

Examples
----------

F268790: Invalid bid created by exploiting this vulnerability. Account with a trustline for BUG asset (balance=500, limit=501) posted an offer to sell 100XLM to buy BUG at price 100 XLM per BUG. Result: account bought 1 BUG from the best ask at 9 XLM per BUG, and an offer to sell the remaining 91XLM at price 100 was saved into the orderbook.

F268791: Real case on a public network on MOBI-XLM traiding pair happened to some user (this is where I noticed the anomaly in trade history and started investigation). Relevant ledgers 16494494 - 16494512.

## Impact

Attacker could exploit this behaviour to mess up the orderbook, trade history and chart for any trading pair on Stellar Distributed Exchange. 

For example, it's possible (and very easy) to create a bot which will constantly create an bid at arbitrary high price P and immediately sell into this bid from another account, making last ticker price always equal P, despite that there're sell offers at a lower price. 

This will make OHLC chart analysis useless because high price will be P on every tick. It could also confuse other market participants by creating the impression that P is the fair price for the asset.

## Attachments
- SDX_invalid_bid_.png
- MOBI-XLM_trade_history.png
