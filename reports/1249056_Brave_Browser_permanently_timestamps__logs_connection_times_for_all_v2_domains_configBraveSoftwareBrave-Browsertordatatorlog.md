# Brave Browser permanently timestamps & logs connection times for all v2 domains ~/.config/BraveSoftware/Brave-Browser/tor/data/tor.log

## Report Details
- **Report ID**: 1249056
- **URL**: https://hackerone.com/reports/1249056
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-07-01T08:53:07.950Z
- **Disclosed**: 2021-08-16T17:57:43.188Z

## Reporter
- **Username**: sickcodes
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

A vulnerability in the Brave Browser v1.28.43 and below allows a local or physical attacker to view the exact timestamps that a user connected to a v2 onion address. A local or physical attacker could read  ~/.config/BraveSoftware/Brave-Browser/tor/data/tor.log identify the exact moment a user connected to a new site, easily triangulating the user via a complete log of connection timestamps, which could be easily compared with a server connection log, a compromised Tor end point, or other related Tor attack, affecting the confidentiality & integrity of a user's Tor session.

## Products affected: 

 * operating system, Brave version or Brave website page, etc.

Tor Desktop Browser (All platforms)

## Steps To Reproduce:

 * List the steps needed to reproduce the vulnerability

Visit http://wikitoronionlinks.com/ while using Tor Private Browsing.

Click on an assortment of .onion v2 URLs.

Inspect `~/.config/BraveSoftware/Brave-Browser/tor/data/tor.log`

## Supporting Material/References:

```
Jul 01 08:40:50.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:40:50.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:40:51.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:40:51.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:40:51.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:40:52.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:40:53.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:40:59.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:40:59.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:41:00.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:41:02.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:41:02.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:41:02.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:41:07.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:41:07.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:41:09.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:41:09.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:41:09.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:41:10.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:41:12.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline

```

## Impact

Violate the confidentiality & integrity of a user's Tor session.

## Attachments
- Screenshot_2021-07-01_08-41-05.png
- Screenshot_2021-07-01_08-50-25.png
