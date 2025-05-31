# OpenSSL engines can be used to bypass and/or disable the permission model

## Report Details
- **Report ID**: 1954535
- **URL**: https://hackerone.com/reports/1954535
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-04-19T10:00:30.773Z
- **Disclosed**: 2023-06-22T11:45:34.136Z

## Reporter
- **Username**: tniessen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:** Node.js 20 allows loading arbitrary OpenSSL engines even when the permission model is enabled, which can bypass and/or disable the permission model.

**Description:** The permission model implementation permits loading arbitrary native code, e.g., through `crypto.setEngine()`, even when native addons are disallowed, which is the default configuration. Not only can this code bypass the permission system, it can also disable the permission system entirely, effectively allowing JavaScript code to escalate its own privileges.

## Steps To Reproduce:

  1. Enable the permission model.
  2. Call, for example, `crypto.setEngine()` with a compatible OpenSSL engine.
  3. Arbitrary code execution occurs, unaffected by the permission model.

## Impact

The permission model is supposed to restrict the capabilities of running code. However, exploiting this vulnerability allows an attacker to easily bypass the permission model entirely. The OpenSSL engine can, for example, disable the permission model in the host process, and subsequently executed JavaScript code will be unaffected by the previously enabled permission model. This allows running JavaScript code to effectively elevate its own permissions.

## Attachments
No attachments
