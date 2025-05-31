# Sensitive information disclosure via response headers on jenkins.brew.sh

## Report Details
- **Report ID**: 222063
- **URL**: https://hackerone.com/reports/222063
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-19T04:42:43.263Z
- **Disclosed**: 2017-04-25T16:46:47.777Z

## Reporter
- **Username**: mrnull1337
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: homebrew

## Vulnerability Information
While logging into jenkins.brew.sh site, the vulnerable nginx version is disclosed via response headers.
There is a chance with known vulnerabilities this could be compromised. so better to avoid banner disclosure with "Server Tokens Prod off" modification in conf file.

Please let me know if any further information is required.

Regards,
Mr_R3boot.

## Attachments
- serverversion.png
