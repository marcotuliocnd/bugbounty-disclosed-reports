# Subdomain Takeover

## Report Details
- **Report ID**: 180393
- **URL**: https://hackerone.com/reports/180393
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2016-11-05T16:41:06.898Z
- **Disclosed**: 2017-05-05T06:03:15.111Z

## Reporter
- **Username**: kholy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: paragonie

## Vulnerability Information
Hello,

Your Subdomain engineering.github.com/paragonie is Pointing to Tumblr.com

You should immediately remove the DNS-entry for engineering.zomato.com is Pointing to Tumblr.com.. Any One Can Claim That Domain , Please Read The Advisory Below.

Remediation
Please make sure you're always going through your DNS-entries so no subdomains are pointing to external services you do not use.

We've written an advisory about this at Detectify:
http://blog.detectify.com/post/100600514143/hostile-subdomain-takeover-using-heroku-github-desk

Where you can read more about this sort of attack.

I Have Done NSLookup For POC :-

nslookup github.com/paragonie
Server: 192.168.188.1
Address: 192.168.188.2#53

Non-authoritative answer:
engineering.zomato.com canonical name = domains.tumblr.com.
Name: domains.tumblr.com
Address: 66.6.42.22
Name: domains.tumblr.com
Address: 66.6.43.22




## Attachments
No attachments
