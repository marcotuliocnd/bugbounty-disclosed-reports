# Brave Browser Tor Window leaks user's real IP to the external DNS server

## Report Details
- **Report ID**: 1077022
- **URL**: https://hackerone.com/reports/1077022
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-01-12T13:44:50.530Z
- **Disclosed**: 2021-06-17T05:25:38.585Z

## Reporter
- **Username**: newfunction
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

When a user navigates to a URL in Tor Window, the DNS requests are sent directly without using the Tor proxy, which leaks the user's real IP address and the requested domain name to the user's ISP and the DNS server.

## Products affected: 

 * OS: Ubuntu 18.04.5 LTS x86_64
 * Brave: Version 1.18.78 Chromium: 87.0.4280.141 (Official Build) (64-bit)

## Steps To Reproduce:

 * Open WireShark, and start capturing traffic on the Internet interface. Set WireShark's display filter to `dns`.
 * Open Brave Browser. Then open new private window with Tor.
 * On the Tor window, navigate to https://tools.ietf.org/ (or any other URLs)
 * In WireShark, you can see a DNS request for tools.ietf.org sent to your DNS server.

## Supporting Material/References:

  * a screenshot attached

## Impact

Brave's Tor window passively leaks users' IP addresses and requests to DNS servers. This undermines the user's anonymity.

## Attachments
- tor-window-dns-leakage.png
