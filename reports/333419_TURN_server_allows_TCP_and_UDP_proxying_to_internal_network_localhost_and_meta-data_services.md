# TURN server allows TCP and UDP proxying to internal network, localhost and meta-data services

## Report Details
- **Report ID**: 333419
- **URL**: https://hackerone.com/reports/333419
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-04-04T14:05:47.045Z
- **Disclosed**: 2020-03-12T00:15:42.616Z

## Reporter
- **Username**: sandrogauci
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
The TURN servers used by Slack allow TCP connections and UDP packets to be proxied to the internal network. This gives an attacker the ability to scan and interact with internal systems.

The attacker may proxy TCP connections to the internal network by setting the `XOR-PEER-ADDRESS` of the TURN connect message (method `0x000A`, <https://tools.ietf.org/html/rfc6062#section-4.3>) to a private IPv4 address.

UDP packets may be proxied by setting the `XOR-PEER-ADDRESS` to a private IP in the TURN send message indication (method `0x0006`, <https://tools.ietf.org/html/rfc5766#section-10>).

Please check the attached report for additional details.

## Impact

By abusing this feature an attacker will be able to read and potentially modify sensitive information in Slack's internal infrastructure. Typically, this security vulnerability has at least the same impact as an SSRF. However it is considered more useful from an attacker's point of view since attacks are not restricted to HTTP.

The hacker selected the **Server-Side Request Forgery (SSRF)** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**Can internal services be reached bypassing network access control?**
Yes

**What internal services were accessible?**
Metadata, localhost, network services on the `10.0.0.0/8`

**Security Impact**
By abusing this feature an attacker will be able to read and potentially modify sensitive information in Slack's internal infrastructure. Typically, this security vulnerability has at least the same impact as an SSRF. However it is considered more useful from an attacker's point of view since attacks are not restricted to HTTP.

Note: vulnerability is not SSRF but open TURN proxy - this was the closest I could choose.



## Attachments
- turn_tcp_proxy_response.pcapng
- report.md
- turn_udp(53)_proxy_response.pcapng
