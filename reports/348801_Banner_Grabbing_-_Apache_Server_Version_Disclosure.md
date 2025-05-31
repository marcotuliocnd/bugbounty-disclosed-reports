# Banner Grabbing - Apache Server Version Disclosure

## Report Details
- **Report ID**: 348801
- **URL**: https://hackerone.com/reports/348801
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-05-08T08:32:13.236Z
- **Disclosed**: 2018-05-17T09:05:01.273Z

## Reporter
- **Username**: kistimat
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
I have found a little information disclosure on your system.

Banner Grabbing is a technique used to gain information about a remote server. Additionally, this technique is use to get information about remote servers.

I've captured the HTTP request while visiting https://customerupdates.nextcloud.com

POC: 
Simply check screenshot you will see server version of Nextcloud  [Apache/2.4.18 (Ubuntu)]

This information might help an attacker gain a greater understanding of the systems in use and potentially develop further attacks targeted at the specific version of Apache.

Remediation
Configure your web server to prevent information leakage from the SERVER header of its HTTP response.

I hope you'll fix it!

I think and hope this report would impress you.

## Impact

An attacker might use the disclosed information to harvest specific security vulnerabilities for the version identified.

## Attachments
- nextcloud_poc.JPG
