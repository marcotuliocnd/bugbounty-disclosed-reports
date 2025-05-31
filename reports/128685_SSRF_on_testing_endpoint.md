# SSRF on testing endpoint

## Report Details
- **Report ID**: 128685
- **URL**: https://hackerone.com/reports/128685
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-04-06T10:39:49.602Z
- **Disclosed**: 2016-09-14T20:32:06.836Z

## Reporter
- **Username**: agarri_fr
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: apitest

## Vulnerability Information
# Synopsis

The form at https://www.apitest.io/request accepts (among others) the "url" parameter. This feature allows to reach internal services (like the OpenStack metadata server) or services running on loopback.

# Identified services

http://0x7f.1/ (nginx) => "If you see this page, the nginx web server is successfully installed and
working. Further configuration is required."

http://169.254.169.254/meta-data (OpenStack metada) => directoty listing (instance-id, mac, local-ipv4, public-ipv4, network_config/content_path, SUBID, ipv6-addr, ipv6-prefix)

http://0x7f.1:8081/ (vestacp admin panel) => <a href="http://vestacp.com/">Powered by VESTA</a>

# Impacts

The metadata server does't seem to host any sensitive data. However, access to port 8081 may allow to reconfigure the OS or services (untested). Additional services may exist, but it seems that my IP address (81.56.184.117) was just blacklisted on your side.

## Attachments
No attachments
