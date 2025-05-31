# URGENT - Subdomain Takeover on status.vimeo.com due to unclaimed domain pointing to statuspage.io

## Report Details
- **Report ID**: 49663
- **URL**: https://hackerone.com/reports/49663
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-02-28T18:36:46.860Z
- **Disclosed**: 2015-04-18T09:57:10.447Z

## Reporter
- **Username**: avlidienbrunn
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: vimeo

## Vulnerability Information
Hi,

**Brief**
This is an urgent issue and I hope you will act on it likewise.
Your subdomain status.vimeo.com is pointing to hosted.statuspage.io, but no statuspage was connected to it. This means that anyone can claim the subdomain by setting up a statuspage.io site and using "status.vimeo.com" as the name!

*You should immediately remove the DNS-entry for statu.vimeo.com pointing to statuspage.io.*

Since I have complete control over the subdomain I can do whatever I want on it. Creating a login form that would fool anyone, since it's present on a vimeo.com domain, abuse same origin bugs, get/set vimeo cookies, you name it!

**PoC**
PoC-link:
http://status.vimeo.com

**Remediation**
Please make sure you're always going through your DNS-entries so no subdomains are pointing to external services you do not use.

We've written an advisory about this at Detectify:
http://blog.detectify.com/post/100600514143/hostile-subdomain-takeover-using-heroku-github-desk

Where you can read more about this sort of attack.

Best,
Mathias

## Attachments
No attachments
