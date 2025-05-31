# Sub-Domain Takeover at   http://www.codefi.consensys.net/

## Report Details
- **Report ID**: 1717626
- **URL**: https://hackerone.com/reports/1717626
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-09-30T08:16:28.777Z
- **Disclosed**: 2022-12-16T18:24:27.444Z

## Reporter
- **Username**: krrish_hackk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: consensys

## Vulnerability Information
Summary:
 
Subdomain takeovers:

A subdomain takeover occurs when an attacker gains control over a subdomain of a target domain. Typically, this happens when the subdomain has a canonical name (CNAME) in the Domain Name System (DNS), but no host is providing content for it. This can happen because either a virtual host hasn't been published yet or a virtual host has been removed. An attacker can take over that subdomain by providing their own virtual host and then hosting their own content for it.

If an attacker can do this, they can potentially read cookies set from the main domain, perform cross-site scripting, or circumvent content security policies, thereby enabling them to capture protected information (including logins) or send malicious content to unsuspecting users.

 Steps To Reproduce:

  1. GO to http://consensys.net and find its sub-domains using Subfinder.
  1. now find sub-domains status code.
  1. Search for 404 code.
 4.  its showing :- 
Domain Not Claimed
This domain has been mapped to Squarespace, but it has not yet been claimed by a website. If this is your domain, claim it in the Domains tab of your Website Manager.
5. now create a account at Squarespace, create a website template and then go to use a domain i own.
 6. then copy and paste http://www.codefi.consensys.net/  and  boom sub-domain takeover completed.

Supporting Material/References:

POC is attached below.


 How to prevent it ?

Preventing subdomain takeovers is a matter of order of operations in lifecycle management for virtual hosts and DNS. Depending on the size of the organization, this may require communication and coordination across multiple departments, which can only increase the likelihood for a vulnerable misconfiguration.

Define standard processes for provisioning and deprovisioning hosts. Do all steps as closely together as possible.
Start provisioning by claiming the virtual host; create DNS records last.
Start deprovisioning by removing DNS records first.
Create an inventory of all of your organization's domains and their hosting providers, and update it as things change, to ensure that nothing is left dangling.

## Impact

Risks of a Subdomain Takeover:-

Various risks could be the result of a subdomain takeover.

1. Bypassing CSRF protection
2. Phishing
3. Leak of OAuth 2.0 Tokens
4. The redirect is only performed if the target URL is trusted. If all subdomains are trusted as target URL, an attacker might be able to get OAuth 2.0 tokens via a target URL which points to a compromised subdomain.
5. Bypass Content Security Policy
6. A, AAAA and CNAME Records

## Attachments
- screen-capture.webm
