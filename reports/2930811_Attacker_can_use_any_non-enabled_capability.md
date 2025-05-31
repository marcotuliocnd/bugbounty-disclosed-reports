# Attacker can use any non-enabled capability

## Report Details
- **Report ID**: 2930811
- **URL**: https://hackerone.com/reports/2930811
- **State**: Closed
- **Severity**: low
- **Submitted**: 2025-01-10T12:59:36.282Z
- **Disclosed**: 2025-01-15T20:33:51.232Z

## Reporter
- **Username**: julianor
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: cosmos

## Vulnerability Information
An attacker can deploy a `cosmwasm` contract  on a chain and execute _any_ action on that chain,  even when the executing chain does not allow  that capability. This issue stems from a naive implementation  of capabilities and misleading documentation.

This goes against the `Capabilites` description 
in `CAPABILITIES.md` (https://github.com/CosmWasm/cosmwasm/blob/main/docs/CAPABILITIES.md):

```
The contract defines required capabilities. The environment defines its capabilities. If the required capabilities are all available, the contract can be used. 
```

We show that even if the required capabilities are not available, the capability can be used.

### Steps to reproduce 

 * Assume a chain that announced no capabilities to disallow contracts from executing certain paths.  
* The chain does allow users to execute those paths via regular non-wasm messages. 

1. The attacker comments out the generation of the capabilities-string in the [cosmwasm compiler](https://github.com/CosmWasm/cosmwasm//blob/3a6093936520e9a1559423b50aa911ed9b836b3c/packages/std/src/exports.rs#L40). 
2. The attacker deploys the contract to the chain 
3. The chain will allow the upload as the `requires_*` string is **not** present. 
4. The attacker can execute any action on the chain.

### Workarounds 

None known. `capabilities`  should be checked at runtime too. In particular, the `DefaultMessageHandler` should  check for a capability before dispatching a message.

## Impact

A blockchain that leverages `Capabilities` restrictions to prevent contracts from executing specific actions is open to attacks. The severity of the impact on Integrity and Availability depends on the particular features of the blockchain's implementation, and this impact can potentially be **critical.**

## Attachments
No attachments
