# Banner Grabbing - Apache Server Version Disclousure

## Report Details
- **Report ID**: 460556
- **URL**: https://hackerone.com/reports/460556
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-12-11T17:54:57.078Z
- **Disclosed**: 2018-12-11T20:57:14.603Z

## Reporter
- **Username**: hamzamandil
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ratelimited

## Vulnerability Information
Hello RATELIMITED, I'd like to report a nice little bug.

Banner Grabbing is a technique used to gain information about a remote server. Additionally, this technique is use to get information about remote servers.

I've captured the HTTP request while visiting theendlessweb.com

POC: 
Simply check screenshot you will see server version of RATELIMITED [Apache/2.4.25 (Debian)]

This information might help an attacker gain a greater understanding of the systems in use and potentially develop further attacks targeted at the specific version of Apache.

Impact
An attacker might use the disclosed information to harvest specific security vulnerabilities for the version identified.

Remediation

Configure your web server to prevent information leakage from the SERVER header of its HTTP response.

I hope you'll fix it!

## Impact

An attacker might use the disclosed information to harvest specific security vulnerabilities for the version identified.

## Attachments
- version.PNG
