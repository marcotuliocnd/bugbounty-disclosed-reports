#  ETHEREUM_PRIVATE_KEY leaked via Open Github Repository

## Report Details
- **Report ID**: 1133670
- **URL**: https://hackerone.com/reports/1133670
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-03-23T23:24:34.959Z
- **Disclosed**: 2021-05-07T19:52:07.648Z

## Reporter
- **Username**: fozisimi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
## Summary:
GitHub is a truly awesome service but it is unwise to put any sensitive data in code that is hosted on GitHub and similar services as I was able to find internal data as responsible disclosure I wanted to share it like this the only channel to do so, and it's related to your sensitive services uploaded by
User: khdegraaf Last indexed on Mar 17, 2021

##Leak here:

https://github.com/Sifchain/sifnode/blob/develop/.github/workflows/node.yml

==================================================================

CONSENSUS_THRESHOLD: 25
          OPERATOR: "0x627306090abaB3A6e1400e9345bC60c78a8BEf57"
          PAUSER: "0x627306090abaB3A6e1400e9345bC60c78a8BEf57"
          OWNER: "0x627306090abaB3A6e1400e9345bC60c78a8BEf57"
          MNEMONIC: "candy maple cake sugar pudding cream honey rich smooth crumble sweet treat"
          INFURA_PROJECT_ID: "JFSH7439sjsdtqTM23Dz"
          INITIAL_VALIDATOR_ADDRESSES: "0x627306090abaB3A6e1400e9345bC60c78a8BEf57,0xf17f52151EbEF6C7334FAD080c5704D77216b732"
          INITIAL_VALIDATOR_POWERS: "50,50"
          MAINNET_GAS_PRICE: 200000000000
          EROWAN_ADDRESS: "0x0d8cc4b8d15D4c3eF1d70af0071376fb26B5669b"
          ==ETHEREUM_PRIVATE_KEY: "c87509a1c067bbde78beb793e6fa76530b6382a4c0241e5e4a9ec0a0f44dc0d3"==

## Impact

Thanks

## Attachments
No attachments
