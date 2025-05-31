# Tor Browser using --log or --verbose logs the exact connection time a client connects to any v2 domains.

## Report Details
- **Report ID**: 1250273
- **URL**: https://hackerone.com/reports/1250273
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-07-02T20:37:16.712Z
- **Disclosed**: 2021-09-27T09:14:58.374Z

## Reporter
- **Username**: sickcodes
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
## Summary:
A vulnerability in the Tor Browser 78.11.0esr and below allows a local or physical attacker to view metadata about v2 domains, namely the exact timestamp that a user connected to a v2 onion address while using either the --log or --verbose command line options. A local or physical attacker can identify the exact moment a user connected to a new v2 onion site, easily triangulating the user via a complete log of connection timestamps in the log file, or verbosely in the terminal window. This timestamp is generated every single time a client connects to a v2 onion address and could therefore be easily compared with a server connection log, a compromised Tor end point, or other related Tor attack, affecting the confidentiality & integrity of a user's Tor session when using --log or --verbose.

## Steps To Reproduce:
Download Tor latest
Use either:
`./start-tor-browser.desktop --log ./file.log`
`./start-tor-browser.desktop --verbose`

Visit http://wikitoronionlinks.com/

Click on an assortment of .onion v2 URLs.

Inspect the output.

Notably, the warning occurs when the client connects, rather than clicking a link, making it even easier to pair up with server connection times.

## Supporting Material/References:

