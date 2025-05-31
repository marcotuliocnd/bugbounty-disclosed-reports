# Leaking VPN traffic through non-RFC1918 local IP addresses

## Report Details
- **Report ID**: 1987680
- **URL**: https://hackerone.com/reports/1987680
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-05-15T06:33:02.228Z
- **Disclosed**: 2024-11-08T12:01:23.990Z

## Reporter
- **Username**: vanhoefm
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mozilla

## Vulnerability Information
## Disclosure and Deviation of T&Cs

This finding is part of a multi-party coordinated disclosure on VPN security. We plan to publicly disclose relevant findings in early August 2023. Please don't give a bug bounty if you disagree with the eventual public disclosure, we will still be happy to discuss details even without a bounty. Note that it's OK for us if you already release updated binaries before the coordinated disclosure as long as the details of the vulnerability are not mentioned. If you use the information in this report we assume this will be OK. Happy to discuss details.

For context, we tested more than 66 VPNs/devices, meaning your device is just one of the many VPNs we tested, so there won't be an explicit focus on it during disclosure. We also plan to contact CERT/CC to reach other VPN companies for similar vulnerabilities.


## Summary

As part of a larger study on VPN security, we found that Mozilla VPN on Linux and iOS sends traffic to the local network outside the VPN tunnel. On its own, this is not an issue, but a malicious Wi-Fi or Ethernet network can hand out non-RFC1918 IP addresses for the local network, and then your VPN client can be tricked into sending _nearly all_ IP-based traffic outside the VPN tunnel.

As a simple example, if a rogue Wi-Fi hotspot uses the subnet `216.165.47.0/24` for the local network, then all traffic to these IP addresses will be leaked in plaintext, i.e., sent outside the VPN tunnel. This is because the VPN client thinks these IP addresses are in the local network. For instance, if the victim then visits `http://nyu.edu`, which has IP address `216.165.47.10`, the website will be loaded _outside_ the VPN tunnel. An adversary can also use `0.0.0.0/1` or `128.0.0.0/1` as the local network so nearly all IP-based traffic can be intercepted.


## Steps to Reproduce

A quick-and-dirty method to test for the vulnerability is to make your router hand out non-RFC1918 IP addresses for the local network, e.g., using `216.165.47.0/24` for the local network. Then enable the VPN and try to visit `http://nyu.edu` or directly visit `http://216.165.47.10`. This should have as result that the NYU website won't load and in Wireshark you should see ARP requests for the IP address `216.165.47.10`.

For a more rigorous test, see the attached script `vpn_tester.sh` to reproduce the attack. The file `README.md` has instructions on how to use this script, in particular, the section "Local IP Camouflage Attack". In our experiments, we tried to leak traffic to `nyu.edu` using the following command:

```
sudo ./vpn_tester.sh wlan0 wlan0 testnetwork abcdefgh --vpn-local nyu.edu
```

After executing this command you can connect to the created Wi-Fi network (SSID `testnetwork` with password `abcdefgh`) and enable the VPN. When you now visit the website `http://nyu.edu` in a browser (don't include the WWW prefix!) the corresponding HTTP request and HTTP response will be sent _outside_ the VPN tunnel. You can also try to visit `http://216.165.47.10` (the exact IP address will be displayed by the script). Without performing the attack, traffic to this IP address would be sent through the VPN tunnel.

## Impact

## Example Impact 1: Leaking Traffic to a specific subnet

The direct impact is self-evident: even when the victim is always using the VPN, an adversary can leak all IP traffic in a given subnet. The adversary can forward the leaked traffic to the real server so that the victim can still visit all websites normally. If the website uses plaintext IP protocols, such as HTTP/DNS/SMTP/NTP/FTP/.., this directly leaks sensitive information or the adversary can use it as the basis for subsequent attacks.

If the victim is using an encrypted protocol such as HTTPS or similar, the adversary can still learn which IP addresses the victim is visiting, meaning the adversary can learn the websites that a victim is visiting (see ["What can you learn from an IP?"](https://irtf.org/anrw/2019/anrw2019-final44-acmpaginated.pdf)). Simply knowing the website that someone is visiting can be sensitive information, after all, that's why the victim might be using a VPN. The adversary can further try to perform known attacks on HTTP, such as SSLStrip, since the usage of HSTS is not yet widespread, or the adversary can use fingerprinting techniques to leak additional information such as the specific webpage being visited.


## Example Impact 2: Leaking all IP-based

An adversary can also try to assign the subnet `0.0.0.0/0` to intercept _all_ IP-based traffic. Whether this works depends on the target OS, since this may conflict with the default route. However, we found that using the subnet `0.0.0.0/1` or `128.0.0.0/1` to intercept _almost_ all traffic typically does work. So the attacker needs no prior knowledge of the user's browsing habits since they can intercept most IP-based traffic, and then identify the IP addresses that the victim is contacting.


## Mitigation

Local network access should be automatically blocked when the local network is using a non-RFC1918 IP range. Put differently, local network access should only be allowed towards RFC1918 IP addresses, i.e., only towards IP addresses that are not routed on the public Internet. Optionally, the user can be warned when the local network is using a non-RFC1918 IP range, and after accepting the warning the user can then still manually enable local network access.

On iOS, the API parameter `includeAllNetworks` should be set to True while `excludeLocalNetworks` should be set to False to prevent the attack. Optionally, when the VPN client verified that the local network is using an RFC1918 subnet, the API parameter `excludeLocalNetworks` can be set to True to still allow access to the local network. I have seen reports that on older iOS versions the usage of these parameters can cause reliability issues, but I didn't experience this myself on recent iOS releases.


## Experiments

We confirmed the vulnerability against Linux and iOS.

The following files are attached:

- `vpn_tester.sh` and `README.md`: the tool we used to test VPNs in our research with a short README for this specific vulnerability.
- `mozilla-linux-leak-local.*`: example of the attack against Linux. Notice that the client has an IP address in the subnet `216.165.47.0/24` and notice the traffic leak no `http://nyu.edu` in packets 1109 to 1115. You can use the filter `http` to see more leaks.

Best regards,
Mathy Vanhoef

## Attachments
- README.md
- vpn_tester.sh
- mozilla-linux-leak-local.log
- mozilla-linux-leak-local.pcapng
