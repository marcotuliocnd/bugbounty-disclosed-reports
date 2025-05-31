# SSRF at apps.nextcloud.com/developer/apps/releases/new

## Report Details
- **Report ID**: 213358
- **URL**: https://hackerone.com/reports/213358
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-03-14T09:43:18.482Z
- **Disclosed**: 2017-04-20T14:45:46.994Z

## Reporter
- **Username**: t-pwn
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
***Hi,***

***I've found SSRF vulnerability at https://apps.nextcloud.com/developer/apps/releases/new***

##Description##

Server Side Request Forgery (SSRF) is a vulnerability that appears when an attacker has the ability to create requests from the vulnerable server.

Usually, Server Side Request Forgery (SSRF) attacks target internal systems behind the firewall that are normally inaccessible from the outside world (but using SSRF it’s possible to access these systems). With SSRF it’s also possible to access services from the same server that is listening on the loopback interface.
Using Server Side Request Forgery attacks it’s possible to:

+ Scan and attack systems from the internal network that are not normally accessible
+ Enumerate and attack services that are running on these hosts
+ Exploit host-based authentication services

##Steps to reproduce##

+ Navigate to https://apps.nextcloud.com/developer/apps/releases/new
+ Enter https://127.0.0.1:22 (SSH) or https://127.0.0.1:80 (HTTP) (Download Link area) 
+ You will get this error
{F168743}
         means the 22 port is opened, the same with 80
+ but if you entered https://127.0.0.1:21 (Telnet) you will get this error 
{F168742}
         means the 21 port isn't opened

***Thanks.***


## Attachments
- port21isnotopened.png
- port22openeed.png
