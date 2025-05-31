# Found a url on source code which was disclosing different juicy informations like ip addresses and available endponts

## Report Details
- **Report ID**: 1195432
- **URL**: https://hackerone.com/reports/1195432
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-05-13T10:04:06.465Z
- **Disclosed**: 2021-05-14T15:25:29.993Z

## Reporter
- **Username**: paranoid07
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
## Summary:
I found a link in " https://github.com/Sifchain/sifnode/blob/develop/deploy/rake/cluster.rake" page which was exposing ip adresses and different endpoints which could be missused by hackers. 
Link Is=https://rpc.sifchain.finance/

## Steps To Reproduce:
1. Visit  https://rpc.sifchain.finance/ 

## Supporting Material/References:
{F1299908}
 Sample:
found on https://rpc.sifchain.finance/net_info? 
"remote_ip": "52.215.172.88"
      },
      {
        "node_info": {
          "protocol_version": {
            "p2p": "7",
            "block": "10",
            "app": "0"
          },
          "id": "5a03d7636ad9899e6ffb06ec929cdb9c963d5d3d",
          "listen_addr": "46.137.53.38:26656",
          "network": "sifchain",
          "version": "0.33.9",
          "channels": "4020212223303800",
          "moniker": "sarah",
          "other": {
            "tx_index": "on",
            "rpc_address": "tcp://0.0.0.0:26657"
          }
        },

## Impact

Internal Ip adresses , endpoints and other sensitive info related to company are revealed which can be used by attacker for Bad purpose.Attacker can use those endpoints for further attack

## Attachments
- Screenshot_(83).png
