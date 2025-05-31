# Trusted daemon check fails when proxied through torsocks or proxychains

## Report Details
- **Report ID**: 361269
- **URL**: https://hackerone.com/reports/361269
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-06-03T08:02:27.484Z
- **Disclosed**: 2018-08-02T00:26:29.075Z

## Reporter
- **Username**: equim
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
**Summary:**
If torsocks(1) or proxychains(1) is enforced when using Monero wallet with a remote node without explicit `--untrusted-daemon` arguments given, the application will assume the daemon is trusted.

**Description:**
By default, the wallet checks if the daemon address can be trusted by calling `tools::is_local_address` when `--trust-daemon` is not set. However, if the process is proxied through torsocks(1) or proxychains(1), which resolves onion addresses into a loopback address that is handled by them internally, `is_local_address` will return `true` on such address, while the actual node should be considered untrusted.

This issue may sound trivial and I also noticed a new argument `--untrusted-daemon` has been added in commit [c4907d24cb32129ee52a53711547c5d54960c431](https://github.com/monero-project/monero/commit/c4907d24cb32129ee52a53711547c5d54960c431), but not all users using a remote node with torsocks or proxychains are aware of this. Essentially, we can't really tell if the address is really local, and current judgement of it doesn't make a sufficient condition that the daemon can be trusted.

## Releases Affected:
* Monero CLI wallet (@master)
* Monero GUI wallet (@master)

## Steps To Reproduce:
1. Run the CLI wallet with `torsocks monero-wallet-cli --daemon-address zdhkwneu7lfaum2p.onion:18099`
1. Authenticate the wallet and sync.
1. Send command `rescan_bc`, which should be available only if the daemon is trusted.
1. The command executed successfully.

## Supporting Material/References:
None

## Possible Solutions:
1. Add an extra condition in src/common/util.cpp function is_local_address to judge if the daemon address ends with .onion or .i2p etc..
1. Prompt the user explicitly if the daemon can be trusted.

## Impact

Possible private data disclosure to the untrusted remote node.

## Attachments
No attachments
