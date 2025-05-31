# IDOR on DoD Website exposes FTP users and passes linked to all accounts!

## Report Details
- **Report ID**: 228383
- **URL**: https://hackerone.com/reports/228383
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-05-14T21:23:33.371Z
- **Disclosed**: 2019-10-04T15:21:57.473Z

## Reporter
- **Username**: cdl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
https://████/██████/ is vulnerable to Insecure Direct Object Reference. The application does not validate whether or not who a Push Server belongs to thus allowing an attacker to view the credentials of any FTP / sFTP server linked to any user's account. 

## Impact
An attacker can view anybody's FTP server information, thus **compromising** the user's FTP servers. This also allows an attacker to **update** or **edit** the Push Server in the ██████████ CMS.

## Step-by-step Reproduction Instructions
1. Log into or create an account on `https://██████████/██████████`
2. Now visit `https://████████/█████/filepush/ftp/303/` 

You will be able to see my ftp server details and you will be able to update or delete it!

An attacker can bruteforce the id to see if the server gives back a valid response. The attacker can then log into the person's FTP servers with the credentials stolen using this vulnerability, giving them full access to private / confidential information!

Example: `https://██████████/█████████/filepush/ftp/1/`

Hostname: ██████
Username: ██████
Password: █████
Path: /from_pub/cr/████████

`https://█████████/████/filepush/ftp/<ID>/`

## Suggested Mitigation/Remediation Actions
Check whether or the user's account should have access to the specified Push Server

## Attachments
No attachments
