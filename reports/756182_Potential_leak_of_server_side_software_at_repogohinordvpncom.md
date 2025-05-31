# Potential leak of server side software at repogohi.nordvpn.com

## Report Details
- **Report ID**: 756182
- **URL**: https://hackerone.com/reports/756182
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-12-11T15:14:05.640Z
- **Disclosed**: 2020-02-16T18:51:39.626Z

## Reporter
- **Username**: zerody
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nordsecurity

## Vulnerability Information
## Summary:
I found a public Git Repository at https://repogohi.nordvpn.com/. It looks like the software components in this repository are part of the VPN Servers. So I'm afraid there's a certain risk.

The following packages are among others publicly available:

```
openvpn-xor_2.4.5-stretch1nord_amd64.deb 
openvpn_2.4.5-stretch1nord_amd64.deb  
squid-langpack-nord_20180226-1_all.deb 
```

Furthermore I found the Origin-IP (behind Cloudflare): https://95.216.8.4/
This allows an attacker to bypass all security features of Cloudflare.

Feel free to correct my assumption and Severity of this report :)

## Impact

- Leak of server side software components (VPN Infrastructure)
- Simplifies the reengineering of the used software

## Attachments
No attachments
