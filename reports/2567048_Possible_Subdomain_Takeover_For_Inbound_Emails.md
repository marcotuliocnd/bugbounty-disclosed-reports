# Possible Subdomain Takeover For Inbound Emails

## Report Details
- **Report ID**: 2567048
- **URL**: https://hackerone.com/reports/2567048
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2024-06-20T16:58:33.065Z
- **Disclosed**: 2024-08-07T09:14:10.638Z

## Reporter
- **Username**: cryptic_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: smule

## Vulnerability Information
Hello Smule Security Team,
I'm cryptic_, I have identified that the affected url points to sendgrid.net, via a DNS CNAME record. As a result of this an attacker could potentially initate a subdomain take over by registering the subdomain email.smule.com on sendgrid and consiquently leverage this for further attacks. Additionally it has been noted that sendgrid is a service for email marketing so theoretically should an attacker be able to gain access to the subdomain they could potentially gain access to emails too.

## Affected URL
email.smule.com


## Steps To Reproduce:

  1. Go to email.smule.com
  2. You will see 404 Not Found 
  1. Use this command to see the CNAME Record - dig 

## Risk Breakdown
Risk: Medium
Difficulty to Exploit: Medium
Authentication: None

## Recommended Fix
Check your DNS-configuration for subdomains pointing to services not in use.
Set up your external service so it fully listens to your wildcard DNS.


## Reference
https://www.hackerone.com/blog/Guide-Subdomain-Takeovers
http://blog.pentestnepal.tech/post/149985438982/reading-ubers-internal-emails-uber-bug-bounty
https://hackerone.com/reports/166826
https://hackerone.com/reports/403822

## Impact

A way to take over subdomain for inbound emails. An attacker can simply register to sendgrid and takeover this subdomain.

## Attachments
No attachments
