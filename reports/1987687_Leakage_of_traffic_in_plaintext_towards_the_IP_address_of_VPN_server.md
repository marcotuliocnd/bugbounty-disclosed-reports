# Leakage of traffic in plaintext towards the IP address of VPN server

## Report Details
- **Report ID**: 1987687
- **URL**: https://hackerone.com/reports/1987687
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-05-15T06:40:45.151Z
- **Disclosed**: 2024-11-08T12:02:23.269Z

## Reporter
- **Username**: vanhoefm
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mozilla

## Vulnerability Information
## Disclosure and Deviation of T&Cs

This finding is part of a multi-party coordinated disclosure on VPN security. We plan to publicly disclose relevant findings around July/August 2023. Please don't give a bug bounty if you disagree with the eventual public disclosure, we will still be happy to discuss details even without a bounty. Note that it's OK for us if you already release updated binaries before the coordinated disclosure as long as the details of the vulnerability are not mentioned. If you use the information in this report we assume this will be OK. Happy to discuss details.

For context, we tested more than 66 VPNs, meaning your VPN is just one of the many VPNs we tested, so there won't be an explicit focus on it during disclosure. We also plan to contact CERT/CC to reach other VPN companies for similar vulnerabilities.

## Summary

As part of a larger study on VPN security we found that Mozilla VPN on Linux and Android sends traffic to the IP address of the current VPN server in plaintext.  The impact is low, but it might still be abused to track/deanonymize users and it can have reputational damage since it will cause users to question whether traffic is really encrypted. There is also a hypothetical risk of leaking arbitrary traffic if combined with DNS spoofing.

For instance, in one of our tests, the VPN client was connected to a VPN server at `SERVERIP`. When then visiting `http://<SERVERIP>` in a browser, the resulting TCP connection would be initiated outside the VPN tunnel, i.e., the TCP SYN packet will be sent in plaintext. When an adversary can trick a user into visiting this IP address, the packets sent in plaintext can then be abused to track and deanonymize users.


## Steps to Reproduce

Manual steps:

1. Enable the VPN connection.
2. Identify the IP address of the VPN server. In a real attack, an adversary can collect all VPN server IP addresses and try them all. Or the adversary can sniff traffic to identify the server being used.
3. In the browser visit `http://<SERVERIP>/`. In a real attack, the victim can be tricked into visiting a URL that resolves to this IP address.
4. In Wireshark use the filter `tcp.port == 80` to identify the plaintext TCP SYN packet (or listen on port 443 when using HTTPS).


Semi-automated script:

1. See the attached script `vpn_tester.sh`. The file `README.md` has instructions on how to use this script. To test for this vulnerability, see the section "Leaks to Server IP address" where the parameter `--vpn-serverip` is used.
2. If the script receives the plaintext HTTP request the VPN client is vulnerable.

## Impact

## Hypothetical Risk (Important Reason to Patch)

If the VPN client would ever use plaintext DNS to learn the IP address of the VPN server, an adversary would be able to spoof the IP address of the VPN server, and then leak traffic to this spoofed IP address. This in fact is possible against several VPN clients of _other vendors_ that we tested. To be clear, your VPN client is not affected by this attack variant, since it doesn't appear to use plaintext DNS to obtain the VPN server's IP address. That said, preventing plaintext leakage to the VPN server's IP address would harden the security of the VPN client, and would make it clear it's not affected by this DNS-spoofing attack variant.

tl;dr: patching this vulnerability hardens the security of the VPN client and we consider this important.


## Impact 1: Deanomiyzing Users (Powerful Adversary)

As a more concrete and existing impact of the vulnerability, assume an adversary can trick the victim into loading a website or resource from a given URL (and that the adversary can then see the leaked TCP packets). The adversary can assure that this URL resolves to the IP address of the VPN server that the victim is using. We will now give two examples where doing this has a direct privacy and security impact in practice.

As a first example, assume the victim uses a VPN to visit a sensitive website blocked in their country. The adversary is the country that person is living in and this adversary wants to identify who is visiting this website. For instance, this website may be used by human rights activists, a Torrent website, a prohibited foreign news website, a discussion forum about the country, and so on. It's a realistic assumption that this adversary can influence minor elements of this website, for instance through the following means:

- If the website is a message board or marketplace, the adversary may be able to create a profile that references an external image. The adversary can then make the victim load an image from an arbitrary URL without having to exploit any vulnerability on the website.

