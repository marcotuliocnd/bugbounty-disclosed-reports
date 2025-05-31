# Insecure Transportation Security Protocol Supported (TLS 1.0)

## Report Details
- **Report ID**: 163812
- **URL**: https://hackerone.com/reports/163812
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-27T13:33:55.447Z
- **Disclosed**: 2017-07-10T09:58:26.373Z

## Reporter
- **Username**: yodha
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Description: Its observed that that insecure transportation security protocol (TLS 1.0) is supported by your web server. TLS 1.0 has several flaws. An attacker can cause connection failures and they can trigger the use of TLS 1.0 to exploit vulnerabilities like BEAST.
Websites using TLS 1.0 will be considered non-compliant by PCI after 30 June 2018.

Impact: Attackers can perform man-in-the-middle attacks and observe the encryption traffic between your website and its visitors.

Recommended Fix: Configure your web server to disallow using weak ciphers. You need to restart the web server to enable changes.

By fingerprinting server, found that its Nginx Web server. So below is solution for Nginx
For Nginx, locate any use of the directive ssl_protocols in the nginx.conf file and remove TLSv1.
ssl_protocols TLSv1.1 TLSv1.2;


## Attachments
No attachments
