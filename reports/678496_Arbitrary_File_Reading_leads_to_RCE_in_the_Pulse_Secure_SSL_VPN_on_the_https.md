# Arbitrary File Reading leads to RCE in the Pulse Secure SSL VPN on the https://███

## Report Details
- **Report ID**: 678496
- **URL**: https://hackerone.com/reports/678496
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-08-21T13:03:00.698Z
- **Disclosed**: 2019-12-02T19:59:54.014Z

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

I discovered that https://████ instance is vulnerable to described vulnerabilities.

##POC
Extracting `/etc/passwd` as example:
```
curl -i -k --path-as-is https://██████/dana-na/../dana/html5acc/guacamole/../../../../../../etc/passwd?/dana/html5acc/guacamole/
```
{F561180}

The RCE can be achieved with this chain:
1) Pulse Secure stores credentials in the cleartext.
2) Attacker reads credentials via CVE-2019-11510 (it stored in the `/data/runtime/mtmp/lmdb/dataa/data.mdb`) and authorizes on VPN
3) Attacker exploits CVE-2019-11539 - Post-auth Command Injection achieving RCE as root.

##Suggested fix
Update the Pulse Secure SSL VPN software (also implementing certificate validation can harden access a bit if some similar CVEs will be discovered in future).

## Impact

Remote code execution as root (by reading plaintext credentials and then exploiting CVE-2019-11539 - Post-auth Command Injection) and accessing intranet behind VPN.

## Attachments
No attachments
