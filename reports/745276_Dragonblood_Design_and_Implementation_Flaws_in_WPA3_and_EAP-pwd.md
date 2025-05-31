# Dragonblood: Design and Implementation Flaws in WPA3 and EAP-pwd

## Report Details
- **Report ID**: 745276
- **URL**: https://hackerone.com/reports/745276
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-11-24T10:24:11.406Z
- **Disclosed**: 2020-05-05T20:42:25.951Z

## Reporter
- **Username**: vanhoefm
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Full background information is at [our website](wpa3.mathyvanhoef.com) and detailed information can be found in our [research paper](https://eprint.iacr.org/2019/383).

# Vulnerability Summary

## First Disclosure

Summarized, the Dragonfly handshake of WPA3 and EAP-pwd is supposed to prevent dictionary attacks. However, we discovered design flaws that still enable an adversary to perform dictionary attacks. In particular, we discovered the following design flaws in WPA3 and EAP-pwd:
- Against EAP-pwd, a timing leak exists for all supported elliptic curves. An adversary within range of the victim can induce clients to connect to the adversary's Access Point (AP) and exploit this timing leak. The leaked information can be used to perform a dictionary attack on the password.
- Against WPA3, a similar timing leak is possible when using MODP cryptographic groups.
- Against both EAP-pwd and WPA3, we discovered a cache-based side-channel attack. An adversary that can run unprivileged code on a victim's machine (e.g. through an unprivileged Android app) and can abuse the leaked information to perform a dictionary attack on the password.
- Against a network that supports WPA2 and WPA3 simultaneously, we demonstrated that new WPA3 clients can still be downgraded to WPA2. This means all vulnerabilities of WPA2 still apply.
- Against WPA3 we also discovered a downgrade attack that tricks the client or AP into using a weaker elliptic curve than devices normally would.

We also discovered the following implementation flaws in EAP-pwd and WPA3 products:
- All tested EAP-pwd implementations (FreeRADIUS, Radiator, wpa_supplicant, Hostapd, Intel's iwd, Aruba's EAP-pwd) were vulnerable to Invalid Curve Attacks. An adversary can abuse this to trivially bypass authentication and connect to any network that supports EAP-pwd. This corresponds to CVE-2019-9498, CVE-2019-9499 and CVE-2019-11235.
- The WPA3 implementation of Intel's IWD client was also vulnerable to an invalid curve attack.
- Aruba's EAP-pwd implementation for Windows didn't generate secure random numbers, and this can be abused to create a rogue AP and subsequently man-in-the-middle all traffic of the client.
- Most EAP-pwd implementations were also vulnerable to a reflection attack. Fortunately, this is a more theoretic attack with low practical impact. This corresponds to CVE-2019-9497 and CVE-2019-11234.

## Second Disclosure

After our first disclosure, the Wi-Fi Alliance released security guidelines on how to implement WPA3. Unfortunately, these guidelines still contained flaws. Summarized, we found that:
- Timing-based side-channel attacks against WPA3's Dragonfly handshake remain possible when using Brainpool curves (CVE-2019-13377).
- In FreeRADIUS we found an implementation-specific side-channel that allowed an adversary to gain enough information to perform a dictionary attack. No tedious timing attacks are needed to exploit this side-channel. This corresponds to CVE-2019-13456.

# Updates to WPA3 and EAP-pwd

- The Wi-Fi Alliance released [security guidelines](https://wpa3.mathyvanhoef.com/WPA3_Security_Considerations_20190410.pdf) on how to prevent our attacks in a backwards-compatible manner. Unfortunately, this defence is costly on resource-constrained devices.
- The IEEE is [updating the Dragonfly handshake](https://mentor.ieee.org/802.11/dcn/19/11-19-1173-18-000m-pwe-in-constant-time.docx) to avoid the discovered side-channels. Note that HostAP already has an [experimental implementation](https://w1.fi/cgit/hostap/tree/src/common/sae.c?id=5b50265e133d2ce111211e69d584ba71bf0551e4#n617) of this update.
- [Updates to EAP-pwd](https://tools.ietf.org/html/draft-harkins-eap-pwd-prime-00) are proposed as well but are not yet implemented by any vendors.
- Samsung patched the Galaxy S10 to prevent downgrade attacks to WPA2.

## Impact

The design issues in WPA3 and EAP-pwd allow an adversary to perform dictionary (and brute-force) attacks on the password.

The invalid curve attacks against all EAP-pwd and selected WPA3 implementations allow an adversary to bypass authentication.

The impact of other vulnerabilities is summarized above and also explained on [our website](wpa3.mathyvanhoef.com).

## Attachments
No attachments
