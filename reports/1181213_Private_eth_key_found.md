# Private eth key found

## Report Details
- **Report ID**: 1181213
- **URL**: https://hackerone.com/reports/1181213
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2021-04-30T14:03:21.563Z
- **Disclosed**: 2021-06-10T15:00:17.485Z

## Reporter
- **Username**: fle_xxx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
Hello, team! 

Found private ethereum key at file: 
https://github.com/Sifchain/sifnode/blob/develop/smart-contracts/.env.example 

This key points to wallet balance: 
{F1284232}

As I understood, private key allows to spend this coins, so it may need to be masked or hidden.

## Impact

eth private key disclosure

## Attachments
- balance.jpg
