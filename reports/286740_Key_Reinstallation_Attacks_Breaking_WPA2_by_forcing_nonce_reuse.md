# Key Reinstallation Attacks: Breaking WPA2 by forcing nonce reuse

## Report Details
- **Report ID**: 286740
- **URL**: https://hackerone.com/reports/286740
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-11-02T22:08:43.565Z
- **Disclosed**: 2017-11-03T00:37:55.335Z

## Reporter
- **Username**: vanhoefm
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Full background information is at [krackattacks.com](https://www.krackattacks.com) and all detailed information can be found in our [research paper](https://papers.mathyvanhoef.com/ccs2017.pdf).

# Key Reinstallation Attack: 4-way handshake example

We use the 4-way handshake to illustrate the idea behind key reinstallation attacks (CVE-2017-13077).
Note that in practice, all protected Wi-Fi network rely on the 4-way handshake to derive a fresh session key (PTK) from some shared secret.

### Step 1. Channel-based man-in-the-middle and initial handshake messages:

* The adversary clones the access point (AP) on a different channel. Say the real AP is on channel 6, and it will be cloned on channel 1.
* The adversary uses Channel Switch Announcements to force victims into connecting to the cloned AP on channel 1.
* The adversary forwards the first three message of the 4-way handshake between the client and AP (i.e. the adversary fowards frames over the different channels).
* After the client receives message 3 of the handshake, it will install the fresh session key (PTK) for the first time.

### Step 2. Triggering a key reinstallation:

* The attacker does not forward message 4 of the handshake to the AP, effectively blocking it.
* As a result, the AP will retransmit message 3 to the client.
* After the client receives message 3, it responds with message 4. In practice all clients encrypt this retransmitted message 4 at the link layer. Note that it's encrypted because message 4 an ordinary data frame, and the victim has already installed the session key to encrypt data frames (recall end of step 1). The victim will **use a nonce value of 1 to encrypt** message 4.
* After sending message 4, the client will reinstall the session key. This **resets the transmit nonce** to zero.

### Step 3. Abusing nonce reuse:

* When the client now transmit a normal encrypted data frame, it will increment the nonce counter, and then **reuse the nonce value 1 when encrypting the data frame**.
* We can derive known keystream from the encrypted retransmitted message 4 (recall step 2), and use this to decrypt parts of the just transmitted encrypted data frame.
* Other predictable packets (ARP, DHCP, HTML, and so on) can be used to obtain additional known plaintext and keystream, which can in turn be used to decrypt more and bigger packets.

The above example attack against the 4-way handshake is also illustrated in my [CCS'17 presentation](https://papers.mathyvanhoef.com/ccs2017-slides.pdf).

# Other handshakes

Other Wi-Fi handshakes or features that were found to be vulnerable to key reinstallation attacks are:
- Reinstallation of group keys in the 4-way handshake: CVE-2017-13078 and CVE-2017-13079
- The group key handshake: CVE-2017-13080 and CVE-2017-13081
- The Fast BSS Transition (FT) handshake: CVE-2017-13082
- The PeerKey handshake: CVE-2017-13084
- The Tunneled Direct-Link Setup (TDLS) handshake: CVE-2017-13086
- Handling of Wireless Network Management (WNM) Sleep Mode Response frame: CVE-2017-13087 and CVE-2017-13088.

# Countermeasures

Implementations can be updated to prevent key reinstallation attacks in a backwards-compatible manner.

As an additional mitigation, an access point can also prevent most attacks against vulnerable clients.
In particular, attacks against the 4-way handshake can be prevented by not retransmitting message 3.
Similarly, attacks against the group key handshake can be prevented by not retransmitting message 1 of the group key handshake. Alternatively, the access point can retransmit these two handshake messages using the previously used EAPOL-Key replay counter.

# Additional Contributions

- We helped with writing several [patches for hostap](https://w1.fi/security/2017-1/), which is used in Linux, Android, and several professional APs.
- We wrote most parts of the [patch to OpenBSD](https://ftp.openbsd.org/pub/OpenBSD/patches/6.1/common/027_net80211_replay.patch.sig).
- We created vulnerability test tools to detect if devices are vulnerable. [The Wi-Fi Alliance](https://www.wi-fi.org/news-events/newsroom/wi-fi-alliance-security-update) is using these to [test if new products are affected](https://www.wi-fi.org/security-update-october-2017) or not. These test tools will be released publically once they are stable enough.

## Attachments
No attachments