```
[user@hostname tor-browser_en-US]$ ./start-tor-browser.desktop --verbose
Launching './Browser/start-tor-browser --detach --verbose'...
Fontconfig warning: "/tmp/tor-browser_en-US/Browser/TorBrowser/Data/fontconfig/fonts.conf", line 37: Use of ambiguous path in <dir> element. please add prefix="cwd" if current behavior is desired.
Fontconfig warning: "/tmp/tor-browser_en-US/Browser/TorBrowser/Data/fontconfig/fonts.conf", line 85: unknown element "blank"
Jul 02 20:06:58.983 [notice] Tor 0.4.5.9 (git-d0ed04d50e80fe1c) running on Linux with Libevent 2.1.11-stable, OpenSSL 1.1.1k, Zlib 1.2.11, Liblzma N/A, Libzstd N/A and Glibc 2.33 as libc.
Jul 02 20:06:58.983 [notice] Tor can't help you if you use it wrong! Learn how to be safe at https://www.torproject.org/download/download#warning
Jul 02 20:06:58.983 [notice] Read configuration file "/tmp/tor-browser_en-US/Browser/TorBrowser/Data/Tor/torrc-defaults".
Jul 02 20:06:58.983 [notice] Read configuration file "/tmp/tor-browser_en-US/Browser/TorBrowser/Data/Tor/torrc".
Jul 02 20:06:58.984 [notice] Opening Control listener on 127.0.0.1:9151
Jul 02 20:06:58.984 [notice] Opened Control listener connection (ready) on 127.0.0.1:9151
Jul 02 20:06:58.984 [notice] DisableNetwork is set. Tor will not make or accept non-control network connections. Shutting down all existing connections.
Jul 02 20:06:58.000 [notice] Parsing GEOIP IPv4 file /tmp/tor-browser_en-US/Browser/TorBrowser/Data/Tor/geoip.
Jul 02 20:06:59.000 [notice] Parsing GEOIP IPv6 file /tmp/tor-browser_en-US/Browser/TorBrowser/Data/Tor/geoip6.
Jul 02 20:06:59.000 [notice] Bootstrapped 0% (starting): Starting
Jul 02 20:06:59.000 [notice] Starting with guard context "default"
Jul 02 20:06:59.000 [notice] Delaying directory fetches: DisableNetwork is set.
Jul 02 20:06:59.000 [notice] New control connection opened from 127.0.0.1.
Jul 02 20:06:59.000 [notice] DisableNetwork is set. Tor will not make or accept non-control network connections. Shutting down all existing connections.
Jul 02 20:06:59.000 [notice] New control connection opened from 127.0.0.1.
Fontconfig warning: "/tmp/tor-browser_en-US/Browser/TorBrowser/Data/fontconfig/fonts.conf", line 37: Use of ambiguous path in <dir> element. please add prefix="cwd" if current behavior is desired.
Fontconfig warning: "/tmp/tor-browser_en-US/Browser/TorBrowser/Data/fontconfig/fonts.conf", line 85: unknown element "blank"
Fontconfig warning: "/tmp/tor-browser_en-US/Browser/TorBrowser/Data/fontconfig/fonts.conf", line 37: Use of ambiguous path in <dir> element. please add prefix="cwd" if current behavior is desired.
Fontconfig warning: "/tmp/tor-browser_en-US/Browser/TorBrowser/Data/fontconfig/fonts.conf", line 85: unknown element "blank"
Jul 02 20:07:01.000 [notice] DisableNetwork is set. Tor will not make or accept non-control network connections. Shutting down all existing connections.
Jul 02 20:07:01.000 [notice] DisableNetwork is set. Tor will not make or accept non-control network connections. Shutting down all existing connections.
Jul 02 20:07:01.000 [notice] DisableNetwork is set. Tor will not make or accept non-control network connections. Shutting down all existing connections.
Jul 02 20:07:01.000 [notice] Opening Socks listener on 127.0.0.1:9150
Jul 02 20:07:01.000 [notice] Opened Socks listener connection (ready) on 127.0.0.1:9150
Jul 02 20:07:01.000 [notice] Renaming old configuration file to "/tmp/tor-browser_en-US/Browser/TorBrowser/Data/Tor/torrc.orig.1"
Jul 02 20:07:02.000 [notice] Bootstrapped 5% (conn): Connecting to a relay
Jul 02 20:07:02.000 [notice] Bootstrapped 10% (conn_done): Connected to a relay
Jul 02 20:07:02.000 [notice] Bootstrapped 14% (handshake): Handshaking with a relay
Jul 02 20:07:02.000 [notice] Bootstrapped 15% (handshake_done): Handshake with a relay done
Jul 02 20:07:02.000 [notice] Bootstrapped 20% (onehop_create): Establishing an encrypted directory connection
Jul 02 20:07:02.000 [notice] Bootstrapped 25% (requesting_status): Asking for networkstatus consensus
Jul 02 20:07:02.000 [notice] Bootstrapped 30% (loading_status): Loading networkstatus consensus
Jul 02 20:07:03.000 [notice] I learned some more directory information, but not enough to build a circuit: We have no usable consensus.
Jul 02 20:07:04.000 [notice] Bootstrapped 40% (loading_keys): Loading authority key certs
Jul 02 20:07:04.000 [notice] The current consensus has no exit nodes. Tor can only build internal paths, such as paths to onion services.
Jul 02 20:07:04.000 [notice] Bootstrapped 45% (requesting_descriptors): Asking for relay descriptors
Jul 02 20:07:04.000 [notice] I learned some more directory information, but not enough to build a circuit: We need more microdescriptors: we have 0/6832, and can only build 0% of likely paths. (We have 0% of guards bw, 0% of midpoint bw, and 0% of end bw (no exits in consensus, using mid) = 0% of path bw.)
Jul 02 20:07:05.000 [notice] Bootstrapped 50% (loading_descriptors): Loading relay descriptors
Jul 02 20:07:06.000 [notice] The current consensus contains exit nodes. Tor can build exit and internal paths.
Jul 02 20:07:07.000 [notice] Bootstrapped 55% (loading_descriptors): Loading relay descriptors
Jul 02 20:07:07.000 [notice] Bootstrapped 60% (loading_descriptors): Loading relay descriptors
Jul 02 20:07:07.000 [notice] Bootstrapped 69% (loading_descriptors): Loading relay descriptors
Jul 02 20:07:08.000 [notice] Bootstrapped 75% (enough_dirinfo): Loaded enough directory info to build circuits
Jul 02 20:07:08.000 [notice] Bootstrapped 80% (ap_conn): Connecting to a relay to build circuits
Jul 02 20:07:08.000 [notice] Bootstrapped 85% (ap_conn_done): Connected to a relay to build circuits
Jul 02 20:07:08.000 [notice] Bootstrapped 89% (ap_handshake): Finishing handshake with a relay to build circuits
Jul 02 20:07:09.000 [notice] Bootstrapped 90% (ap_handshake_done): Handshake finished with a relay to build circuits
Jul 02 20:07:09.000 [notice] Bootstrapped 95% (circuit_create): Establishing a Tor circuit
Jul 02 20:07:10.000 [notice] Bootstrapped 100% (done): Done
Jul 02 20:07:10.000 [notice] New control connection opened from 127.0.0.1.
Jul 02 20:07:10.000 [notice] New control connection opened from 127.0.0.1.
Fontconfig warning: "/tmp/tor-browser_en-US/Browser/TorBrowser/Data/fontconfig/fonts.conf", line 37: Use of ambiguous path in <dir> element. please add prefix="cwd" if current behavior is desired.
Fontconfig warning: "/tmp/tor-browser_en-US/Browser/TorBrowser/Data/fontconfig/fonts.conf", line 85: unknown element "blank"
Fontconfig warning: "/tmp/tor-browser_en-US/Browser/TorBrowser/Data/fontconfig/fonts.conf", line 37: Use of ambiguous path in <dir> element. please add prefix="cwd" if current behavior is desired.
Fontconfig warning: "/tmp/tor-browser_en-US/Browser/TorBrowser/Data/fontconfig/fonts.conf", line 85: unknown element "blank"
Fontconfig warning: "/tmp/tor-browser_en-US/Browser/TorBrowser/Data/fontconfig/fonts.conf", line 37: Use of ambiguous path in <dir> element. please add prefix="cwd" if current behavior is desired.
Fontconfig warning: "/tmp/tor-browser_en-US/Browser/TorBrowser/Data/fontconfig/fonts.conf", line 85: unknown element "blank"
Jul 02 20:07:58.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Fontconfig warning: "/tmp/tor-browser_en-US/Browser/TorBrowser/Data/fontconfig/fonts.conf", line 37: Use of ambiguous path in <dir> element. please add prefix="cwd" if current behavior is desired.
Fontconfig warning: "/tmp/tor-browser_en-US/Browser/TorBrowser/Data/fontconfig/fonts.conf", line 85: unknown element "blank"
Jul 02 20:07:59.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Fontconfig warning: "/tmp/tor-browser_en-US/Browser/TorBrowser/Data/fontconfig/fonts.conf", line 37: Use of ambiguous path in <dir> element. please add prefix="cwd" if current behavior is desired.
Fontconfig warning: "/tmp/tor-browser_en-US/Browser/TorBrowser/Data/fontconfig/fonts.conf", line 85: unknown element "blank"
Jul 02 20:07:59.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Fontconfig warning: "/tmp/tor-browser_en-US/Browser/TorBrowser/Data/fontconfig/fonts.conf", line 37: Use of ambiguous path in <dir> element. please add prefix="cwd" if current behavior is desired.
Fontconfig warning: "/tmp/tor-browser_en-US/Browser/TorBrowser/Data/fontconfig/fonts.conf", line 85: unknown element "blank"
Jul 02 20:08:07.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 02 20:08:07.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 02 20:08:10.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 02 20:08:28.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 02 20:08:28.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 02 20:08:28.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 02 20:08:28.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 02 20:08:28.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 02 20:09:30.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
^[[1;2D	^CJul 02 20:19:34.000 [notice] Interrupt: exiting cleanly.
Exiting due to channel error.
Exiting due to channel error.
Exiting due to channel error.
Exiting due to channel error.
Exiting due to channel error.
Exiting due to channel error.
Exiting due to channel error.

```

  * [attachment / reference]

## Impact

Violate the confidentiality & integrity of a user's Tor session.

## Attachments
- tor_browser_v2_timestamps.mp4
