# Brute Force of fabric-ca server admin account

## Report Details
- **Report ID**: 411364
- **URL**: https://hackerone.com/reports/411364
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-09-19T07:34:01.745Z
- **Disclosed**: 2022-08-06T17:36:44.655Z

## Reporter
- **Username**: xiaoc
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: hyperledger

## Vulnerability Information
## fabric-ca server
- Default configuration maxenrollments value -1(enable outside enrollment)
- Listening 0.0.0.0:7054(easily discoved and can be reached)
- No limit to wrong password try
Above conditions result in brute force to CA server admin account

## Impact

## Attack gain a high-level permissioned account to permissioned network and can add\delete\update\query

## Attachments
- Poc_of_Brute_Force.docx
