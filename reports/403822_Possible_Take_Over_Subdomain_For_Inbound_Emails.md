# Possible Take Over Subdomain For Inbound Emails 

## Report Details
- **Report ID**: 403822
- **URL**: https://hackerone.com/reports/403822
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-09-01T12:43:59.247Z
- **Disclosed**: 2018-11-08T20:19:27.954Z

## Reporter
- **Username**: rootbakar___
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: khanacademy

## Vulnerability Information
Hello KhanAcademy Security Team,

I'm **rootbakar**, The researcher identified that the affected url points to sendgrid.net, via a DNS CNAME record. As a result of this an attacker could potentially initate a subdomain take over by registering the subdomain sendgrid.khanacademy.org on sendgrid and consiquently leverage this for further attacks. Additionally it has been noted that sendgrid is a service for email marketing so theoretically should an attacker be able to gain access to the subdomain they could potentially gain access to emails too.


###Affected URLs
sendgrid.khanacademy.org

###Risk Breakdown
Risk: **Medium**
Difficulty to Exploit: **Medium** 
Authentication: None

###Recommended Fix
Check your DNS-configuration for subdomains pointing to services not in use.
Set up your external service so it fully listens to your wildcard DNS.


###Reference
https://www.hackerone.com/blog/Guide-Subdomain-Takeovers
http://blog.pentestnepal.tech/post/149985438982/reading-ubers-internal-emails-uber-bug-bounty
https://hackerone.com/reports/166826

## Impact

**a way to take over subdomain for inbound emails**

## Attachments
- 2.png
- 1.png
