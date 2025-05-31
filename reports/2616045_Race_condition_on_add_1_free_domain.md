# Race condition on add 1 free domain

## Report Details
- **Report ID**: 2616045
- **URL**: https://hackerone.com/reports/2616045
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-07-22T11:58:05.469Z
- **Disclosed**: 2025-05-09T18:59:17.285Z

## Reporter
- **Username**: root_geek280
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
When a website/provider provide free account they will give the user some feature that limited from access, but if we using race condition vulnerability an user can create/bypass limitation from the provider

## Platform(s) Affected:
wordpress.com

## Steps To Reproduce:
1. create free account in Gravatar
2. login the account, select claim free custom domain below My profile
██████████
3. after click claim domain you will redirect to
https://wordpress.com/start/domain-for-gravatar/domain-only?search=yes&new=(gravatar domain)
4. complete the payment until you get this endpoint
public-api.wordpress.com/rest/v1.1/me/transactions?
██████
5. create group request and duplicate until 1-15 times
6. change parameter "meta" to any other name
7. after complete changing meta, send all request with Group (parallel)
████
8. free domain will buy more than 1

████████


## Supporting Material/References:
detail PoC on the attachment below

## Impact

user can create more than 1 free domain in wordpress

## Attachments
No attachments
