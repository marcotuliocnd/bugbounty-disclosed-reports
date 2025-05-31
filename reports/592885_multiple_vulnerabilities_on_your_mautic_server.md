# multiple vulnerabilities on your mautic server

## Report Details
- **Report ID**: 592885
- **URL**: https://hackerone.com/reports/592885
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-05-30T20:58:58.986Z
- **Disclosed**: 2019-07-10T14:24:33.699Z

## Reporter
- **Username**: bbc6dfb7d3878289f2f98d4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: unikrn

## Vulnerability Information
Hi @unikrn!
I found some vulnerabilities in you crm server:

1. By pass Cloudflare access:

You Use Cloudflare Access on https://crm.unikrn.com . 
BUt this link bypassed  Cloudflare Access:  ████████/login

This vulnerability generates the disclosure of important data:

PHP info page:
██████████phpinfo  -  an attacker can find out the server configuration and also find out the server path

Symfony request log:

█████empty/search/results?limit=10 list of all requests, IP addresses and so on.

Symfony debug log:
██████████6099a6?panel=logger

Symfony config:
█████6099a6?panel=config

## Impact

crm.unicrn.com  multiple vulnerabilities on your mautic server

## Attachments
No attachments
