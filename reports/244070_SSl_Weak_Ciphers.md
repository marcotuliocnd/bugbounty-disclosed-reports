# SSl Weak Ciphers

## Report Details
- **Report ID**: 244070
- **URL**: https://hackerone.com/reports/244070
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-06-28T17:23:04.200Z
- **Disclosed**: 2017-07-10T09:58:33.536Z

## Reporter
- **Username**: mkd1r
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
# Summary
Websites using TLS 1.0 will be considered non-compliant by PCI after 30 June 2018.

# Description
TLS 1.0 has several flaws. An attacker can cause connection failures and they can trigger the use of TLS 1.0 to exploit vulnerabilities like BEAST (Browser Exploit Against SSL/TLS).

# Steps To Reproduce

-Nginx, locate any use of the directive ssl_protocols in the nginx.conf file and remove TLSv1.

ssl_protocols TLSv1.1 TLSv1.2;
  
-Configure your web server to disallow using weak ciphers. You need to restart the web server to enable changes.

# Supporting Material/References:
https://blog.pcisecuritystandards.org/migrating-from-ssl-and-early-tls

## Attachments
No attachments
