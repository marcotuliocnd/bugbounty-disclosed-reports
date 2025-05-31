# SSRF By adding a custom integration on console.helium.com

## Report Details
- **Report ID**: 1055823
- **URL**: https://hackerone.com/reports/1055823
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-12-10T14:38:28.190Z
- **Disclosed**: 2021-05-26T19:26:24.778Z

## Reporter
- **Username**: th0roid
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: helium

## Vulnerability Information
A Server Side Request Forgery vulnerability was found in the *Add a custom Integration* feature on *console.helium.com*. By creating a custom HTTP integration, and setting the integration endpoint to http://169.254.169.254/latest/meta-data private meta-data from the AWS EC2 instance running can be retrieved.

{F1111768}

{F1111767}

The server makes the HTTP request and sets the response body  as the integration message every time that the device sends a packet. As the endpoint input is not validated, this makes the application vulnerable to a critical SSRF.

{F1111779}

{F1111780}

Endpoint set as: http://169.254.169.254/latest/meta-data/ami-id

{F1111781}

## Impact

By exploiting this vulnerability an attacker can get access to the server internal network and access private and critical information.

## Attachments
- 2_ssrf.png
- 1_ssrf.png
- 3_ssrf.png
- 4_ssrf.png
- 5_ssrf.png
