# Bypass for blind SSRF #281950 and #287496

## Report Details
- **Report ID**: 642675
- **URL**: https://hackerone.com/reports/642675
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-07-14T01:27:49.354Z
- **Disclosed**: 2020-05-24T14:18:34.617Z

## Reporter
- **Username**: 7001
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: infogram

## Vulnerability Information
Hello, 
when checking these 2 reports #281950 and #287496 i found that it can be bypassed using IPv6/IPv4 Address Embedding

Steps to reproduce:
1-access this link https://infogram.com/api/web_resource/url?q=http://[0:0:0:0:0:ffff:127.0.0.1]

POC:
{F528736}

Refrences:
http://www.tcpipguide.com/free/t_IPv6IPv4AddressEmbedding.htm
https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Request%20Forgery

## Impact

Server Side Request Forgery or SSRF is a vulnerability in which an attacker forces a server to perform requests on their behalf.

## Attachments
- ssrf_bps.PNG
