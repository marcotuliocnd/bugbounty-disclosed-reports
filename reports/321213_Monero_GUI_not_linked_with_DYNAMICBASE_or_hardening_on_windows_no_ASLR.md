# Monero GUI not linked with /DYNAMICBASE or hardening on windows, no ASLR

## Report Details
- **Report ID**: 321213
- **URL**: https://hackerone.com/reports/321213
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-03-01T20:21:49.113Z
- **Disclosed**: 2018-03-18T00:46:08.663Z

## Reporter
- **Username**: flxflndy_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
**Summary:**
The monero daemon is compiled and linked without ASLR, at least on windows. This security hardening feature should be enabled in order to make exploiting of this service harder.

**Description:** 
See above. 

## Releases Affected:

  * At least v0.11.1.0 (probably more) / Tested on Windows 8.1

## Steps To Reproduce:

  1. Start the monero-gui and monero daemon on windows
  2. Start Process Explorer https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer 
  3. Check ASLR under "select columns"
  4. See that ASLR is not activated for this process.

## Supporting Material/References:

  * I've attached a screenshot of the sysinternals tool on my machine.

## Impact

Exploiting code reuse attacks is alot easier without this feature. 
This might impact future bug bounty payouts because people can't exploit reliable bugs to get code execution :)

## Attachments
- monero-aslr.png
