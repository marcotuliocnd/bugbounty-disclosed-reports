# EC2 subdomain takeover at http://████████/

## Report Details
- **Report ID**: 1296366
- **URL**: https://hackerone.com/reports/1296366
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-08-09T16:26:45.976Z
- **Disclosed**: 2022-02-14T21:24:17.776Z

## Reporter
- **Username**: dreyand_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
There is a dangling DNS A record that points to an EC2 instance that no longer exists, I was able to claim the EC2 instance and host content on http://███████/.

## Steps To Reproduce:

  1. Visit http://█████████/██████████.html and view the PoC:  ██████


## Suggested Remediation Steps

  Remove the A record pointing to the current ec2 instance. 

## Impact

Hosting content on http://█████/ and potentionally fully bypassing web protections like CORS (in cases of `████████`) or redirecting users to malicious pages.

## Impact

Hosting content on http://██████/ and potentionally fully bypassing web protections like CORS (in cases of `██████████`) or redirecting users to malicious pages,

## System Host(s)
██████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Visit http://██████████/█████.html and view the PoC:  █████

## Suggested Mitigation/Remediation Actions
Remove the A record pointing to the current ec2 instance.



## Attachments
No attachments
