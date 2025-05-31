# Private KEY of crypto wallet

## Report Details
- **Report ID**: 1145581
- **URL**: https://hackerone.com/reports/1145581
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-04-02T19:20:22.518Z
- **Disclosed**: 2021-05-07T16:08:32.681Z

## Reporter
- **Username**: krynos
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
## Summary:

Hello,

I'm writing in order to inform you that in your source code is stored the Private key of your crypto wallet that contains some money, as EOS, FNDR, and more.

Your wallet address is this:

0x627306090abaB3A6e1400e9345bC60c78a8BEf57


## Steps To Reproduce:

The key is stored in "those files" and is:

./.github/workflows/node.yml
./test/integration/.env.ciExample
./test/integration/start-integration-env.sh
./smart-contracts/.env.example
./smart-contracts/Deployment.md
./smart-contracts/.env.ui.example
./ui/core/src/test/utils/accounts.ts

and is this:

ETHEREUM_PRIVATE_KEY="c87509a1c067bbde78beb793e6fa76530b6382a4c0241e5e4a9ec0a0f44dc0d3"


## Supporting Material/References:

I've attached a screenshot of your wallet where you can show some amounts of EOS and other money.

Your can access on it using the site https://www.myetherwallet.com

## Impact

Github code expose the private key of your wallet 0x627306090abaB3A6e1400e9345bC60c78a8BEf57

## Attachments
- wallet.png
