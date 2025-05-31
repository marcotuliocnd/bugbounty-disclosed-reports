# Insecure Transportation Security Protocol Supported (TLS 1.0) on https://www.jamieweb.net

## Report Details
- **Report ID**: 323735
- **URL**: https://hackerone.com/reports/323735
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-03-08T19:38:42.983Z
- **Disclosed**: 2018-05-11T10:51:52.104Z

## Reporter
- **Username**: retr0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: jamieweb

## Vulnerability Information
## Summary: 
https://www.jamieweb.net still support TLS 1.0 protocol which has several flaws.

## Vulnerability:
With a SSL security scanner i was able to identify that an insecure transportation security protocol (TLS 1.0) is still supported by your web server.

TLS 1.0 has several flaws. An attacker can cause connection failures and they can trigger the use of TLS 1.0 to exploit vulnerabilities like BEAST (Browser Exploit Against SSL/TLS).

Websites using TLS 1.0 will be considered non-compliant by PCI after 30 June 2018.

## How to reproduice:
- Using Kali Linux, or any Linux distribution with nmap installed:
- Launch this command: nmap --script ssl-enum-ciphers -p 443 jamieweb.net
- Please check attached file for scan result: F270760 and see that there is still references to TLSv1.0.

## Remedy:
Configure your web server to disallow using weak ciphers. Please note that you need to restart the web server to enable changes.

- For Apache, adjust the SSLProtocol directive provided by the mod_ssl module. This directive can be set either at the server level or in a virtual host configuration.
>SSLProtocol +TLSv1.1 +TLSv1.2

- For Nginx, locate any use of the directive ssl_protocols in the nginx.conf file and remove TLSv1.
>ssl_protocols TLSv1.1 TLSv1.2;

- For Microsoft IIS, you should make some changes on the system registry.
1) Click on Start and then Run, type regedt32 or regedit, and then click OK.
2) In Registry Editor, locate the following registry key or create if it does not exist:
>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\
3) Locate a key named Server or create if it doesn't exist.
4) Under the Server key, locate a DWORD value named Enabled or create if it doesn't exist and set its value to "0".

## Supporting Material/References:
- [How to disable TLS v1.0](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn786418(v=ws.11)#BKMK_SchannelTR_TLS10)
- [OWASP - Insecure Configuration Management](https://www.owasp.org/index.php/Insecure_Configuration_Management)
- [OWASP - Insufficient Transport Layer Protection](https://www.owasp.org/index.php/Top_10_2010-A9-Insufficient_Transport_Layer_Protection)
- [How to disable PCT 1.0, SSL 2.0, SSL 3.0, or TLS 1.0 in Internet Information Services](https://support.microsoft.com/en-us/help/187498/how-to-disable-pct-1-0-ssl-2-0-ssl-3-0-or-tls-1-0-in-internet-informat)
- [IIS Crypto is a free tool that gives administrators the ability to enable or disable protocols, ciphers, hashes and key exchange algorithms on Windows Server 2003, 2008 and 2012](https://www.nartac.com/Products/IISCrypto/)
- [Date Change for Migrating from SSL and Early TLS](https://blog.pcisecuritystandards.org/migrating-from-ssl-and-early-tls)
- [Browser Exploit Against SSL/TLS Attack (BEAST)](http://resources.infosecinstitute.com/ssl-attacks/)

Thanks for reading,
Regards,
retr0

## Impact

Attackers can perform man-in-the-middle attacks and observe the encryption traffic between your website and its visitors.

## Attachments
- nmap.txt
