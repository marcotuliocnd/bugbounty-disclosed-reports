# Mailgun misconfiguration on email.bitwarden.com

## Report Details
- **Report ID**: 272357
- **URL**: https://hackerone.com/reports/272357
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-09-27T10:32:13.527Z
- **Disclosed**: 2017-10-27T12:46:02.640Z

## Reporter
- **Username**: khizer47
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bitwarden

## Vulnerability Information
Hi, 

While checking the subdomains i found that the subdomain email.bitwarden.com upon navigating downloads a file saying "Mailgun Magnificent API" And has the following DNS info

```````````````
DNS Records for email.bitwarden.com
Hostname	Type	TTL	Priority	Content
email.bitwarden.com	SOA	899		ns-586.awsdns-09.net awsdns-hostmaster@amazon.com 1 7200 900 1209600 86400
email.bitwarden.com	NS	86399		ns-133.awsdns-16.com
email.bitwarden.com	NS	86399		ns-1482.awsdns-57.org
email.bitwarden.com	NS	86399		ns-1614.awsdns-09.co.uk
email.bitwarden.com	NS	86399		ns-586.awsdns-09.net
email.bitwarden.com	A	59		52.200.128.214
email.bitwarden.com	A	59		52.3.128.73
email.bitwarden.com	CNAME	299		mailgun.org
email.bitwarden.com	MX	899	10	mxa.mailgun.org
email.bitwarden.com	MX	899	10	mxb.mailgun.org
``````````````````````
I saw a report from @fransrosen #174983 so Following that I added the Subdomain to My mailgun account {F224453}

Now Your subdomain email.bitwarden.com Belongs to my Mailgun account and is under DNS verification process {F224452}

The problem lies in this issue:

You add the domain email.bitwarden.com to Mailgun
Mailgun asks you to add a MX record to email.bitwarden.com
You add that, then Mailgun also tells you that to get tracking you need to add a CNAME from email.email.bitwarden.com to mailgun.org as well.
What is missing here, is for you to actually add email.email.bitwarden.com to your account as a separate domain by itself. By not doing this, anyone can add this domain to their account.
You probably later on remove the MX from email.bitwarden.com again, but the CNAME is still there for email.email.bitwarden.com
The problem with missing out on #4 above is how DNS CNAMEs works. If you have a CNAME pointing to another domain, this CNAME will actually inherit the MX-records from the other domain. This basically means that your email.email.bitwarden.com is now listed with MX-records from Mailgun:

The Verification process takes upto 24+ Hours but i decided to report the issue as soon as possible so it can be migrated :) let me know I can delete the domain from my account so that you guys can set it up again or maybe U simpel need to delete the DNS info 

## Attachments
- 000.JPG
- 00.JPG
- 0.JPG