- Another alternative scenario in which the vulnerability can be abused are typical private messaging applications (Slack, Discord, Telegram, etc). Often, when a link is shared through a messaging application, the client will show a preview of the link by making a request to the URL in the background. Therefore, by sending a link that resolves to the IP address of the VPN server, we can make the victim leak traffic outside the VPN tunnel.

- The adversary may abuse a (stored) XSS vulnerability on the website. This allows the adversary to make the victim load a page from an arbitrary URL. Note that XSS vulnerabilities are considered common even in the most secure web applications.

- In targeted attacks, a hostile country or organization may use exploits to gain full control over the sensitive website that the victim is using. For instance, just recently the Genesis Dark Web Market was taken down by several law enforcement agencies. Law enforcement could have used this access to try to deanonymize users of the website by modifying the website such that the victim's browser will try to load resources from a VPN server IP address.

All combined, we can assume the adversary can make the victim's browser load a website from the VPN server's IP address. A powerful adversary can use this ability to deanonymize the user. In particular, a powerful enough adversary, such as a country or cooperating law enforcement agencies, can then monitor the traffic of all its citizens to then see which VPN user is now sending plaintext TCP packets to the VPN server's IP address. All combined, this enables a powerful adversary to deanonymize users of sensitive/blocked websites in their country.


## Impact 2: Negative Business Impact (Any Adversary)

As a second example, a less powerful adversary may be able to trick the victim into visiting any URL but may not be able to intercept the leaked plaintext traffic. This would still negatively impact your users and VPN. In particular, a malicious website can make the victim initiate connections to the IP addresses of VPN servers. This would show that your VPN doesn't always encrypt all traffic. Note that there are other VPNs that don't leak this type of traffic in plaintext. So this could have reputational damage because users will now start to doubt whether the VPN will encrypt and protect all traffic.


## Redirecting Leaked Traffic

An important remark is that a person-in-the-middle attacker can redirect the plaintext traffic so it gets forwarded to the adversary's own server instead of to the VPN server. For instance, a malicious Linux Wi-Fi hotspot can use the following iptable rule to redirect this leaked traffic to its own local server:

```
sudo iptables -t nat -I PREROUTING -p tcp -d $SERVERIP --dport 80 -j REDIRECT --to 80
```

This will redirect the plaintext HTTP traffic to the adversary's local server instead of forwarding it to the VPN server's IP address (this is what the `--vpn-serverip` parameter of the `vpn_tester.sh` script does). The adversary can then host their own server and will be able to see the full URL that the victim is trying to access, and the adversary can send any reply back.


## Mitigation

On Linux:
- Option 1: The VPN traffic can be given a `fwmark` and [policy-based routing](https://ro-che.info/articles/2021-02-27-linux-routing) can be used such that everything is sent through the VPN tunnel except traffic generated by the VPN client.
- Option 2: The VPN process can run under a different user, and then [UID-based routing](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=4fb74506838b) can be used to send all traffic through the VPN tunnel except traffic generated by the VPN process/user.

On Android:
- By default, Android assures that all traffic gets tunneled except encrypted VPN traffic itself (using UID-based routing). There should be no need to call `VpnService.Builder excludeRoute` or similar to exclude traffic to the VPN server IP.


## Experiments

We tested Linux and Android and confirmed the vulnerability on both OSs.

In my experiments, the adversary acted as a Wi-Fi Access Point using the attached `vpn_tester.sh` script. I connected with the VPN and used the script to identify the IP address of the VPN server (and confirmed this with Wireshark). The script redirects plaintext traffic on port 80 to the script's web server. Finally, I visited `http://<SERVERIP>` in a browser (replace that IP address with the VPN server). This causes the browser to load a page with the following content:

	<html>
	<head>
		<title>User is being tracked!</title>
	</head>
	<body>
	This website visit was leaked outside the encrypted VPN tunnel!
	</body>
	</html>

The resulting network captures are attached:

- `vpn_tester.sh` and `README.md`: the tool we used to test VPNs in our research with a short README for this specific vulnerability.
- `mozilla-linux-leak-serverip.*`: example network capture of the attack against Linux. See packets 199 to 205 for the example leak.
- `mozilla-android-leak-serverip.pcapng`: example network capture against Android. See packet 4288 for an example leak. Use the filter `http` to see all leaks.

Best regards,
Mathy Vanhoef

## Attachments
- README.md
- vpn_tester.sh
- mozilla-linux-leak-serverip.log
- mozilla-linux-leak-serverip.pcapng
- mozilla-android-leak-serverip.pcapng
