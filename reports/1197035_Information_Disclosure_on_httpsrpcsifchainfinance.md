# Information Disclosure on https://rpc.sifchain.finance/

## Report Details
- **Report ID**: 1197035
- **URL**: https://hackerone.com/reports/1197035
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-05-14T07:31:48.923Z
- **Disclosed**: 2021-05-15T04:04:17.004Z

## Reporter
- **Username**: bringing2021
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
Description:
Hi team,
I see the subdomain https://rpc.sifchain.finance/  .
And I visited this subdomain it contains  many  endpoints.

Affected URLs:
https://rpc.sifchain.finance/

Poc Available endpoints:
Endpoints that require arguments:
//rpc.sifchain.finance/abci_info?
//rpc.sifchain.finance/abci_query?path=_&data=_&height=_&prove=_
//rpc.sifchain.finance/block?height=_
//rpc.sifchain.finance/block_by_hash?hash=_
//rpc.sifchain.finance/block_results?height=_
//rpc.sifchain.finance/blockchain?minHeight=_&maxHeight=_
//rpc.sifchain.finance/broadcast_evidence?evidence=_
//rpc.sifchain.finance/broadcast_tx_async?tx=_
//rpc.sifchain.finance/broadcast_tx_commit?tx=_
//rpc.sifchain.finance/broadcast_tx_sync?tx=_
//rpc.sifchain.finance/commit?height=_
//rpc.sifchain.finance/consensus_params?height=_
//rpc.sifchain.finance/consensus_state?
//rpc.sifchain.finance/dump_consensus_state?
//rpc.sifchain.finance/genesis?
//rpc.sifchain.finance/health?
//rpc.sifchain.finance/net_info?
//rpc.sifchain.finance/num_unconfirmed_txs?
//rpc.sifchain.finance/status?
//rpc.sifchain.finance/subscribe?query=_
//rpc.sifchain.finance/tx?hash=_&prove=_
//rpc.sifchain.finance/tx_search?query=_&prove=_&page=_&per_page=_&order_by=_
//rpc.sifchain.finance/unconfirmed_txs?limit=_
//rpc.sifchain.finance/unsubscribe?query=_
//rpc.sifchain.finance/unsubscribe_all?
//rpc.sifchain.finance/validators?height=_&page=_&per_page=_

And visit every individual link it contain a sensitive information.
So I will  submitted as a bug report.

Here is the poc screenshot:
{F1300962}

## Impact

Sensitive Information  Disclosed via this subdomain.

## Attachments
- poc_screenshot.png
