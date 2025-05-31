# Hardware Wallets Do Not Check Unlock TIme

## Report Details
- **Report ID**: 817245
- **URL**: https://hackerone.com/reports/817245
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-03-12T00:41:50.915Z
- **Disclosed**: 2021-09-12T08:36:40.539Z

## Reporter
- **Username**: thecharlatan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
## Summary:

The hardware wallet implementations using the monero wallet do not check the unlock time when signing. This allows malware on the user's computer (which the hardware wallet should protect from) to permanently lock-up all the user's funds if the user signs a transaction on the device with a very high unlock time.To provide a scenario for this kind of attack: A disgruntled employee can use this vector to permanently cripple a business' funds.

## Releases Affected:

All releases since inclusion of hardware wallet support.

## Steps To Reproduce:

Reproduction is easy, just create a new wallet with monero-wallet-cli with either Trezor or Ledger as a keystore. Then sign a transaction with locked_transfer and set a high unlock time.

## Supporting Material/References:

I disclosed this vulnerability on 02.02.2020 to both Trezor and Ledger. 
Trezor was able to quickly patch the vulnerability, since they already parsed the unlock time field. They will release this patch beginning of April. No patch for the monero wallet is required in their case.
Ledger has not patched the vulnerability yet. Unlike Trezor, they do not parse the unlock time field in the firmware currently, so their patch might require a change in the monero wallet. The possibility of requiring this patch is the reason why I am raising this report now, such that monero developers can prepare for its inclusion in a point release. I will stick to the 90 day disclosure timeline measured from 02.02.2020 . The Ledger developers have vouched to patch the problem by end of this period.

## Impact

Permanently lock-up a user's hardware wallet funds.

## Attachments
No attachments
