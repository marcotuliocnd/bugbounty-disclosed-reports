# ETHEREUM_PRIVATE_KEY leaked 

## Report Details
- **Report ID**: 1183269
- **URL**: https://hackerone.com/reports/1183269
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2021-05-03T20:09:07.344Z
- **Disclosed**: 2021-05-07T16:04:28.047Z

## Reporter
- **Username**: dexter34
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
## Summary:
I found  below private key for ethereum wallet leaked via public code in github repository  
```
ETHEREUM_PRIVATE_KEY="c87509a1c067bbde78beb793e6fa76530b6382a4c0241e5e4a9ec0a0f44dc0d3"
```
## Steps To Reproduce:
You can find private key via below link :
>https://github.com/Sifchain/sifnode/blob/5d222e51f10665322ddb5301a4eb54df37974310/smart-contracts/Deployment.md

## Impact :
This private key for ethereum wallet  allow to someone to send Ether from the address to another address  .

I didn't try anything with this key to avoid violation policy  of program .

## Impact

ETHEREUM_PRIVATE_KEY leaked

## Attachments
No attachments
