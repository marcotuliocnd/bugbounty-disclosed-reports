# Fragmentation and Aggregation Flaws in Wi-Fi

## Report Details
- **Report ID**: 1238470
- **URL**: https://hackerone.com/reports/1238470
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2021-06-19T21:24:25.912Z
- **Disclosed**: 2021-07-23T03:59:49.616Z

## Reporter
- **Username**: vanhoefm
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
I discovered three design flaws in the Wi-Fi standard and widespread related implementation flaws ([see GitHub overview and test tool](https://github.com/vanhoefm/fragattacks#fragattacks-fragmentation--aggregation-attacks)). **Here I'll specifically cover open source software**. These findings have not received bug bounties from other sources.


# Implementation flaws allowing trivial packet injection

- [CVE-2020-26140](https://nvd.nist.gov/vuln/detail/CVE-2020-26140): Accepting plaintext data frames in a protected network. This allows trivial packet injection. On a Linux client, the AWUS036H network card is vulnerable and two out of four Linux-based **home routers** were vulnerable. On **NetBSD access points**, three out of four tested network cards were vulnerable, and on FreeBSD access points, the F5D8053 network card was vulnerable.

- [CVE-2020-26143](https://nvd.nist.gov/vuln/detail/CVE-2020-26143): Accepting fragmented plaintext data frames in a protected network. This allows trivial packet injection. On a **Linux client**, 7 out of 16 network cards were vulnerable. On FreeBSD access points, two out of four tested network cards were vulnerable.

- [CVE-2020-26145](https://nvd.nist.gov/vuln/detail/CVE-2020-26145): Accepting plaintext broadcast fragments as full frames. This allows trivial packet injection. All tested network cards on **NetBSD and FreeBSD access points** were vulnerable. On a Linux client, only the TWFM-B003D network card was vulnerable.

- [CVE-2020-26144](https://nvd.nist.gov/vuln/detail/CVE-2020-26144): Accepting plaintext A-MSDU frames that start with an RFC1042 header with EtherType EAPOL. This allows trivial packet injection. On a Linux client, the AWUS036ACH and TWFM-B003D network cards were vulnerable. All 6 tested **FreeBSD** network cards were vulnerable (both as clients and access points).


# Other implementation vulnerabilities

- [CVE-2020-26139](https://nvd.nist.gov/vuln/detail/CVE-2020-26139): the access point forwards EAPOL frames even if the client isn't yet authenticated. This allows an adversary to perform the aggregation attack (see below) against any client by simply being within radio range (i.e. no social engineering needed). All **NetBSD and FreeBSD access points** were vulnerable, as were two out of four Linux-based home routers.

- [CVE-2020-26146](https://nvd.nist.gov/vuln/detail/CVE-2020-26146): reassembling encrypted fragments with non-consecutive packet numbers. This can be abused to exfiltrate data, under the condition that another device sends fragmented frames. All tested open source Wi-Fi implementations were vulnerable (FreeBSD, NetBSD, FullMAC Linux drivers) except SoftMAC Linux drivers.

- [CVE-2020-26147](https://nvd.nist.gov/vuln/detail/CVE-2020-26147): reassembling mixed encrypted/plaintext fragments. The impact ranges from data exfiltration to packet injection, under the condition that another device sends fragmented frames. All open source Wi-Fi implementations were vulnerable (Linux, FreeBSD, NetBSD, Linux, etc).

- [CVE-2020-26142](https://nvd.nist.gov/vuln/detail/CVE-2020-26142): processing fragmented frames as full frames. This can be abused to inject packets, under the condition that the another device sends fragmented frames, and in most cases requires (minor) social engineering. Among open source platforms, only OpenBSD was vulnerable.

- [CVE-2020-26141](https://nvd.nist.gov/vuln/detail/CVE-2020-26141): not verifying the TKIP MIC of fragmented frames. This can be abused to exfiltrate and inject packets in old WPA1 networks. On Linux, only the NWD6505 and AWUS036ACM network cards were vulnerable.


# Design flaws

1. [Aggregation Attack](https://www.fragattacks.com/#aggregationattack) (CVE-2020-24588): the A-MSDU flag in the plaintext Wi-Fi header is not authenticated. This can be abused, usually in combination with minor social engineering, to inject arbitrary packets to a victim. All 802.11n-compatible open source implementations were vulnerable (Linux, FreeBSD, OpenBSD, etc).

2. [Mixed Key Attack](https://www.fragattacks.com/#mixedkeyattack) (CVE-2020-24587): a receiver will reassemble fragments that were decrypted using different keys. Under very rare conditions this can be abused to exfiltrate data. All open source Wi-Fi implementations were vulnerable (FreeBSD, NetBSD, Linux, etc) except OpenBSD because it doesn't support fragmentation.

3. [Fragment Cache Attack](https://www.fragattacks.com/#fragcacheattack) (CVE-2020-24586): a receiver will not clear fragments from memory when reconnecting or reassociating to a Wi-Fi network. Under the right conditions this can be abused to exfiltrate data. Under very rare conditions it can also be abused to inject arbitrary packets towards clients. Most open source Wi-Fi implementations were vulnerable (FreeBSD, Linux, etc) with the exception of OpenBSD and NetBSD.

## Impact

As indicated above, there are two impacts:

1. **Arbitrary packet injection**: this clearly breaks the security of Wi-Fi. A first practical example is that this can be abused to make a client use a malicious DNS server to subsequently intercept all traffic (and perform SSL stripping attacks). As second practical example, the adversary can abuse packet injection to "punch holes in the NAT" to then directly attack internal devices (e.g. exploit internet-of-things devices or exploit BlueKeep against outdated Windows 7 machines). See [this addendum](https://papers.mathyvanhoef.com/fragattacks-overview.pdf) for the technical details or [watch three demos](https://www.youtube.com/watch?v=88YZ4061tYw).

2. **Data exfiltration**: this is only possible if another device sends fragmented frames. In practice this is rare unless Wi-Fi 6 is used. Additionally, the data can only be exfiltrated if no higher-layer encryption is used (i.e. TLS will prevent data exfiltration).


Finally, I've also contributed patches to these open source projects:

- [Linux](https://lwn.net/ml/linux-wireless/20210511200110.30c4394bb835.I5acfdb552cc1d20c339c262315950b3eac491397@changeid/): I wrote patches to prevent all attacks. Additional defense-in-depth and driver-specific patches were added by Linux developers.

- [Wi-Fi standard](https://mentor.ieee.org/802.11/dcn/21/11-21-0816-00-000m-on-a-msdu-addressing.docx): I'm helping to update the 802.11 standard to fix the design flaws (starting with A-MSDU fixes).

- [FreeBSD](https://bugs.freebsd.org/bugzilla/buglist.cgi?quicksearch=ALL%20reporter%3Avanhoef): I wrote patches to mitigate vulnerabilities in FreeBSD. These patches are now under review [[1](https://reviews.freebsd.org/D30665), [2](https://reviews.freebsd.org/D30664), [3](https://reviews.freebsd.org/D30663)].

- [NetBSD](https://gnats.netbsd.org/cgi-bin/query-pr-single.pl?number=56204): I submitted initial patches. The remaining patches are in progress.

- [OpenBSD](https://github.com/openbsd/src/commit/e12e039eea57d78605e08542b570756b41a2a610): I reviewed patches related to A-MSDU vulnerabilities resulting in more secure patches.

## Attachments
No attachments
