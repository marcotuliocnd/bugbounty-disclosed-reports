# Leak of Internal IP addresses

## Report Details
- **Report ID**: 673723
- **URL**: https://hackerone.com/reports/673723
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-08-14T15:44:27.994Z
- **Disclosed**: 2021-03-12T15:31:56.472Z

## Reporter
- **Username**: rook1337
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: trint

## Vulnerability Information
## Summary:
The leak of Internal IP Addresses.
IP Addresses:-
   10.6.96.4 
   10.6.136.194
   10.6.127.182  

### Assessment:
[add your assessment of the vulnerability]

## Steps To Reproduce:
        1. Open request page of (graphql2.trint.com)  with "getUser" Operation name.
        2. Remove "authorization: Bearer" line and error will raise.
        3. You can see ("ip":"::ffff:10.6.127.182) and ("data":{"user":null}) in error.
It is happening only on "getUser" operation name.

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]
F555596

## Impact

The leak of Internal IP Addresses will allow the attacker to get more information about the server.

## Attachments
- ipleak1.JPG
