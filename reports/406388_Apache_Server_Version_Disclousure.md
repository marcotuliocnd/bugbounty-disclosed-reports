# Apache Server Version Disclousure

## Report Details
- **Report ID**: 406388
- **URL**: https://hackerone.com/reports/406388
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-09-06T08:43:46.114Z
- **Disclosed**: 2020-03-30T17:20:39.600Z

## Reporter
- **Username**: mazmur
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bohemia

## Vulnerability Information
Hello Team,
I would like to report a bug for https://forums.bohemia.net/
Banner Grabbing is a technique used to get information about remote servers. In addition, this directory is used to find information about remote servers.

Proof of concept :
1. Go to https://forums.bohemia.net/applications/

This information might help an attacker gain a greater understanding of the systems in use and potentially develop further attacks targeted at the specific version of Apache.

Remediation
Configure your web server to prevent information leakage from the SERVER header of its HTTP response.

I hope my report can help you to fix it and impress you. Looking forward from you soon.

Kind Regards,

## Impact

Impact
An attacker might use information aimed at harvesting specifically for an exploit version.

## Attachments
- poc4.png
