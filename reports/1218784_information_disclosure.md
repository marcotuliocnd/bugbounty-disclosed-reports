# information disclosure

## Report Details
- **Report ID**: 1218784
- **URL**: https://hackerone.com/reports/1218784
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2021-06-07T03:50:17.853Z
- **Disclosed**: 2021-12-09T17:48:17.369Z

## Reporter
- **Username**: hacker13377331
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
Hi team 

during github recon i find something and I dont know what access it has,  but still i though it would be a good idea to share this finding with you in case it can be used in a way that i dont know.

what i find 

link : https://github.com/Sifchain/sifnode/blob/30f0c45720b964342f3011c124c79c66c4c01a6b/deploy/rake/cluster.rake
      create_test_secret = `kubectl exec --kubeconfig=./kubeconfig -n vault -it vault-0 -- vault kv put kv-v2/staging/test username=test123 password=foobar123`

+
also i find this link 

http://rpc.sifchain.finance/ 

when i open it i find these endpoints 

Available endpoints:

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


and when i open one of this  i find 

{
  "jsonrpc": "2.0",
  "id": -1,
  "result": {
    "node_info": {
      "protocol_version": {
        "p2p": "7",
        "block": "10",
        "app": "0"
      },
      "id": "b2063fd8e35d1f699a7fab506ef2eb76366051c0",
      "listen_addr": "34.228.72.160:26656",
      "network": "sifchain",
      "version": "0.33.9",
      "channels": "4020212223303800",
      "moniker": "helen",
      "other": {
        "tx_index": "on",
        "rpc_address": "tcp://0.0.0.0:26657"
      }
    },
    "sync_info": {
      "latest_block_hash": "15E4E94C0C11491EFB21E1C41D6532B045BF38F158A41A16A96D249234F65A2A",
      "latest_app_hash": "99B36B8F46BAA06D6E33E0CA6B3E8C000F619758E92A3B4FAFB72AE628E13E1F",
      "latest_block_height": "1767705",
      "latest_block_time": "2021-06-07T03:47:41.661876769Z",
      "earliest_block_hash": "A2D20EE2550E2D962A5ADD95D3CEB2838ECCD622ED2A6A4F47F3F05D4307208C",
      "earliest_app_hash": "",
      "earliest_block_height": "1",
      "earliest_block_time": "2021-02-11T11:59:14.685903388Z",
      "catching_up": false
    },
    "validator_info": {
      "address": "30E8474151D3C6A97BFB942D512317DAF22B9DAD",
      "pub_key": {
        "type": "tendermint/PubKeyEd25519",
        "value": "ubYpBmPNyJFZi401nuYcYPyJcjCpLsPsTMkmunRCJT8="
      },
      "voting_power": "0"
    }
  }
}

## Impact

again I dont know what access it has,  but still i though it would be a good idea to share this finding with you in case it can be used in a way that i dont know.

## Attachments
- 2.png
- 1_.png
