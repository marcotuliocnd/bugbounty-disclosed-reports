# Unauthorized access of Monero wallet by an unprivileged process

## Report Details
- **Report ID**: 462442
- **URL**: https://hackerone.com/reports/462442
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-12-14T13:45:15.815Z
- **Disclosed**: 2019-04-03T22:38:50.924Z

## Reporter
- **Username**: thanhb
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
## Description:
As per our understanding, Monero wallet app provides a separate executable for the user to enable the RPC interface (monero-wallet-rpc). When the user runs the executable, the RPC server will start on a port number that is specified by the user. The RPC server authenticates the client with the HTTP digest access authentication scheme, which is based on a simple challenge-response paradigm. Basically, the client receives a nonce from the server and then replies with a MD5 hash value of the username, the password, the nonce, the HTTP method, and the URI. 

An attacker is a non-privileged user, who can sign in to the victim’s computer with his own credentials or guest account. The attacker first needs to run a process in the background when the victim is using the computer. On Linux and macOS, the attacker only needs to log in, run the process, and leave it running when he logs out. On Windows, user processes are killed at the end of the login session, and thus the attacker needs to do fast user switching to leave his session in the background. The attacker can also remotely run his malicious process if SSH or remote desktop is enabled on the target computer.

With the malicious process running in the background, it is possible to perform server impersonation on the Monero wallet by hijacking the port number before the victim starts the RPC server. The digest access authentication mechanism does not help here because it only authenticates the client. However, the RPC executable will fail to start if the port that it uses has already been taken. While this allows the victim to detect the attack, it does not free him from risks. For example, an aggressively-caching user may attach the RPC executable to the operating system's startup to launch it automatically after login for convenience. In that case, since the RPC server process does not have a GUI to notify the victim that it has failed, the victim will not notice the failure and thus assume that the RPC server is running. Hence, the attacker's malicious server captures commands from the benign client. An example of such commands is “create_wallet”, which tells the server to create a new wallet account. This allows the attacker to have access to the new account because it is created by the attacker instead of the real wallet application.

The attack is straightforward, and no privilege escalation is needed. Also, there are many potential attackers who can perform the attack. For example, in enterprise environments that employ centralized access control mechanisms and allow login by multiple users to the same computer, anyone is a potential attacker. Any computer with guest account enabled is similarly vulnerable.

## Releases Affected:
Tested on Monero wallet 0.12.3

## How to fix:
We found similar issues on other cryptocurrencies’ wallet applications and are working with them to address the issues. There are various ways to prevent the attack, some of which are as follows:
- Mandate the use of TLS on the RPC interface.
- The RPC server accepts only RPC clients that are owned by users belonging to Administrators or a special group.

## Supporting Material/References:
Recently, we have shown similar critical vulnerabilities in many well-known password managers, hardware tokens, and other security-critical applications at Usenix Security and DefCon: 
https://www.usenix.org/conference/usenixsecurity18/presentation/bui

## Impact

Access to the victim's wallet without knowing authentication credentials.

## Attachments
No attachments
