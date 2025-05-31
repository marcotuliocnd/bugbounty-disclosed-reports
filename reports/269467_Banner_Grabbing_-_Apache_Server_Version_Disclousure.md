# Banner Grabbing - Apache Server Version Disclousure

## Report Details
- **Report ID**: 269467
- **URL**: https://hackerone.com/reports/269467
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-09-19T12:46:00.504Z
- **Disclosed**: 2017-10-22T10:07:12.848Z

## Reporter
- **Username**: cybertiger
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: owncloud

## Vulnerability Information
Hello ownCloud, I'd like to report a nice little bug.

Banner Grabbing is a technique used to gain information about a remote server. Additionally, this technique is use to get information about remote servers.

I've captured the HTTP request while visiting https://marketplace.owncloud.com/ and https://owncloud.com

POC: 
Simply check screenshot you will see server version of ownCloud [Apache/2.4.27 (Unix)]

This information might help an attacker gain a greater understanding of the systems in use and potentially develop further attacks targeted at the specific version of Apache.

Impact
An attacker might use the disclosed information to harvest specific security vulnerabilities for the version identified.

Remediation
Configure your web server to prevent information leakage from the SERVER header of its HTTP response.

I hope you'll fix it!

I think and hope this report would impress you.

Let me know if u have any question
Thanks
Cheers
Anas


## Attachments
- moc.png
