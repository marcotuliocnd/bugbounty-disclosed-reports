# ETHEREUM_PRIVATE_KEY leaked via github

## Report Details
- **Report ID**: 1283605
- **URL**: https://hackerone.com/reports/1283605
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-07-29T18:01:30.950Z
- **Disclosed**: 2021-12-09T17:46:20.458Z

## Reporter
- **Username**: bugkillerak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
ETHEREUM_PRIVATE_KEY 

It is used to sign Ethereum transactions on the Blockchain.

## Steps To Reproduce:
Open this url
https://github.com/Sifchain/sifnode/blob/f96727748e1f44926d3bd72b1021f6c2461dee17/test/integration/start-integration-env.sh



  * POC - screenshot attached

## Impact

It shouldn’t be publicly shared because whoever owns the Private keys can access the funds for that address.
-Private keys are used to create Public addresses using SHA256 hash function.

## Attachments
- Screenshot_(164).png
