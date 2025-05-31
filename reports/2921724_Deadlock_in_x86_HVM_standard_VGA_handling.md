# Deadlock in x86 HVM standard VGA handling

## Report Details
- **Report ID**: 2921724
- **URL**: https://hackerone.com/reports/2921724
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2025-01-03T22:22:00.514Z
- **Disclosed**: 2025-03-07T20:37:45.934Z

## Reporter
- **Username**: stonksy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
### Overview

This vulnerability has been reported to the Xen project maintainers in mid October 2024. The Xen project has acknowledged the vulnerability, published patches and released an advisory as well as a CVE, see: https://xenbits.xen.org/xsa/advisory-463.html

### Vulnerability

The hypervisor contains code to accelerate VGA memory accesses for HVM guests, when the (virtual) VGA is in "standard" mode. Locking involved there has an unusual discipline, leaving a lock acquired past the return from the function that acquired it. This behavior results in a problem when emulating an instruction with two memory accesses, both of which touch VGA memory (plus some further constraints which aren't relevant here). When emulating the 2nd access, the lock that is already being held would be attempted to be re-acquired, resulting in a deadlock. This deadlock was already found when the code was first introduced, but was analysed incorrectly and the fix was incomplete. Analysis in light of the new finding cannot find a way to make the existing locking discipline work. In staging, this logic has all been removed because it was discovered to be accidentally disabled since Xen 4.7. Therefore, we are fixing the locking problem by backporting the removal of most of the feature. Note that even with the feature disabled, the lock would still be acquired for any accesses to the VGA MMIO region.

Attached is the PoC that I utilized for the original report of the vulnerability to the Xen maintainers. It was tested on Xen version 4.19.

## Impact

An attacker executing code in ring0 inside of an unprivileged x86-HVM-DomU can trigger a deadlock in the host hypervisor, resulting in a Denial of Service of all other Domains running under the Hypervisor, including the hypervisor itself.
"Xen versions 4.6 through 4.19 are vulnerable." as per the referenced XSA.
The CVE database (https://nvd.nist.gov/vuln/detail/CVE-2024-45818) contains a CVSS v3.x rating of: 6.5 Medium.

## Attachments
- poc-stdvga-io-deadlock.tar.gz
