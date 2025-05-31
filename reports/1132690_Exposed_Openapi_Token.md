# Exposed Openapi Token

## Report Details
- **Report ID**: 1132690
- **URL**: https://hackerone.com/reports/1132690
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-03-23T01:49:36.804Z
- **Disclosed**: 2021-05-07T16:00:37.064Z

## Reporter
- **Username**: johnjhacking
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
**Summary**
While looking for secrets, I noticed that Developers had removed a swagger spec draft. The URL had a committed token in the history of multiple project files:
ui/core/src/api/transactionsService.ts
ui/core/src/api/tendermintService.ts
ui/core/src/api/stakingService.ts
ui/core/src/api/slashingService.ts
ui/core/src/api/sifdistService.ts
ui/core/src/api/bankService.ts
...etc, etc

**Steps To Reproduce**
1. Look at the file history of the the github ui/core/src/api and check for secrets. I will provide exposed file history if requested further.

**Proof**
 https://raw.githubusercontent.com/Sifchain/sifnode/c1bb5a268da8b519d0fc90f81fa194d31c0f82b3/api/openapi/swagger.yml?token=AAJSXWM6CDXYAEETSC6BJ2S7Q2JLS

## Impact

An attacker can utilize the token on the api.sifchain.finance API

## Attachments
No attachments
