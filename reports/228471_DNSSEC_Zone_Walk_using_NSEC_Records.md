# DNSSEC Zone Walk using NSEC Records

## Report Details
- **Report ID**: 228471
- **URL**: https://hackerone.com/reports/228471
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-05-15T11:07:14.609Z
- **Disclosed**: 2018-01-30T20:45:18.666Z

## Reporter
- **Username**: pk21
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Due to a design flaw in the NSEC records used by DNSSEC it is possible to discover all subdomains of a particular domain for which NSEC records are available. NSEC records are used by the weblate.org domain which means anyone can retreive all subdomains of weblate.org.
These subdomains can contain great information for any attacker looking for a quick entry into a network. There currently aren't much subdomains for weblate.org but it is worth protecting it.
Also note that domains hosted on the same dns servers are probably also vulnerable.

PoC:
There already is a tool called dnsrecon to exploit this issue:
# dnsrecon -t zonewalk -d weblate.org
[*] Performing NSEC Zone Walk for weblate.org
[*] Getting SOA record for weblate.org
[*] Name Server 81.0.217.111 will be used
[*] 	 A weblate.org 77.78.107.252
[*] 	 AAAA weblate.org 2001:1528:136:dead:beef:4242:0:30
[*] 	 A _dmarc.weblate.org no_ip
[*] 	 TXT _domainkey.weblate.org o=~; r=root@tele3.cz
[*] 	 TXT 20150416._domainkey.weblate.org v=DKIM1;p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC9rsl4FuYcCYtAwa6ggVQWfNEi0W7sx3T6Sp0k8vE57gtaqTBAEzW7EOW6keMkn0GjfV6SFZNEZJkpFAdv2wgLYybhBC5wbCNzQ0mVt7UR+pgT+ypwjcizNgxHoCrTtRg6vVhLBwUonEtMHGxr1+7HTFdwHpcr1ZoMucMtWrjjvQIDAQAB
[*] 	 TXT 20150504._domainkey.weblate.org v=DKIM1;p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDanhclUcE1X+OlI4NdYeF5zYgXcmxxzGCnFWb8KmRV8dTDfS0RxKKyz+o3WtHC2DSsePfQYY6gHjCp8d0lxuo1tdVez/YkEru6JM/ot7QS64wSY12+OfZkEXyhs80vicxiCMv1zFKGXb5v/MRjlVPEZNSWIh4CVRAxHVC/dYSz9wIDAQAB
[*] 	 TXT tele3._domainkey.weblate.org v=DKIM1; k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzDGsRC+f9ltDEOXN5SYBvwkYMxBARm/9Sepf2F8L7v54RVz1t+YOupxbMcAKWWeyjrXQIuhmX+lwLcvRryZRmJGEnKQR9JWuuF9+EnH7BaH5/EFqg4522E5p2ERCxKcVomWpaeoe6OzV7SpK7Y6AzTzstR5+roHCDrYD84bRk61ZYvfZ5on4wuY2d7zNL7Iv1Kc01YxiF4FCrq5Vb4VSdr1MA/wF8mkvKMoZcwRl0GAXfesYb14S4vraKo5Z+CfMqKMWYE5XQVU9UVsX/orQpk2V0z/ttxIuR2SkItSwQY/VtkjcvepZX4Wu1eUGRuwXQfsbg4jzDupuPHXk9UqNpQIDAQAB
[*] 	 SRV _avatars._tcp.weblate.org avatar.cihar.com 77.78.107.252 80 0
[*] 	 SRV _avatars._tcp.weblate.org avatar.cihar.com 2001:1528:136:dead:beef:4242:0:30 80 0
[*] 	 SRV _avatars-sec._tcp.weblate.org avatar.cihar.com 77.78.107.252 443 0
[*] 	 SRV _avatars-sec._tcp.weblate.org avatar.cihar.com 2001:1528:136:dead:beef:4242:0:30 443 0
[*] 	 A a0fab3dee337e76f57e91f4ac803658c.weblate.org 204.79.197.200
[*] 	 A a0fab3dee337e76f57e91f4ac803658c.weblate.org 13.107.21.200
[*] 	 CNAME debian.weblate.org hosted.weblate.org
[*] 	 A hosted.weblate.org 77.78.107.252
[*] 	 CNAME debian.weblate.org hosted.weblate.org
[*] 	 AAAA hosted.weblate.org 2001:1528:136:dead:beef:4242:0:30
[*] 	 A debug.weblate.org 77.78.107.252
[*] 	 AAAA debug.weblate.org 2001:1528:136:dead:beef:4242:0:30
[*] 	 CNAME demo.weblate.org hosted.weblate.org
[*] 	 A hosted.weblate.org 77.78.107.252
[*] 	 CNAME demo.weblate.org hosted.weblate.org
[*] 	 AAAA hosted.weblate.org 2001:1528:136:dead:beef:4242:0:30
[*] 	 A mexw22uufza2.demo.weblate.org no_ip
[*] 	 CNAME docs.weblate.org web.cihar.com
[*] 	 A web.cihar.com 77.78.107.252
[*] 	 CNAME docs.weblate.org web.cihar.com
[*] 	 AAAA web.cihar.com 2001:1528:136:dead:beef:4242:0:30
[*] 	 A git.weblate.org 77.78.107.252
[*] 	 AAAA git.weblate.org 2001:1528:136:dead:beef:4242:0:40
[*] 	 A hg.weblate.org 77.78.107.252
[*] 	 AAAA hg.weblate.org 2001:1528:136:dead:beef:4242:0:30
[*] 	 A hosted.weblate.org 77.78.107.252
[*] 	 AAAA hosted.weblate.org 2001:1528:136:dead:beef:4242:0:30
[*] 	 CNAME www.weblate.org weblate.org
[*] 	 A weblate.org 77.78.107.252
[*] 	 CNAME www.weblate.org weblate.org
[*] 	 AAAA weblate.org 2001:1528:136:dead:beef:4242:0:30
[*] 	 A 4rzkhhatpbba.hosted.weblate.org no_ip
[*] 39 records found

Solution:
The best solution is implementing NSEC3. There is a nice article at http://strotmann.de/roller/dnsworkshop/entry/take_your_dnssec_with_a which describes NSEC and NSEC3 in further detail.

## Attachments
No attachments
