# Subdomain takeover on partners.ubnt.com due to non-used CloudFront DNS entry

## Report Details
- **Report ID**: 145224
- **URL**: https://hackerone.com/reports/145224
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-16T18:56:01.472Z
- **Disclosed**: 2016-11-27T17:52:14.451Z

## Reporter
- **Username**: fransrosen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ui

## Vulnerability Information
Hi,

So lately I have discovered that CloudFront is not validating which user that connects a CNAME:d domain to a CloudFront Origin. This means that if I could find a domain that is still pointing to CloudFront, without being connected to any Origin as a Custom CNAME, I can actually claim the domain myself and point it to whatever I want. A vulnerable domain looks like this:
{F99783}

I noticed that this was indeed the result I got on partners.ubnt.com. This domain is currently still pointing to CloudFront, but there is no CF Origin with the domain set as a CNAME.

I have claimed the domain now for PoC using the following setup:
{F99779}

And I have placed a file located under /login for validation and to show what could be a possible variant of an attack:

http://partners.ubnt.com/login

PoC-image:
{F99780}

You should most likely just remove the DNS-entry for this domain, and also make sure you constantly remove DNS records pointing to CloudFront (and other services as well of course) when you stop using them.

As you might understand, the consequences of this are pretty bad. I now can serve whatever I like on this domain, even fetching httpOnly cookies. I would also be able to issue an SSL for this domain through AlphaSSL or Let's Encrypt (that only needs meta/file verification to issue the certificate) That would end up with the ability to read secure cookies as well.

Also, there's no way at all for a visitor of this page to validate that the content on this domain is not served by UBNT, making it extremely easy to utilize this for targeting the organization by fake login forms / spear phishing using your own domain to plant the attack.

We at Detectify have written about this before a few years ago, but we were now able to actually exploit this using CloudFront as well, something that was not known before.

Regards,
Frans

## Attachments
- ubnt-setup.png
- poc-ubnt.png
- vulnerable-cloudfront.png
