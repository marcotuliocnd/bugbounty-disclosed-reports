# Dynamic fee algorithm doesn't check for zero fee

## Report Details
- **Report ID**: 1981441
- **URL**: https://hackerone.com/reports/1981441
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-05-10T13:44:24.668Z
- **Disclosed**: 2025-05-23T14:25:46.960Z

## Reporter
- **Username**: sech1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
## Summary:
Dynamic fee algorithm `Blockchain::get_dynamic_base_fee` calculates the minimal fee per byte from current median block weight and block reward. The comment in the code says `// min_fee_per_byte = round_up( 0.95 * block_reward * ref_weight / (fee_median^2) )`, so it's supposed to round up the result of the division and never return 0 because the argument of `round_up` is always > 0. But the actual code rounds down when doing divisions and can return `min_fee_per_byte = 0`.

## Releases Affected:
All current versions of Monero (v0.18.x.x)

## Steps To Reproduce:
An attacker could spam the network with transactions until median block weight reaches 42426407 or bigger, at which point `Blockchain::get_dynamic_base_fee` will return 0, allowing 0-fee transactions to be included in mempool and mined. After that, the transaction flood attack will have 0 cost and can continue indefinitely.

## Possible solution

`Blockchain::get_dynamic_base_fee` can check for 0 and return `min_fee_per_byte = 1` to avoid this problem. Since it's not a part of consensus, it can be changed in a point release.

## Impact

An attacker can eventually flood XMR network with transactions essentially for free, resulting in unlimited blockchain growth.

## Attachments
No attachments
