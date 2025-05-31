# Dangling cloud instance at vpn.inverselink.com

## Report Details
- **Report ID**: 1112679
- **URL**: https://hackerone.com/reports/1112679
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-02-27T04:03:24.729Z
- **Disclosed**: 2021-03-11T17:58:20.365Z

## Reporter
- **Username**: ian
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:** `	vpn.inverselink.com` points to `54.202.130.246`, which is currently serving a TLS certificate for `Workday, Inc`. This seems to indicate that the subdomain is no longer controlled by HackerOne.

### Optional: Supporting Material/References (Screenshots)
```
% dig  vpn.inverselink.com +short
54.202.130.246

 % curl -v https://vpn.inverselink.com
*   Trying 54.202.130.246...
* TCP_NODELAY set
* Connected to vpn.inverselink.com (54.202.130.246) port 443 (#0)
[...]
* Server certificate:
*  subject: C=US; ST=California; L=Pleasanton; O=Workday Inc.; CN=*.workdaysuv.com
```

### Optional: Did you use [recon data made available by HackerOne](https://github.com/Hacker0x01/helpful-recon-data) to find this vulnerability?
no

## Impact

Subdomain takeover if Workday releases this IP address

## Attachments
No attachments
