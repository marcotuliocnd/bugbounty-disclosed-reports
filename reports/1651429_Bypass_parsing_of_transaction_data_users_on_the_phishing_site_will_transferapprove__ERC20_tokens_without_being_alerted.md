# Bypass parsing of transaction data, users on the phishing site will transfer/approve  ERC20 tokens without being alerted

## Report Details
- **Report ID**: 1651429
- **URL**: https://hackerone.com/reports/1651429
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-07-27T11:47:59.589Z
- **Disclosed**: 2023-04-10T19:23:57.284Z

## Reporter
- **Username**: ronnyx2017
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: metamask

## Vulnerability Information
## Summary:
There are still a lot of valuable erc20 tokens compiled with solc < 0.5.0 on the eth mainnet. The methods compiled with Solc below 0.5.0 will not check if the length of the input calldata matches the params types. It will load the calldata as long as the params types need, regardless of the actual input length. And the insufficient parts will be read as byte(00). 

Metamask can't parse these unusual length transaction data like normal. For example, delete the last byte of the input data:

A normal transfer call data:
```
sighash ->          0xa9059cbb
address to ->       000000000000000000000000C588e338FdBB2CC523a1177f3D18e87FF5A16a6b
uint256 value ->    0000000000000000000000000000000000000000000000000000000000989700  ->  10000128
```
Evil call data:
```
sighash ->          0xa9059cbb
address to ->       000000000000000000000000C588e338FdBB2CC523a1177f3D18e87FF5A16a6b
uint256 value ->    00000000000000000000000000000000000000000000000000000000009897  
```

When users connect to a phishing site, attack can trigger a token transfer or approve transaction without alerting users to the token amount. 

## Steps To Reproduce:

I fork the metamask test dapp repo as a exp demo. {F1840812}

1. cd in the dist, and setup a http server, for example run `static-server . -z --port 9011`.
2. open in the browser and connect with metamask ext at the Rinkeby network.
3. Click the button `Create Token` will deploy a erc20 token with compiler solc 0.4.26. 
contract source code: {F1840809}

{F1840801}

4. After contract deploying, click `Transfer Tokens`, metamask will show its a normal contract call without showing send to address, send amount and token symbol.

{F1840802}

transfer send data hex:

{F1840803}

Transfer event log:

{F1840800}

5. Click `Approve Tokens`, lack of prompt like transfer.

{F1840799}

## Impact

The attacker can induce the victims to send/approve any number of tokens without knowing it.

## Attachments
- 18.png
- approve.png
- event.png
- token.png
- transfer.png
- transfer_hex.png
- TokenERC20_pure.sol
- dist.tar.gz
