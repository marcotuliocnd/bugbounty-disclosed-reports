# Outdated Jenkins server hosted at OwnCloud.org

## Report Details
- **Report ID**: 208566
- **URL**: https://hackerone.com/reports/208566
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-02-24T08:22:00.187Z
- **Disclosed**: 2017-03-30T08:26:41.572Z

## Reporter
- **Username**: computer-engineer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: owncloud

## Vulnerability Information
###Summary: 
The target OwnCloud's server is running an outdated version of _Jenkins server_ which is vulnerable to various attacks.

Server Location: `https://ci.owncloud.org`

Vulnerable Software: `Jenkins ver. 2.27`

###Proof of Exploitability

CVE-2016-3727
**POC URL:** `https://ci.owncloud.org/computer/(master)/api/xml`

>Details:

> The API URL /computer/(master)/api/xml allowed users with the extended read permission for the master node to see some global Jenkins configuration, including the configuration of the security realm.

> Source: https://jenkins.io/security/advisory/2016-05-11/


Additionally, the current software version is also vulnerable to RCE.
>CVE-2017-2608

>XStream remote code execution vulnerability

>Affected Versions:  < 2.43

> Source: https://jenkins.io/security/advisory/2017-02-01/

###Recommended Fix
Update Jenkins server to latest version 2.47


## Attachments
- POC_for_CVE-2016-3727.JPG
